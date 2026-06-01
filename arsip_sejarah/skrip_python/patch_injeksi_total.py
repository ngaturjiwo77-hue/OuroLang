import os, subprocess

# ==========================================
# 1. INJEKSI VIRTUAL MACHINE (ouro_vm.c)
# ==========================================
vm_path = 'src/vm/ouro_vm.c'
try:
    with open(vm_path, 'r') as f: vm_code = f.read()

    # Tambahkan memori stack (Jika belum ada)
    stack_code = "\n// === SISTEM TUMPUKAN FILE ===\n#define MAX_FILE_STACK 16\nstatic FILE* tumpukan_file[MAX_FILE_STACK];\nstatic int tf_sp = 0;\n"
    if "MAX_FILE_STACK" not in vm_code:
        vm_code = vm_code.replace("static int ret_sp = 0;", "static int ret_sp = 0;" + stack_code)
        
        # Tambahkan Opcode 98 dan 99
        opcodes = """
        case 98: { // OP_TUMPUK_FILE
            char var_nama[64]; baca_string(f, var_nama, 64);
            // Catatan: Implementasi pointer C disesuaikan dengan engine Anda
            break;
        }
        case 99: { // OP_PULIH_FILE
            char var_nama[64]; baca_string(f, var_nama, 64);
            break;
        }
"""
        vm_code = vm_code.replace('default:', opcodes + '        default:')
        with open(vm_path, 'w') as f: f.write(vm_code)
        print("✅ [VM] Struktur Tumpukan File disuntikkan ke ouro_vm.c")
        subprocess.run(['gcc', 'src/vm/ouro_vm.c', '-o', 'bin/ouro_vm'])
except Exception as e:
    print(f"⚠️ Melewati patch VM: {e}")

# ==========================================
# 2. INJEKSI KOMPILATOR (kompilator.ouro)
# ==========================================
komp_path = 'src/compiler/kompilator.ouro'
try:
    with open(komp_path, 'r') as f: komp_code = f.read()

    # Tambahkan variabel LEVEL_FILE
    if "GLOBAL LEVEL_FILE" not in komp_code:
        komp_code = komp_code.replace("GLOBAL JUMLAH_MAKRO 0", "GLOBAL JUMLAH_MAKRO 0\nGLOBAL LEVEL_FILE 0")

    # Blok Logika EOF & BAWAKAN
    blok_baru = """
            BILA_SAMA ADA_KATA 0
                BILA_LEBIH_SAMA LEVEL_FILE 1
                    TUTUP_FILE FILE_IN
                    PULIH_FILE FILE_IN
                    TURUN LEVEL_FILE
                    SIMPAN ADA_KATA 1
                    LANJUTKAN
                BATAS_BILA
            BATAS_BILA

            BILA_SAMA SIDIK_JARI 2028
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                TUMPUK_FILE FILE_IN
                BUKA_BACA BUFFER_TOKEN FILE_IN
                NAIK LEVEL_FILE
                LANJUTKAN
            BATAS_BILA
"""
    if "2028" not in komp_code:
        komp_code = komp_code.replace("        BATAS_BILA\n    BATAS_SELAMA", blok_baru + "        BATAS_BILA\n    BATAS_SELAMA")
        with open(komp_path, 'w') as f: f.write(komp_code)
        print("✅ [KOMPILATOR] Logika EOF dan BAWAKAN (Hash: 2028) disuntikkan!")
except Exception as e:
    print(f"❌ Gagal menyuntik kompilator: {e}")

# ==========================================
# 3. INJEKSI BOOTSTRAPPER PYTHON
# ==========================================
boot_path = 'ouro_bootstrap_final.py'
try:
    with open(boot_path, 'r') as f: boot_code = f.read()
    if "TUMPUK_FILE" not in boot_code:
        boot_code = boot_code.replace('"CETAK_ANGKA": 62,', '"CETAK_ANGKA": 62, "TUMPUK_FILE": 98, "PULIH_FILE": 99,')
        boot_code = boot_code.replace('["CETAK_ANGKA",', '["CETAK_ANGKA", "TUMPUK_FILE", "PULIH_FILE",')
        with open(boot_path, 'w') as f: f.write(boot_code)
        print("✅ [BOOTSTRAPPER] Jembatan Python siap memproses Opcode baru!")
except Exception as e:
    print(f"⚠️ Melewati patch Python: {e}")

