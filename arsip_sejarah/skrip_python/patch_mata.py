komp_path = 'src/compiler/kompilator.ouro'
with open(komp_path, 'r') as f: komp = f.read()

anchor = 'CETAK_TEKS "=== KOMPILATOR BINER V4 (BEBAS HANG) ===\\n"\n'
if 'BUKA_BACA' not in komp.split(anchor)[-1][:50]:
    komp = komp.replace(anchor, anchor + '    BUKA_BACA "input.ouro" FILE_IN\n    BUKA_FILE "output.obf" FILE_OUT\n')

komp = komp.replace('BUKA_TULIS "output.obf"', 'BUKA_FILE "output.obf"')

with open(komp_path, 'w') as f: f.write(komp)
print("✅ Mata Kompilator telah dikembalikan!")
