import struct

print("Merakit bytecode uji logika IF...")
with open("output.obf", "wb") as f:
    # 1. Header (17 bytes)
    f.write(b'\x00' * 17)

    # 2. SIMPAN X 5 (Opcode 10)
    f.write(bytes([10]))
    f.write(b"X\0")
    f.write(struct.pack("<i", 5))

    # 3. BILA_SAMA X 5 (Opcode 32 = LOMPAT_JIKA_SALAH)
    # Jika X != 5, lompat sejauh 47 byte (melewati blok cetak)
    f.write(bytes([32]))
    f.write(b"X\0")
    f.write(struct.pack("<i", 5))
    f.write(struct.pack("<i", 67)) # Target lompatan (byte ke-67)

    # 4. CETAK_TEKS "Logika IF Berhasil! X adalah 5\n" (Opcode 61)
    f.write(bytes([61]))
    f.write(b"Logika IF Berhasil! X adalah 5\n\0")

    # 5. BATAS_PROGRAM & EOF (Byte ke-67)
    f.write(bytes([2, 255]))

print("[OK] output.obf untuk IF dirakit!")
