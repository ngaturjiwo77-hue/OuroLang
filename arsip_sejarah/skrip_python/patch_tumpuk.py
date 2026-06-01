import re
komp_path = 'src/compiler/kompilator.ouro'
with open(komp_path, 'r') as f: komp = f.read()

# Memperbaiki blok BAWAKAN yang kehilangan perintah TUMPUK
blok_benar = """BILA_SAMA SIDIK_JARI 2028
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                TUMPUK_FILE FILE_IN
                BAWAKAN_FILE
                SIMPAN FILE_IN FD
                NAIK LEVEL_FILE
                LANJUTKAN
            BATAS_BILA"""

komp = re.sub(r'BILA_SAMA SIDIK_JARI 2028.*?BATAS_BILA', blok_benar, komp, flags=re.DOTALL)
with open(komp_path, 'w') as f: f.write(komp)
print("✅ Pembatas Buku (TUMPUK_FILE) telah dikembalikan!")
