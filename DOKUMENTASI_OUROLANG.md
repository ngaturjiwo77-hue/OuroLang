# 📜 DOKUMENTASI OUROLANG v3

> **Bahasa Pemrograman Indonesia — Turing-Complete — Dibuat dari HP Android**
> *"Dari Termux untuk dunia."*

---

## 1. PENDAHULUAN

**OuroLang** adalah bahasa pemrograman prosedural dengan sintaks Bahasa Indonesia. Dirancang untuk menjadi **self-hosted** dan **cross-platform** melalui VM portable berbasis C.

| Aspek | Detail |
|-------|--------|
| Paradigma | Prosedural, imperatif |
| Turing-complete | ✅ |
| Self-hosted | ✅ (bootstrap) |
| Dibuat dengan | HP Android + Termux |
| Platform | ARM64 Linux / Linux / macOS / Windows |
| Versi | v3 (16 opcode) |

---

## 2. PANDUAN MEMULAI

```bash
make                                          # Kompilasi VM
./bin/ouro_vm build/hasil_kompilasi.obf       # Jalankan
./ouro examples/halo.ouro                     # Pipeline penuh
```

---

## 3. DAFTAR OPCODE VM (16 opcode)

| Opcode | Mnemonic | Deskripsi |
|--------|----------|-----------|
| 10 | SIMPAN | Alokasi integer |
| 11 | TAMBAH | Penjumlahan |
| 12 | PANGKAS | Pengurangan |
| 13 | KALI | Perkalian |
| 14 | BAGI | Pembagian + error handling |
| 21 | CETAK_TEKS | Output string |
| 22 | CETAK_ANGKA | Output integer |
| 23 | CETAK_FLOAT | Output float |
| 31 | LOMPAT_KE | Lompat absolut |
| 32 | LOMPAT_JIKA_SALAH | Lompat jika var != cmp |
| 33 | TANDA | No-op, penanda posisi |
| 34 | LOMPAT_JIKA_BENAR | Lompat jika var == cmp |
| 40 | BACA_INPUT | Input dari keyboard |
| 41 | SIMPAN_FLOAT | Alokasi float |
| 60 | BATAS_PROGRAM | Exit program |
| 255 | EOF | End of bytecode |

---

## 4. PUSTAKA STANDAR (11 modul)

| Modul | Fungsi Utama |
|-------|-------------|
| core.ouro | Konstanta syscall |
| std.ouro | UI (garis, header, pesan) |
| sys.ouro | File system |
| io.ouro | Input/output karakter |
| math.ouro | Nilai mutlak, pangkat |
| string.ouro | Panjang, compare, isEmpty |
| konversi.ouro | Angka↔teks |
| acak.ouro | Random number |
| waktu.ouro | Waktu, tunda |
| array.ouro | Array dinamis |
| bin_writer.ouro | Tulis byte mentah |

---

## 5. STATUS PENGEMBANGAN

**✅ SELESAI:**
- VM C (16 opcode) + VM Ouro murni
- Lexer, Parser, Assembler
- Integer, Float, Input user
- Loop, If-Else
- Error handling (pembagian nol)
- 11 Pustaka standar
- Turing-complete
- Bootstrap self-hosted
- Cross-platform

**🔜 MENDATANG:**
- Array multi-dimensi
- Garbage collection
- Debugger
- Compiler self-hosted penuh
- WebAssembly target

---

> *"Bahasa ini lahir bukan di server room, bukan di laptop mahal, tapi di genggaman tangan, di layar 6 inci, di terminal Termux. OuroLang adalah bukti bahwa kreativitas tidak terbatas perangkat."*

**© 2025 OuroLang Project — Dibuat dari HP Android + Termux**
