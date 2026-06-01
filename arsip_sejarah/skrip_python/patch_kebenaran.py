import os, subprocess

# 1. PERBAIKI MESIN C (Rak Buku yang sesungguhnya)
vm_path = 'src/vm/ouro_vm.c'
with open(vm_path, 'r') as f: vm = f.read()
if "tumpukan_file[tf_sp++] = f_in;" not in vm:
    vm = vm.replace("// Catatan: Implementasi pointer C disesuaikan dengan engine Anda", 
                    "if(f_in != NULL && tf_sp < MAX_FILE_STACK) tumpukan_file[tf_sp++] = f_in;")
    vm = vm.replace("case 99: { // OP_PULIH_FILE\n            char var_nama[64]; baca_string(f, var_nama, 64);\n            break;",
                    "case 99: { // OP_PULIH_FILE\n            char var_nama[64]; baca_string(f, var_nama, 64);\n            if(tf_sp > 0) f_in = tumpukan_file[--tf_sp];\n            break;")
    with open(vm_path, 'w') as f: f.write(vm)
    subprocess.run(['gcc', 'src/vm/ouro_vm.c', '-o', 'bin/ouro_vm'])
    print("✅ [VM] Rak Buku C telah diperbaiki!")

# 2. PERBAIKI KOMPILATOR OURO
komp_path = 'src/compiler/kompilator.ouro'
with open(komp_path, 'r') as f: komp = f.read()

# Hapus pemaksaan input.ouro dan perbaiki penulisan file
komp = komp.replace('BUKA_BACA "input.ouro" FILE_IN\n', '')
komp = komp.replace('BUKA_FILE "output.obf"', 'BUKA_TULIS "output.obf"')

# Perbaiki bug Opcode 22 (KALI) yang menyusup ke CETAK_ANGKA
komp = komp.replace('PANGGIL_PARAM TULIS_BYTE FILE_OUT 22', 'PANGGIL_PARAM TULIS_BYTE FILE_OUT OP_CETAK_ANGKA')

# Rombak sistem Perulangan Utama agar tahan banting
loop_lama = """    SELAMA_SAMA ADA_KATA 1
        PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN"""
        
loop_baru = """    SIMPAN BERJALAN 1
    SELAMA_SAMA BERJALAN 1
        PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN

        BILA_SAMA ADA_KATA 0
            BILA_LEBIH_SAMA LEVEL_FILE 1
                TUTUP_FILE FILE_IN
                PULIH_FILE FILE_IN
                TURUN LEVEL_FILE
                SIMPAN ADA_KATA 1
            BATAS_BILA
            BILA_SAMA LEVEL_FILE 0
                SIMPAN BERJALAN 0
            BATAS_BILA
        BATAS_BILA
        
        BILA_SAMA ADA_KATA 1"""

if "SIMPAN BERJALAN 1" not in komp:
    komp = komp.replace(loop_lama, loop_baru)
    # Hapus blok logika EOF usang yang ada di bawah
    komp = komp.replace("""            BILA_SAMA ADA_KATA 0
                BILA_LEBIH_SAMA LEVEL_FILE 1
                    TUTUP_FILE FILE_IN
                    PULIH_FILE FILE_IN
                    TURUN LEVEL_FILE
                    SIMPAN ADA_KATA 1
                    LANJUTKAN
                BATAS_BILA
            BATAS_BILA""", "")
    # Tutup BILA_SAMA ADA_KATA 1 yang baru
    komp = komp.replace("        BATAS_BILA\n    BATAS_SELAMA", "        BATAS_BILA\n        BATAS_BILA\n    BATAS_SELAMA")
    with open(komp_path, 'w') as f: f.write(komp)
    print("✅ [KOMPILATOR] Logika File & Loop berhasil dibersihkan!")

