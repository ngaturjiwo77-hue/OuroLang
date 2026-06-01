import struct
import re
import sys
import os

# 1. PREPROCESSOR: Membaca file dan mengekspansi BAWAKAN & Makro
def parse_file(filepath, visited=None):
    if visited is None: visited = set()
    if filepath in visited or not os.path.exists(filepath):
        return []
    visited.add(filepath)
    
    with open(filepath, 'r') as f:
        source = f.read()
        
    raw_tokens = [m.group(0) for m in re.finditer(r'"[^"]*"|\S+', source)]
    tokens = []
    
    i = 0
    while i < len(raw_tokens):
        token = raw_tokens[i]
        if token == "BAWAKAN":
            i += 1
            inc_file = raw_tokens[i].strip('"')
            tokens.extend(parse_file(inc_file, visited)) # Rekursif import
        elif token == "NAIK":
            i += 1
            tokens.extend(["TAMBAH", raw_tokens[i], "1"])
        elif token == "TURUN":
            i += 1
            tokens.extend(["KURANG", raw_tokens[i], "1"])
        elif token == "UBAH":
            i += 1
            var1 = raw_tokens[i]
            i += 1
            var2 = raw_tokens[i]
            tokens.extend(["SIMPAN", var1, "0", "TAMBAH_VAR", var1, var2])
        else:
            tokens.append(token)
        i += 1
    return tokens

# 2. KOMPILATOR UTAMA
def compile_ouro(input_file, output_file):
    tokens = parse_file(input_file)
    out = bytearray(b'\x00' * 17) # Header ELF
    jump_stack = []
    loop_stack = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token == "PROGRAM_UTAMA": out.append(1)
        elif token == "BATAS_PROGRAM": out.extend([2, 255])
        
        # Operasi Standar
        elif token == "CETAK_TEKS":
            out.append(61)
            i += 1; out.extend(tokens[i].strip('"').replace('\\n', '\n').encode('utf-8') + b'\0')
        elif token in ["CETAK_ANGKA", "BUKA_BACA", "BUKA_TULIS"]:
            ops = {"CETAK_ANGKA": 62, "BUKA_BACA": 70, "BUKA_TULIS": 73}
            out.append(ops[token])
            i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
        elif token in ["SIMPAN", "TAMBAH", "KURANG"]:
            ops = {"SIMPAN": 10, "TAMBAH": 11, "KURANG": 24}
            out.append(ops[token])
            i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1; out.extend(struct.pack("<i", int(tokens[i])))
        elif token in ["TAMBAH_VAR", "KURANG_VAR"]:
            ops = {"TAMBAH_VAR": 12, "KURANG_VAR": 25}
            out.append(ops[token])
            i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            
        # Logika IF
        elif token == "BILA_SAMA":
            out.append(32)
            i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1; out.extend(struct.pack("<i", int(tokens[i])))
            jump_stack.append(len(out))
            out.extend(struct.pack("<i", 0))
        elif token == "BATAS_BILA":
            if jump_stack:
                jp = jump_stack.pop()
                struct.pack_into("<i", out, jp, len(out))

        # Logika LOOP (Perulangan)
        elif token in ["SELAMA_SAMA", "SELAMA_KURANG"]:
            loop_start = len(out)
            out.append(32) # Menggunakan logika Lompat Jika Salah
            i += 1; out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1
            # Ekstrak nilai (Bisa angka bisa variabel, kita asumsikan angka dulu untuk aman)
            val = int(tokens[i]) if tokens[i].isdigit() else 0 
            out.extend(struct.pack("<i", val))
            loop_stack.append((loop_start, len(out)))
            out.extend(struct.pack("<i", 0))
        elif token == "BATAS_SELAMA":
            if loop_stack:
                start_pos, patch_pos = loop_stack.pop()
                out.append(31) # LOMPAT_KE kembali ke awal
                out.extend(struct.pack("<i", start_pos))
                struct.pack_into("<i", out, patch_pos, len(out)) # Keluar loop

        i += 1

    with open(output_file, 'wb') as f:
        f.write(out)
    print(f"✅ [ULTIMATE BOOTSTRAPPER] Berhasil merakit {len(out)} bytes. Preprocessor Aktif!")

if __name__ == "__main__":
    compile_ouro(sys.argv[1] if len(sys.argv) > 1 else "input.ouro", "output.obf")
