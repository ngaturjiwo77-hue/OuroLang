import os

filepath = 'src/compiler/kompilator.ouro'

with open(filepath, 'r') as f:
    kode = f.read()

# Blok instruksi array baru
blok_array = """
            BILA_SAMA SIDIK_JARI 6031
                PANGGIL_PARAM TULIS_BYTE FILE_OUT 90
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_PARAM TULIS_BUFFER_KODE FILE_OUT
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_KEMBALI NILAI_ASLI STRING_KE_ANGKA
                PANGGIL_PARAM TULIS_ANGKA_4BYTE FILE_OUT NILAI_ASLI
                LANJUTKAN
            BATAS_BILA

            BILA_SAMA SIDIK_JARI 4227
                PANGGIL_PARAM TULIS_BYTE FILE_OUT 93
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_PARAM TULIS_BUFFER_KODE FILE_OUT
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_PARAM TULIS_BUFFER_KODE FILE_OUT
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_PARAM TULIS_BUFFER_KODE FILE_OUT
                LANJUTKAN
            BATAS_BILA

            BILA_SAMA SIDIK_JARI 6059
                PANGGIL_PARAM TULIS_BYTE FILE_OUT 91
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_PARAM TULIS_BUFFER_KODE FILE_OUT
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_PARAM TULIS_BUFFER_KODE FILE_OUT
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_PARAM TULIS_BUFFER_KODE FILE_OUT
                LANJUTKAN
            BATAS_BILA
"""

# Menyuntikkan sebelum BATAS_SELAMA
kode = kode.replace("        BATAS_BILA\n    BATAS_SELAMA", blok_array + "        BATAS_BILA\n    BATAS_SELAMA")

with open(filepath, 'w') as f:
    f.write(kode)

print("✅ [PATCH SUKSES] Logika Array telah ditanamkan ke kompilator.ouro")
