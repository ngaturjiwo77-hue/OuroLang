import os

filepath = 'src/compiler/kompilator.ouro'

if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        code = f.read()

    # Menyelaraskan Opcode yang salah dengan standar VM C yang benar
    code = code.replace('GLOBAL OP_CETAK_TEKS 21', 'GLOBAL OP_CETAK_TEKS 61')
    code = code.replace('GLOBAL OP_CETAK_ANGKA 22', 'GLOBAL OP_CETAK_ANGKA 62')
    code = code.replace('GLOBAL OP_BILA_SAMA 30', 'GLOBAL OP_BILA_SAMA 32')
    code = code.replace('GLOBAL OP_KURANG 12', 'GLOBAL OP_KURANG 24')
    
    with open(filepath, 'w') as f:
        f.write(code)
    print("✅ [SUKSES] Opcode di kompilator.ouro telah disinkronkan dengan VM!")
else:
    print("❌ File kompilator.ouro tidak ditemukan.")
