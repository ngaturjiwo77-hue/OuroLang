import os, subprocess

vm_path = 'src/vm/ouro_vm.c'

try:
    with open(vm_path, 'r') as f:
        code = f.read()

    # 1. Menyuntikkan Variabel Call Stack (Jika belum ada)
    if 'MAX_CALL' not in code:
        # Mencari jangkar yang aman untuk menaruh variabel global
        anchor = 'static int jumlah_var'
        insert_idx = code.find(anchor)
        if insert_idx == -1: 
            anchor = 'int main'
            insert_idx = code.find(anchor)
            
        stack_code = "\n// === SISTEM CALL STACK (FUNGSI) ===\n#define MAX_CALL 256\nstatic long ret_stack[MAX_CALL];\nstatic int ret_sp = 0;\n\n"
        code = code.replace(anchor, stack_code + anchor)

    # 2. Menyuntikkan Opcode 94 dan 95 (Jika belum ada)
    if 'case 94:' not in code:
        opcode_code = """
        case 94: { // OP_PANGGIL_FUNGSI (CALL)
            int target_alamat = baca_int32(f);
            if(ret_sp < MAX_CALL) {
                ret_stack[ret_sp++] = ftell(f);
                fseek(f, target_alamat, SEEK_SET);
            }
            break;
        }
        case 95: { // OP_KEMBALIKAN (RETURN)
            if(ret_sp > 0) {
                fseek(f, ret_stack[--ret_sp], SEEK_SET);
            } else {
                hidup = 0; // Selesai jika stack kosong
            }
            break;
        }
"""
        # Menyisipkan tepat sebelum default: di dalam switch
        code = code.replace('default:', opcode_code + '        default:')

    # Tulis ulang file
    with open(vm_path, 'w') as f:
        f.write(code)
    print("✅ [Fase 1] Patch kode sumber ouro_vm.c berhasil diterapkan!")

    # 3. Kompilasi otomatis menggunakan GCC
    print("⚙️  [Fase 2] Menempa ulang Virtual Machine (GCC)...")
    result = subprocess.run(['gcc', 'src/vm/ouro_vm.c', '-o', 'bin/ouro_vm'])
    
    if result.returncode == 0:
        print("🎉 [SUKSES MUTLAK] Mesin VM kini memiliki memori Call Stack untuk Fungsi!")
    else:
        print("❌ [GAGAL] GCC menemukan masalah. Cek log di atas.")

except FileNotFoundError:
    print(f"❌ File {vm_path} tidak ditemukan! Pastikan Anda berada di root direktori proyek.")
