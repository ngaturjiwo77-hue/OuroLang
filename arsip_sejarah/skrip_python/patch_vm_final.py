vm_path = 'src/vm/ouro_vm.c'
with open(vm_path, 'r') as f: vm = f.read()

# Memperbaiki pembacaan nama file di Opcode 96 agar kebal dari whitespace/pindah baris
blok_fitur_file = """            case 96: { // OP_BAWAKAN_FILE
                int idx = cari_array("BUFFER_TOKEN");
                int p = baca_var("PANJANG_TOKEN");
                if(idx != -1 && p > 0 && p < 256) {
                    char filename[256];
                    int len = 0;
                    for(int i=0; i<p; i++) {
                        char c = (char)data_array[idx][i];
                        if(c != '\\n' && c != '\\r' && c != ' ' && c != '\\t') {
                            filename[len++] = c;
                        }
                    }
                    filename[len] = '\\0';
                    FILE* new_f = fopen(filename, "r");
                    if(new_f) {
                        if(tf_sp < MAX_FILE_STACK) tumpukan_fd[tf_sp++] = baca_var("FD");
                        files[file_count] = new_f;
                        simpan_var("FD", file_count++);
                    } else {
                        // Jika gagal, jangan putus alur, cetak peringatan
                        printf("[PERINGATAN] File tidak ditemukan: '%s'\\n", filename);
                    }
                }
                break;
            }"""

import re
vm = re.sub(r'case 96: \{.*?break;\s*\}', blok_fitur_file, vm, flags=re.DOTALL)

with open(vm_path, 'w') as f: f.write(vm)
print("✅ [VM C] Pembersihan nama file dinamis berhasil disempurnakan!")
