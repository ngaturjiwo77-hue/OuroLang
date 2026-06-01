import re

with open('src/vm/ouro_vm.c', 'r') as f:
    code = f.read()

# Menyuntikkan case 75 tepat di atas OP_STRING_MULAI
patch = '''case 75:{char n[64];baca_string(f,n,sizeof(n));int s=baca_var("FD");if(s>=0&&s<file_count&&files[s])tulis_int32(files[s],baca_var(n));break;}
            case OP_STRING_MULAI:'''

if 'case 75:' not in code:
    code = code.replace('case OP_STRING_MULAI:', patch)
    with open('src/vm/ouro_vm.c', 'w') as f:
        f.write(code)
    print("[OK] BUG HANG DIPERBAIKI! Opcode 75 berhasil ditambahkan ke ouro_vm.c")
else:
    print("Opcode 75 sudah ada!")
