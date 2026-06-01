import os

filepath = 'src/compiler/kompilator.ouro'

with open(filepath, 'r') as f:
    kode = f.read()

# 1. Menambahkan Array Global dan Fungsi Makro
blok_modul_makro = """
# --- MODUL PREPROCESSOR: MAKRO GLOBAL ---
GLOBAL_ARRAY MAKRO_KUNCI 256
GLOBAL_ARRAY MAKRO_NILAI 256
GLOBAL JUMLAH_MAKRO 0

FUNGSI_PARAM DAFTAR_MAKRO HASH NILAI
    ARRAY_SIMPAN MAKRO_KUNCI JUMLAH_MAKRO HASH
    ARRAY_SIMPAN MAKRO_NILAI JUMLAH_MAKRO NILAI
    NAIK JUMLAH_MAKRO
BATAS_FUNGSI

FUNGSI_KEMBALI CARI_MAKRO HASH
    SIMPAN I 0
    SELAMA_KURANG I JUMLAH_MAKRO
        BACA_ARRAY KUNCI_SAAT_INI MAKRO_KUNCI I
        BILA_SAMA KUNCI_SAAT_INI HASH
            BACA_ARRAY NILAI_MAKRO MAKRO_NILAI I
            KEMBALIKAN NILAI_MAKRO
        BATAS_BILA
        NAIK I
    BATAS_SELAMA
    KEMBALIKAN -1
BATAS_FUNGSI
"""

# 2. Menambahkan Logika Pengecekan GLOBAL
blok_deteksi_global = """
            BILA_SAMA SIDIK_JARI 1912
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_KEMBALI HASH_NAMA HITUNG_SIDIK_JARI
                PANGGIL_KEMBALI ADA_KATA BACA_TOKEN FILE_IN
                PANGGIL_KEMBALI NILAI_MAKRO STRING_KE_ANGKA
                PANGGIL_PARAM DAFTAR_MAKRO HASH_NAMA NILAI_MAKRO
                LANJUTKAN
            BATAS_BILA
"""

# Injeksi ke file
if "MODUL PREPROCESSOR" not in kode:
    kode = kode.replace("FUNGSI_PARAM TULIS_BYTE", blok_modul_makro + "\nFUNGSI_PARAM TULIS_BYTE")
    kode = kode.replace("        BATAS_BILA\n    BATAS_SELAMA", blok_deteksi_global + "        BATAS_BILA\n    BATAS_SELAMA")
    
    with open(filepath, 'w') as f:
        f.write(kode)
    print("✅ [PREPROCESSOR TAHAP 1] Logika Makro (GLOBAL) berhasil ditanamkan ke kompilator.ouro!")
else:
    print("⚠️ Modul Makro sudah ada di dalam kompilator.")

