import struct

print("Merakit bytecode matematika...")
with open("output.obf", "wb") as f:
    # 1. Header (17 bytes)
    f.write(b'\x00' * 17)

    # 2. CETAK_TEKS "--- UJI MATEMATIKA ---\n"
    f.write(bytes([61])) # Opcode 61
    f.write(b"--- UJI MATEMATIKA ---\n\0")

    # 3. SIMPAN X 100
    f.write(bytes([10])) # Opcode 10
    f.write(b"X\0")
    f.write(struct.pack("<i", 100)) # Ubah 100 jadi 4-byte

    # 4. TAMBAH X 50
    f.write(bytes([11])) # Opcode 11
    f.write(b"X\0")
    f.write(struct.pack("<i", 50)) # Ubah 50 jadi 4-byte

    # 5. CETAK_TEKS "Hasil X (100 + 50) = "
    f.write(bytes([61])) # Opcode 61
    f.write(b"Hasil X (100 + 50) = \0")

    # 6. CETAK_ANGKA X
    f.write(bytes([62])) # Opcode 62
    f.write(b"X\0")

    # 7. CETAK_TEKS "\n"
    f.write(bytes([61])) # Opcode 61
    f.write(b"\n\0")

    # 8. BATAS_PROGRAM & EOF
    f.write(bytes([2, 255])) # Opcode 2 dan 255

print("[OK] output.obf berhasil dirakit!")
