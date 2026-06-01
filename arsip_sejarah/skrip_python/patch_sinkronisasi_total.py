import os, subprocess, re

print("⚙️ Memulai Penyatuan Absolut...")

# ==================================================
# 1. PERBAIKAN VM C (Menambah Opcode 76: TULIS_BYTE_VAR)
# ==================================================
vm_path = 'src/vm/ouro_vm.c'
with open(vm_path, 'r') as f: vm = f.read()
if "case 76:" not in vm:
    op76 = '            case 76: {char n[64];baca_string(f,n,sizeof(n));int s=baca_var("FD");if(s>=0&&s<file_count&&files[s])fputc(baca_var(n)&0xFF,files[s]);break;}\n'
    vm = vm.replace('case OP_TULIS_BYTE:', op76 + '            case OP_TULIS_BYTE:')
    with open(vm_path, 'w') as f: f.write(vm)
    subprocess.run(['gcc', 'src/vm/ouro_vm.c', '-o', 'bin/ouro_vm'])
    print("✅ [VM] Opcode 76 (TULIS_BYTE_VAR) berhasil disuntikkan!")

# ==================================================
# 2. PERBAIKAN KOMPILATOR.OURO (Memperbaiki I/O dan Fungsi)
# ==================================================
komp_path = 'src/compiler/kompilator.ouro'
with open(komp_path, 'r') as f: komp = f.read()
if "BUKA_BACA" not in komp:
    komp = komp.replace('BUKA_FILE "output.obf" FILE_OUT', 'BUKA_BACA "input.ouro" FILE_IN\n        BUKA_TULIS "output.obf" FILE_OUT')
    with open(komp_path, 'w') as f: f.write(komp)
    print("✅ [KOMPILATOR] Logika I/O File (BUKA_BACA & BUKA_TULIS) diperbaiki!")

# ==================================================
# 3. PENEMPAAN SUPER BOOTSTRAPPER PYTHON
# ==================================================
boot_path = 'ouro_bootstrap_final.py'
super_boot = r"""import struct, re, sys, os

def safe_int(v):
    v_clean = v.strip('"').lstrip('-')
    if v_clean.isdigit(): return int(v.strip('"'))
    if all(c in '0123456789ABCDEFabcdef' for c in v_clean) and len(v_clean) > 0:
        try:
            val = int(v_clean, 16)
            return -val if v.startswith('-') else val
        except ValueError: pass
    return 0

def parse_file(filepath, visited=None, globals_dict=None, funcs=None):
    if visited is None: visited = set()
    if globals_dict is None: globals_dict = {}
    if funcs is None: funcs = {}
    if not os.path.exists(filepath): return []
    if filepath in visited: return []
    visited.add(filepath)

    with open(filepath, 'r') as f: source = f.read()
    raw_tokens = [m.group(0) for m in re.finditer(r'"[^"]*"|\S+', source)]
    tokens = []
    j = 0
    KNOWN = {"SIMPAN", "ARRAY_SIMPAN", "BACA_ARRAY", "ARRAY_AMBIL", "TULIS_BYTE_VAR", "SELAMA_KURANG", "SELAMA_SAMA", "BILA_SAMA", "BILA_LEBIH_SAMA", "PANGGIL_PARAM", "PANGGIL_KEMBALI", "BAGI", "KALI", "TAMBAH", "KURANG", "NAIK", "TURUN", "UBAH", "ULANGI"}
    
    while j < len(raw_tokens):
        token = raw_tokens[j]
        if token == "BAWAKAN":
            j += 1; inc_file = raw_tokens[j].strip('"')
            inc_path = os.path.join(os.path.dirname(filepath), inc_file) if os.path.dirname(filepath) else inc_file
            if not os.path.exists(inc_path): inc_path = inc_file
            tokens.extend(parse_file(inc_path, visited, globals_dict, funcs))
        elif token == "GLOBAL":
            j += 1; name = raw_tokens[j]; j += 1; globals_dict[name] = raw_tokens[j]
        elif token == "GLOBAL_ARRAY":
            j += 1; name = raw_tokens[j]; j += 1; size = raw_tokens[j]
            tokens.extend(["ARRAY_BUAT", name, size])
        elif token in ["FUNGSI_PARAM", "FUNGSI_KEMBALI"]:
            func_name = raw_tokens[j+1]; j += 2
            args = []
            while j < len(raw_tokens) and raw_tokens[j] not in KNOWN and raw_tokens[j] not in ["BATAS_FUNGSI", "KEMBALIKAN", "TULIS_KARAKTER"]:
                args.append(raw_tokens[j]); j += 1
            body = []
            while j < len(raw_tokens) and raw_tokens[j] != "BATAS_FUNGSI":
                body.append(raw_tokens[j]); j += 1
            funcs[func_name] = (args, body)
        elif token in ["PANGGIL_PARAM", "PANGGIL_KEMBALI"]:
            is_ret = (token == "PANGGIL_KEMBALI"); j += 1
            ret_var = raw_tokens[j] if is_ret else None
            if is_ret: j += 1
            func_name = raw_tokens[j]
            
            # Cerdas Memilih TULIS_BYTE (Konstan) atau TULIS_BYTE_VAR (Variabel)
            if func_name == "TULIS_BYTE":
                fd_arg = raw_tokens[j+1]; val_arg = raw_tokens[j+2]; j += 2
                tokens.extend(["SIMPAN", "FD", "0", "TAMBAH_VAR", "FD", fd_arg])
                if val_arg.isdigit() or (val_arg.startswith('-') and val_arg[1:].isdigit()) or "OP_" in val_arg:
                    tokens.extend(["TULIS_BYTE", val_arg])
                else:
                    tokens.extend(["TULIS_BYTE_VAR", val_arg])
            elif func_name in funcs:
                args, body = funcs[func_name]
                call_args = [raw_tokens[j+1+k] for k in range(len(args))]
                j += len(args)
                inst_body = []
                for bt in body:
                    replaced = bt
                    for k, a in enumerate(args):
                        if bt == a: replaced = call_args[k]
                    if replaced == "KEMBALIKAN" and is_ret:
                        inst_body.extend(["SIMPAN", ret_var])
                    elif replaced == "TULIS_KARAKTER":
                        pass # Diabaikan karena sudah ditangani native
                    else:
                        inst_body.append(replaced)
                tokens.extend(inst_body)
            else:
                tokens.append(token)
        elif token == "NAIK":
            j += 1; tokens.extend(["TAMBAH", raw_tokens[j], "1"])
        elif token == "TURUN":
            j += 1; tokens.extend(["KURANG", raw_tokens[j], "1"])
        elif token == "UBAH":
            j += 1; v1 = raw_tokens[j]; j += 1; v2 = raw_tokens[j]
            tokens.extend(["SIMPAN", v1, "0", "TAMBAH_VAR", v1, v2])
        elif token == "ULANGI":
            j += 1; cnt = raw_tokens[j]
            tokens.extend(["SIMPAN", "ULG_IDX", "0", "SELAMA_KURANG", "ULG_IDX", cnt])
        elif token == "BATAS_ULANGI":
            tokens.extend(["NAIK", "ULG_IDX", "BATAS_SELAMA"])
        else:
            tokens.append(globals_dict.get(token, token))
        j += 1
    return tokens

def compile_ouro(input_file, output_file):
    tokens = parse_file(input_file)
    out = bytearray(b'\x00' * 17)
    jump_stack, loop_stack = [], []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t == "PROGRAM_UTAMA": out.append(1)
        elif t == "BATAS_PROGRAM": out.extend([2, 255])
        elif t in ["BACA_KARAKTER", "TUTUP_FILE", "STRING_MULAI", "STRING_TULIS_BUFFER", "KONVERSI_STR_KE_INT"]:
            ops = {"BACA_KARAKTER": 71, "TUTUP_FILE": 72, "STRING_MULAI": 80, "STRING_TULIS_BUFFER": 86, "KONVERSI_STR_KE_INT": 88}
            out.append(ops[t])
        elif t == "CETAK_TEKS":
            out.append(61); i += 1; out.extend(tokens[i].strip('"').replace('\\n', '\n').encode('utf-8') + b'\0')
        elif t in ["CETAK_ANGKA", "TUMPUK_FILE", "PULIH_FILE", "BAWAKAN_FILE", "BUKA_BACA", "BUKA_TULIS", "TULIS_INT32", "STRING_TAMBAH_VAR", "STRING_BANDING", "ARRAY_BUAT"]:
            ops = {"CETAK_ANGKA": 62, "TUMPUK_FILE": 98, "PULIH_FILE": 99, "BAWAKAN_FILE": 96, "BUKA_BACA": 70, "BUKA_TULIS": 73, "TULIS_INT32": 75, "STRING_TAMBAH_VAR": 84, "STRING_BANDING": 83, "ARRAY_BUAT": 90}
            out.append(ops[t]); i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
        elif t in ["TULIS_BYTE", "LOMPAT_KE"]:
            ops = {"TULIS_BYTE": 74, "LOMPAT_KE": 31}
            out.append(ops[t]); i += 1; out.extend(struct.pack("<i", safe_int(tokens[i])))
        elif t == "TULIS_BYTE_VAR":
            out.append(76); i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
        elif t in ["SIMPAN", "TAMBAH", "KURANG", "KALI", "BAGI"]:
            ops = {"SIMPAN": 10, "TAMBAH": 11, "KURANG": 24, "KALI": 22, "BAGI": 23}
            out.append(ops[t]); i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1; out.extend(struct.pack("<i", safe_int(tokens[i])))
        elif t in ["TAMBAH_VAR", "KURANG_VAR", "KALI_VAR", "BAGI_VAR"]:
            ops = {"TAMBAH_VAR": 12, "KURANG_VAR": 25, "KALI_VAR": 26, "BAGI_VAR": 27}
            out.append(ops[t]); i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
        elif t in ["ARRAY_SIMPAN", "ARRAY_ISI", "ARRAY_AMBIL", "BACA_ARRAY"]:
            ops = {"ARRAY_SIMPAN": 91, "ARRAY_ISI": 92, "ARRAY_AMBIL": 93, "BACA_ARRAY": 93}
            out.append(ops[t]); i += 1
            if t == "ARRAY_AMBIL" or t == "BACA_ARRAY":
                out.extend(tokens[i].encode('utf-8') + b'\0'); i += 1
            out.extend(tokens[i].encode('utf-8') + b'\0'); i += 1
            out.extend(tokens[i].encode('utf-8') + b'\0')
            if t == "ARRAY_SIMPAN":
                i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            elif t == "ARRAY_ISI":
                i += 1; out.extend(struct.pack("<i", safe_int(tokens[i])))
        elif t in ["BILA_SAMA", "BILA_LEBIH_SAMA", "SELAMA_SAMA", "SELAMA_KURANG"]:
            loop_start = len(out) if "SELAMA" in t else None
            ops = {"BILA_SAMA": 32, "BILA_LEBIH_SAMA": 35, "SELAMA_SAMA": 32, "SELAMA_KURANG": 35}
            out.append(ops[t]); i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1; out.extend(struct.pack("<i", safe_int(tokens[i])))
            if loop_start: loop_stack.append((loop_start, len(out)))
            else: jump_stack.append(len(out))
            out.extend(struct.pack("<i", 0))
        elif t == "BATAS_BILA":
            if jump_stack: struct.pack_into("<i", out, jump_stack.pop(), len(out))
        elif t == "BATAS_SELAMA":
            if loop_stack:
                ls, lp = loop_stack.pop(); out.append(31); out.extend(struct.pack("<i", ls))
                struct.pack_into("<i", out, lp, len(out))
        i += 1
    with open(output_file, 'wb') as f: f.write(out)
    print(f"✅ [SUPER BOOTSTRAPPER] Berhasil merakit {len(out)} bytes. OuroLang Siap Mandiri!")

if __name__ == "__main__":
    compile_ouro("src/compiler/kompilator.ouro", "build/ouroc.obf")
"""
with open(boot_path, 'w') as f: f.write(super_boot)
print("✅ [PYTHON] Super Bootstrapper berhasil diciptakan!")

print("🚀 Merakit ulang otak kompilator untuk terakhir kalinya...")
subprocess.run(['python3', boot_path])
