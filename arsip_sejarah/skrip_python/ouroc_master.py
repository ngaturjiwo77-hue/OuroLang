import struct
import re
import sys

def compile_ouro(input_file, output_file):
    with open(input_file, 'r') as f:
        source = f.read()

    tokens = [m.group(0) for m in re.finditer(r'"[^"]*"|\S+', source)]
    out = bytearray(b'\x00' * 17) # Header
    jump_stack = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # 1. PERINTAH TANPA ARGUMEN
        if token == "PROGRAM_UTAMA": out.append(1)
        elif token == "BATAS_PROGRAM": out.extend([2, 255])
        elif token in ["BACA_KARAKTER", "TUTUP_FILE", "STRING_MULAI", "STRING_TULIS_BUFFER", "KONVERSI_STR_KE_INT"]:
            ops = {"BACA_KARAKTER": 71, "TUTUP_FILE": 72, "STRING_MULAI": 80, "STRING_TULIS_BUFFER": 86, "KONVERSI_STR_KE_INT": 88}
            out.append(ops[token])
            
        # 2. PERINTAH TEKS (Dengan penanganan Baris Baru)
        elif token == "CETAK_TEKS":
            out.append(61)
            i += 1
            teks = tokens[i].strip('"').replace('\\n', '\n')
            out.extend(teks.encode('utf-8') + b'\0')

        # 3. PERINTAH DENGAN 1 ARGUMEN (Nama Variabel / String)
        elif token in ["CETAK_ANGKA", "BUKA_BACA", "BUKA_TULIS", "TULIS_INT32", "STRING_TAMBAH_VAR", "STRING_BANDING"]:
            ops = {"CETAK_ANGKA": 62, "BUKA_BACA": 70, "BUKA_TULIS": 73, "TULIS_INT32": 75, "STRING_TAMBAH_VAR": 84, "STRING_BANDING": 83}
            out.append(ops[token])
            i += 1
            out.extend(tokens[i].encode('utf-8') + b'\0')

        # 4. PERINTAH DENGAN 1 ARGUMEN (Angka)
        elif token in ["TULIS_BYTE", "LOMPAT_KE"]:
            ops = {"TULIS_BYTE": 74, "LOMPAT_KE": 31}
            out.append(ops[token])
            i += 1
            out.extend(struct.pack("<i", int(tokens[i])))

        # 5. PERINTAH DENGAN 2 ARGUMEN (Variabel + Angka)
        elif token in ["SIMPAN", "TAMBAH", "KURANG", "KALI", "BAGI"]:
            ops = {"SIMPAN": 10, "TAMBAH": 11, "KURANG": 24, "KALI": 22, "BAGI": 23}
            out.append(ops[token])
            i += 1
            out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1
            out.extend(struct.pack("<i", int(tokens[i])))

        # 6. PERINTAH DENGAN 2 ARGUMEN (Variabel + Variabel)
        elif token in ["TAMBAH_VAR", "KURANG_VAR", "KALI_VAR", "BAGI_VAR"]:
            ops = {"TAMBAH_VAR": 12, "KURANG_VAR": 25, "KALI_VAR": 26, "BAGI_VAR": 27}
            out.append(ops[token])
            i += 1
            out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1
            out.extend(tokens[i].encode('utf-8') + b'\0')

        # 7. MANAJEMEN LOMPATAN (IF / BILA_SAMA)
        elif token == "BILA_SAMA":
            out.append(32) # OP_LOMPAT_JIKA_SALAH
            i += 1
            out.extend(tokens[i].encode('utf-8') + b'\0')
            i += 1
            out.extend(struct.pack("<i", int(tokens[i])))
            jump_stack.append(len(out)) # Catat posisi untuk kembali
            out.extend(struct.pack("<i", 0)) # Alokasi 4 byte kosong
        elif token == "BATAS_BILA":
            if jump_stack:
                jump_pos = jump_stack.pop()
                struct.pack_into("<i", out, jump_pos, len(out)) # Suntik jarak lompatan yang sebenarnya

        i += 1

    with open(output_file, 'wb') as f:
        f.write(out)
    print(f"✅ [OUROC MASTER] Berhasil merakit {len(out)} bytes. OuroLang siap 100%!")

if __name__ == "__main__":
    input_f = sys.argv[1] if len(sys.argv) > 1 else "input.ouro"
    output_f = sys.argv[2] if len(sys.argv) > 2 else "output.obf"
    compile_ouro(input_f, output_f)
