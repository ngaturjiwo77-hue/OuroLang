import os, subprocess, re

# 1. PERBAIKI MESIN C (Buka File dari Array Memori)
vm_path = 'src/vm/ouro_vm.c'
with open(vm_path, 'r') as f: vm = f.read()
if "case 96:" not in vm:
    op96 = """
        case 96: { // OP_BAWAKAN_FILE
            int idx = cari_array("BUFFER_TOKEN");
            int p = baca_var("PANJANG_TOKEN");
            if(idx != -1 && p > 0 && p < 256) {
                char filename[256];
                for(int i=0; i<p; i++) filename[i] = (char)data_array[idx][i];
                filename[p] = '\\0';
                FILE* new_f = fopen(filename, "r");
                if(new_f) {
                    if(f_in != NULL && tf_sp < MAX_FILE_STACK) tumpukan_file[tf_sp++] = f_in;
                    f_in = new_f;
                } else {
                    printf("[PERINGATAN] Gagal BAWAKAN file: %s\\n", filename);
                }
            }
            break;
        }
"""
    vm = vm.replace('default:', op96 + '        default:')
    with open(vm_path, 'w') as f: f.write(vm)
    subprocess.run(['gcc', 'src/vm/ouro_vm.c', '-o', 'bin/ouro_vm'])
    print("✅ [VM] Mesin C kini bisa membuka file dinamis (Opcode 96)!")

# 2. PERBAIKI KOMPILATOR OURO (Menulis Variabel & Buka Dinamis)
komp_path = 'src/compiler/kompilator.ouro'
with open(komp_path, 'r') as f: komp = f.read()

# Ubah BUKA_BACA statis menjadi BAWAKAN_FILE dinamis
komp = komp.replace("TUMPUK_FILE FILE_IN\n                BUKA_BACA BUFFER_TOKEN FILE_IN", "BAWAKAN_FILE")

# Ubah makro GLOBAL menjadi instruksi SIMPAN (Variabel Sejati)
global_baru = """BILA_SAMA SIDIK_JARI 1912
                PANGGIL_PARAM TULIS_BYTE FILE_OUT 10
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_PARAM TULIS_BUFFER_KODE FILE_OUT
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_KEMBALI NILAI_ASLI STRING_KE_ANGKA
                PANGGIL_PARAM TULIS_ANGKA_4BYTE FILE_OUT NILAI_ASLI
                LANJUTKAN
            BATAS_BILA"""
komp = re.sub(r'BILA_SAMA SIDIK_JARI 1912.*?BATAS_BILA', global_baru, komp, flags=re.DOTALL)

with open(komp_path, 'w') as f: f.write(komp)
print("✅ [KOMPILATOR] Logika BAWAKAN dan GLOBAL disempurnakan!")

# 3. PERBAIKI BOOTSTRAPPER PYTHON
boot_path = 'ouro_bootstrap_final.py'
with open(boot_path, 'r') as f: boot = f.read()
if "BAWAKAN_FILE" not in boot:
    boot = boot.replace('"PULIH_FILE": 99,', '"PULIH_FILE": 99, "BAWAKAN_FILE": 96,')
    boot = boot.replace('"PULIH_FILE",', '"PULIH_FILE", "BAWAKAN_FILE",')
    with open(boot_path, 'w') as f: f.write(boot)

