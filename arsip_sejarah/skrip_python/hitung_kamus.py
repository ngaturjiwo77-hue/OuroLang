# Kamus resmi berdasarkan enum di ouro_vm.c
kamus_ouro = {
    "PROGRAM_UTAMA": 1, "BATAS_PROGRAM": 2,
    "SIMPAN": 10, "TAMBAH": 11, "TAMBAH_VAR": 12,
    "KURANG": 24, "KURANG_VAR": 25,
    "KALI": 22, "KALI_VAR": 26,
    "BAGI": 23, "BAGI_VAR": 27,
    "CETAK_TEKS": 61, "CETAK_ANGKA": 62,
    "BUKA_BACA": 70, "BACA_KARAKTER": 71, "TUTUP_FILE": 72,
    "BUKA_TULIS": 73, "TULIS_BYTE": 74, "TULIS_INT32": 75,
    "STRING_MULAI": 80, "STRING_TAMBAH_VAR": 84,
    "STRING_BANDING": 83, "STRING_TULIS_BUFFER": 86,
    "KONVERSI_STR_KE_INT": 88,
    "LOMPAT_KE": 31, "BILA_SAMA": 32, "BATAS_BILA": 0, # Virtual/Logic
    "TANDA": 33, "LOMPAT_JIKA_BENAR": 34
}

def hitung_sidik_jari(token):
    total = 0
    pengali = 1
    for char in token:
        total += ord(char) * pengali
        pengali += 1
    return total

print("="*60)
print(f"{'KATA KUNCI (OUROLANG)':<22} | {'SIDIK JARI':<12} | {'OPCODE VM':<10}")
print("="*60)

for kata, opcode in kamus_ouro.items():
    sidik = hitung_sidik_jari(kata)
    print(f"{kata:<22} | {sidik:<12} | {opcode:<10}")
print("="*60)
