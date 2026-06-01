import os

filepath = 'src/compiler/kompilator.ouro'

def hitung_sidik_jari(token):
    return sum(ord(c) * (i + 1) for i, c in enumerate(token))

hash_panggil = hitung_sidik_jari("SUBRUTIN_PANGGIL")
hash_kembali = hitung_sidik_jari("SUBRUTIN_KEMBALI")

with open(filepath, 'r') as f:
    kode = f.read()

blok_subrutin = f"""
            BILA_SAMA SIDIK_JARI {hash_panggil}
                PANGGIL_PARAM TULIS_BYTE FILE_OUT 94
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_KEMBALI NILAI_ASLI STRING_KE_ANGKA
                PANGGIL_PARAM TULIS_ANGKA_4BYTE FILE_OUT NILAI_ASLI
                LANJUTKAN
            BATAS_BILA

            BILA_SAMA SIDIK_JARI {hash_kembali}
                PANGGIL_PARAM TULIS_BYTE FILE_OUT 95
                LANJUTKAN
            BATAS_BILA
"""

# Menyuntikkan ke dalam blok pengecekan
if f"BILA_SAMA SIDIK_JARI {hash_kembali}" not in kode:
    kode = kode.replace("        BATAS_BILA\n    BATAS_SELAMA", blok_subrutin + "        BATAS_BILA\n    BATAS_SELAMA")
    with open(filepath, 'w') as f:
        f.write(kode)
    print("✅ [Sinkronisasi Kompilator] OuroLang sekarang memahami Opcode Call & Return!")
else:
    print("⚠️ [Aman] Patch sudah pernah diterapkan.")

