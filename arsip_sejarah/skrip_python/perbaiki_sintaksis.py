# 1. PERBAIKI PYTHON BOOTSTRAPPER (file.py)
with open('ouro_bootstrap_final.py', 'r') as f: code = f.read()

# Pindahkan BAWAKAN_FILE dari grup 1-Argumen ke grup 0-Argumen
code = code.replace('"BAWAKAN_FILE", ', '')
code = code.replace('"BAWAKAN_FILE": 96, ', '')

code = code.replace('"KONVERSI_STR_KE_INT"]:', '"KONVERSI_STR_KE_INT", "BAWAKAN_FILE"]:')
code = code.replace('"KONVERSI_STR_KE_INT": 88}', '"KONVERSI_STR_KE_INT": 88, "BAWAKAN_FILE": 96}')

with open('ouro_bootstrap_final.py', 'w') as f: f.write(code)
print("✅ [PYTHON] Sinkronisasi Argumen BAWAKAN_FILE berhasil!")

# 2. PERBAIKI KOMPILATOR.OURO (Hapus argumen palsu pada TUTUP_FILE)
# Mesin C tidak menerima argumen untuk TUTUP_FILE, jadi kita bersihkan sintaksisnya.
with open('src/compiler/kompilator.ouro', 'r') as f: komp = f.read()
komp = komp.replace('TUTUP_FILE FILE_IN', 'TUTUP_FILE')
komp = komp.replace('TUTUP_FILE FILE_OUT', 'TUTUP_FILE')
with open('src/compiler/kompilator.ouro', 'w') as f: f.write(komp)
print("✅ [OURO] Sintaksis TUTUP_FILE dibersihkan!")
