import os
import re

print("="*70)
print("🔍 AUDIT KESENJANGAN OPCODE OUROLANG")
print("="*70)

def get_c_defines(filepath):
    res = {}
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            # Mencari pola: #define OP_NAMA 123
            for match in re.finditer(r'#define\s+(OP_[A-Z0-9_]+)\s+(\d+)', f.read()):
                res[match.group(1)] = match.group(2)
    return res

def get_ouro_globals(filepath):
    res = {}
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            # Mencari pola: GLOBAL OP_NAMA 123
            for match in re.finditer(r'GLOBAL\s+(OP_[A-Z0-9_]+)\s+(\d+)', f.read()):
                res[match.group(1)] = match.group(2)
    return res

vm_ops = get_c_defines('src/vm/ouro_vm.c')
comp_ops = get_ouro_globals('src/compiler/kompilator.ouro')

all_ops = sorted(set(vm_ops.keys()) | set(comp_ops.keys()))

print(f"{'NAMA OPCODE':<28} | {'VM (C)':<8} | {'KOMPILATOR':<10} | {'STATUS'}")
print("-" * 70)

kesenjangan_ditemukan = False

for op in all_ops:
    vm = vm_ops.get(op, "---")
    co = comp_ops.get(op, "---")
    
    if vm == co:
        status = "✅ SINKRON"
    elif vm == "---" or co == "---":
        status = "⚠️ TIDAK LENGKAP"
        kesenjangan_ditemukan = True
    else:
        status = "❌ BENTROK!"
        kesenjangan_ditemukan = True
        
    print(f"{op:<28} | {vm:<8} | {co:<10} | {status}")

print("-" * 70)
if kesenjangan_ditemukan:
    print("⚠️ KESIMPULAN: Ada kesenjangan (bentrok/hilang) yang harus disamakan!")
else:
    print("✅ KESIMPULAN: Semua opcode sudah 100% tersinkronisasi!")
