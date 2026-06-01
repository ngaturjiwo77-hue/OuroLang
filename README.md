[![CI](https://github.com/ngaturjiwo77-hue/ourolang/actions/workflows/ouro.yml/badge.svg)]

# OUROLANG - Bahasa Pemrograman Indonesia Mandiri

> Self-hosted programming language in Bahasa Indonesia

## 🌍 Universal Portable VM

VM Ouro tersedia dalam C murni, bisa dikompilasi di Linux, macOS, dan Windows.

| OS | Compiler | Command |
|----|----------|----------|
| Linux | gcc/clang | make |
| macOS | gcc/clang | make |
| Windows | MinGW | gcc -o ouro_vm.exe src/vm/ouro_vm_portable.c |

## 📁 Struktur Proyek

```
ourolang_project/
├── bin/                    # Executables
│   ├── ouro_vm             # VM Portable (C)
│   ├── ouro_compiler       # Compiler asli ARM64
│   └── ...
├── src/
│   ├── compiler/           # Lexer, Parser, Assembler (.ouro)
│   │   ├── lexer.ouro
│   │   ├── parser.ouro
│   │   ├── assembler.ouro
│   │   └── kompilator.ouro
│   └── vm/
│       ├── ouro_vm_portable.c  # VM Universal (C)
│       ├── mesin_virtual.ouro  # VM Murni Ouro
│       └── mesin_virtual_v1.ouro
├── lib/                    # Pustaka standar
│   ├── core.ouro
│   ├── std.ouro
│   ├── sys.ouro
│   ├── io.ouro
│   ├── math.ouro
│   └── bin_writer.ouro
├── examples/               # Program contoh
│   ├── halo.ouro
│   ├── array.ouro
│   └── ...
├── build/                  # Hasil kompilasi
├── Makefile
└── ouro                    # Entry script
```

## 🚀 Cepat Mulai

```bash
# Kompilasi VM
make

# Jalankan program
./bin/ouro_vm build/hasil_kompilasi.obf

# Atau pakai script utama
./ouro examples/halo.ouro
```

## 📝 Contoh Program

```ouro
PROGRAM_UTAMA
    CETAK_TEKS "Halo Dari OuroLang!\n"
    SIMPAN X 100
    TAMBAH X 50
    CETAK_TEKS "Nilai X: "
    CETAK_ANGKA X
BATAS_PROGRAM
```

Output:
```
Halo Dari OuroLang!
Nilai X: 150
```

## 🔧 Opcode VM

| Opcode | Instruksi | Keterangan |
|--------|-----------|------------|
| 10 | SIMPAN | Alokasi variabel |
| 11 | TAMBAH | Penjumlahan |
| 12 | PANGKAS | Pengurangan |
| 13 | KALI | Perkalian |
| 21 | CETAK_TEKS | Output string |
| 22 | CETAK_ANGKA | Output angka |
| 30 | ANALISIS_JEJAK | Branching/kondisi |
| 60 | BATAS_PROGRAM | Exit program |
| 255 | EOF | End of file |

## 🛠 Pipeline

```
Source.ouro -> Lexer -> Parser -> Assembler -> Bytecode .obf -> VM Portable -> Output
```

## 📦 Dependensi

- GCC atau Clang (untuk kompilasi VM C)
- Make (opsional)
- Tidak ada dependensi runtime selain C standard library

## 🎯 Roadmap

- [x] VM Portable dalam C
- [x] Lexer Ouro
- [x] Assembler Ouro
- [x] Pustaka standar
- [ ] Parser lengkap
- [ ] Compiler self-hosted penuh
- [ ] Windows batch script
- [ ] macOS support

## 📜 Lisensi

Eksperimental - Untuk pembelajaran
