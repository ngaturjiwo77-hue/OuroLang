# 🚀 OuroLang - Bahasa Pemrograman Indonesia

[![CI](https://github.com/ngaturjiwo77-hue/OuroLang/actions/workflows/ouro.yml/badge.svg)](https://github.com/ngaturjiwo77-hue/OuroLang/actions)

**OuroLang** adalah bahasa pemrograman dengan sintaks 100% Bahasa Indonesia. **Self-hosted**, **native ARM64**, **Turing-complete**, dan dikembangkan sepenuhnya dari **HP Android + Termux**.

> *"Dari Termux untuk dunia."* — Bahasa ini lahir dari genggaman tangan, di layar 6 inci, bukan di server room mahal.

---

## ✨ Keunggulan

| Fitur | Status |
|-------|--------|
| 100% Bahasa Indonesia | ✅ |
| Self-Hosted (Bootstrap) | ✅ |
| ARM64 Native | ✅ |
| Turing-Complete | ✅ |
| 100+ Pustaka | ✅ |
| OURO SHELL v3.0 | ✅ |
| Cross-Platform (Linux/macOS/Windows) | ✅ |
| CI/CD Ready | ✅ |

---

## 📦 Komponen Utama

### Versi Terkini
- **Compiler**: v18.0
- **VM**: v24.0 (portable C-based)
- **VM ARM64**: v3.0 (native)
- **Total Pustaka**: 100+ modul

### Struktur Direktori

```
OuroLang/
├── lib/                        # 100+ pustaka standar
│   ├── core.ouro              # Konstanta & core functions
│   ├── std.ouro               # UI primitif
│   ├── sys.ouro               # File system operations
│   ├── io.ouro                # Input/Output
│   ├── math.ouro              # Mathematical functions
│   ├── string.ouro            # String manipulation
│   ├── json.ouro              # JSON parsing/generation
│   ├── http.ouro              # HTTP client/server
│   ├── database.ouro          # Database operations
│   ├── kripto.ouro            # Cryptography
│   ├── neural.ouro            # Neural network basics
│   ├── tensor.ouro            # Tensor operations
│   └── [90+ modul lainnya]
├── native/                    # Native ARM64 implementation
│   ├── kernel_compiler        # Compiler binary (ARM64)
│   ├── kernel_compiler.asm    # ARM64 Assembly
│   ├── vm_arm64               # VM binary (ARM64)
│   ├── vm_arm64.asm          # VM ARM64 Assembly
│   ├── ouro_shell            # Interactive shell (ARM64)
│   └── ouro_shell.asm        # Shell ARM64 Assembly
├── src/                       # Source code (Ouro)
│   ├── compiler/             # Compiler implementation
│   ├── interpreter/          # Interpreter
│   ├── vm/                   # Virtual machine
│   └── compiler_baru.ouro    # New compiler (WIP)
├── apps/                      # Example applications
│   ├── halo.ouro             # Hello World
│   ├── kalkulator.ouro       # Basic calculator
│   ├── kalkulator_ui.ouro    # Calculator with UI
│   ├── jadwal.ouro           # Scheduler app
│   ├── bug_hunter.ouro       # Code bug scanner
│   └── bug_hunter_html.ouro  # Bug hunter with HTML output
├── bin/                       # Compiled binaries
├── stable/                    # Stable releases
├── tests/                     # Test suite
├── examples/                  # Additional examples
├── Makefile                   # Build configuration
├── ouro                      # Main runtime dispatcher
├── ouro_run                  # Compile & run wrapper
├── ouroc                     # Compiler script
├── ouroi                     # Interpreter script
└── program.ouro             # Default program file
```

---

## 🎯 Quick Start

### Kebutuhan Sistem
- **Linux/macOS/Windows** (dengan Termux untuk Android)
- **GCC** untuk compile VM
- **bash** untuk runtime scripts

### Instalasi & Jalankan

```bash
# Clone repository
git clone https://github.com/ngaturjiwo77-hue/OuroLang.git
cd OuroLang

# (Opsional) Compile VM dari C source
make vm

# Jalankan interactive shell
./native/ouro_shell

# Atau jalankan program langsung
./ouro run apps/halo.ouro
```

---

## 📝 Contoh Program

### Hello World
```ouro
CETAK_TEKS "╔══════════════════════════════════════╗"
CETAK_TEKS "║   HALO DARI OURO!                   ║"
CETAK_TEKS "║   Aplikasi Ouro Mandiri             ║"
CETAK_TEKS "╚══════════════════════════════════════╝"
BATAS_PROGRAM
```

### Kalkulator Sederhana
```ouro
CETAK_TEKS "╔══════════════════════════════════════╗"
CETAK_TEKS "║        KALKULATOR OURO               ║"
CETAK_TEKS "╠══════════════════════════════════════╣"
CETAK_TEKS "║ 10 + 20 = 30                         ║"
CETAK_TEKS "║ 50 - 15 = 35                         ║"
CETAK_TEKS "║ 8 x 7 = 56                           ║"
CETAK_TEKS "╚══════════════════════════════════════╝"
BATAS_PROGRAM
```

### Dengan Variable & Logic
```ouro
PROGRAM_UTAMA
    SIMPAN X 100
    TAMBAH X 50
    CETAK_ANGKA X
    
    CETAK_TEKS "X bernilai: "
    CETAK_ANGKA X
    
    BAGI X 10
    CETAK_TEKS "Hasil pembagian:"
    CETAK_ANGKA X
BATAS_PROGRAM
```

---

## 🔧 Instruksi & Opcode

OuroLang menggunakan **16 opcode** untuk eksekusi virtual machine:

| Opcode | Perintah | Fungsi |
|--------|----------|--------|
| 10 | SIMPAN | Alokasi integer variable |
| 11 | TAMBAH | Penjumlahan |
| 12 | PANGKAS | Pengurangan |
| 13 | KALI | Perkalian |
| 14 | BAGI | Pembagian (dengan zero-check) |
| 21 | CETAK_TEKS | Output string |
| 22 | CETAK_ANGKA | Output integer |
| 23 | CETAK_FLOAT | Output floating-point |
| 31 | LOMPAT_KE | Jump absolut ke address |
| 32 | LOMPAT_JIKA_SALAH | Conditional jump (!=) |
| 33 | TANDA | Marker/label |
| 34 | LOMPAT_JIKA_BENAR | Conditional jump (==) |
| 40 | BACA_INPUT | Read keyboard input |
| 41 | SIMPAN_FLOAT | Alokasi float variable |
| 60 | BATAS_PROGRAM | Exit program |
| 255 | EOF | End of bytecode |

---

## 📚 Pustaka Standar (100+)

OuroLang dilengkapi dengan **lebih dari 100 pustaka** untuk berbagai kebutuhan:

### Core & I/O
- `core.ouro` - Konstanta & syscall definitions
- `std.ouro` - UI primitif (garis, header, pesan)
- `io.ouro` - Character-level I/O
- `masukan.ouro` - Input handling

### Data Structures
- `array.ouro` - Dynamic arrays
- `daftar.ouro` - List implementation
- `larik.ouro` - Array utilities
- `struktur_data.ouro` - Data structure helpers
- `regex.ouro` - Regular expressions

### Utilities
- `math.ouro` - Mathematical functions
- `string.ouro` - String manipulation
- `konversi.ouro` - Type conversion
- `acak.ouro` - Random number generation
- `waktu.ouro` - Time & delay functions
- `log.ouro` - Logging utilities

### Advanced
- `json.ouro` - JSON parsing/generation
- `http.ouro` - HTTP client & server
- `http_client.ouro` - HTTP client wrapper
- `web_server.ouro` - Web server implementation
- `jaringan.ouro` - Network utilities
- `database.ouro` - Database operations
- `database_sql.ouro` - SQL support
- `database_nosql.ouro` - NoSQL support

### Security & Crypto
- `kripto.ouro` - Cryptographic functions
- `jwt.ouro` - JWT token handling
- `ssl.ouro` - SSL/TLS support

### Machine Learning
- `neural.ouro` - Neural network basics
- `tensor.ouro` - Tensor operations
- `pikiran.ouro` - AI/ML utilities

### System & OS
- `sys.ouro` - File system operations
- `os.ouro` - Operating system interface
- `kernel.ouro` - Kernel operations
- `path.ouro` - Path manipulation

### Development Tools
- `debug.ouro` - Debugging utilities
- `debugger.ouro` - Interactive debugger
- `test.ouro` - Testing framework
- `testing.ouro` - Test utilities
- `kompiler.ouro` - Compiler utilities
- `vm.ouro` - VM operations
- `assembler_arm64.ouro` - ARM64 assembly support

### Encoding & Compression
- `kompresi.ouro` - Compression algorithms
- `csv.ouro` - CSV parsing
- `xml.ouro` - XML parsing
- `yaml.ouro` - YAML parsing

### Graphics & Media
- `grafik.ouro` - Graphics primitives
- `visi.ouro` - Computer vision basics
- `image.ouro` - Image processing
- `audio.ouro` - Audio handling
- `video.ouro` - Video support

### Advanced Computing
- `solver_3sat.ouro` - 3SAT problem solver
- `algoritma.ouro` - Algorithm implementations
- `logika.ouro` - Logic programming
- `assembly.ouro` - Assembly language support

### Tools & Utilities
- `cli.ouro` - CLI utilities
- `konfig.ouro` - Configuration handling
- `cache.ouro` - Caching layer
- `process.ouro` - Process management
- `queue.ouro` - Queue data structure
- `sort.ouro` - Sorting algorithms
- `search.ouro` - Search algorithms
- `deepseek.ouro` - Deep learning integration

Dan masih banyak lagi! Lihat folder `/lib` untuk daftar lengkap.

---

## 🛠️ Build & Compile

### Compile VM dari Source C
```bash
make vm                    # Compile VM portable
make run-vm               # Run VM dengan bytecode
make bersih               # Clean build artifacts
make help                 # Show help menu
```

### Pipeline Eksekusi Lengkap
```bash
# Step 1: Compile Ouro ke bytecode
./ouroc apps/halo.ouro -o build/hasil_kompilasi.obf

# Step 2: Jalankan bytecode di VM
./bin/ouro_vm build/hasil_kompilasi.obf

# Step 3: Atau gunakan wrapper
./ouro run apps/halo.ouro
```

### Runtime Scripts

| Script | Fungsi |
|--------|--------|
| `./ouro compile <file>` | Compile ke bytecode |
| `./ouro run <file>` | Compile & execute |
| `./ouro vm <bytecode>` | Run bytecode di VM |
| `./ouro_run [file]` | Full pipeline wrapper |
| `./native/ouro_shell` | Interactive shell (ARM64 native) |

---

## 📱 Aplikasi Contoh

### Tersedia di `/apps`
1. **halo.ouro** - Program Hello World sederhana
2. **kalkulator.ouro** - Kalkulator operasi dasar
3. **kalkulator_ui.ouro** - Kalkulator dengan UI enhancement
4. **jadwal.ouro** - Scheduler/planner application
5. **bug_hunter.ouro** - Source code bug scanner
6. **bug_hunter_html.ouro** - Bug hunter dengan output HTML

Jalankan dengan:
```bash
./ouro run apps/halo.ouro
./ouro run apps/kalkulator.ouro
./ouro run apps/bug_hunter.ouro
```

---

## 🧪 Testing

Folder `/tests` untuk test suite (sedang dikembangkan):
```bash
# Run all tests
make test

# Run specific test
./bin/ouro_vm tests/test_arithmetic.obf
```

---

## 📖 Dokumentasi Lanjutan

- **[DOKUMENTASI_OUROLANG.md](DOKUMENTASI_OUROLANG.md)** - Panduan lengkap syntax & opcode
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Panduan kontribusi
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - Code of conduct
- **Folder `/examples`** - Contoh program lengkap (coming soon)

---

## 🌍 Platform Support

| Platform | Status | Note |
|----------|--------|------|
| **Linux ARM64** | ✅ Tested | Native performance |
| **Linux x86_64** | ✅ Supported | Via C VM |
| **macOS (ARM64)** | ✅ Supported | Via C VM |
| **macOS (Intel)** | ✅ Supported | Via C VM |
| **Windows (MinGW)** | ✅ Supported | Via C VM |
| **Android (Termux)** | ✅ Tested | Full support |

---

## 🤝 Kontribusi

Kami menerima kontribusi dari komunitas! Silakan lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk panduan.

### Cara Berkontribusi:
1. Fork repository
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📋 Status Pengembangan

### ✅ Selesai
- [x] VM C (16 opcode)
- [x] Lexer, Parser, Assembler
- [x] Integer & Float support
- [x] Conditional jumps & loops
- [x] Error handling (division by zero)
- [x] 100+ Standard libraries
- [x] Turing-complete
- [x] Self-hosted bootstrap
- [x] ARM64 native compilation
- [x] OURO SHELL v3.0
- [x] CI/CD pipeline

### 🔜 Mendatang
- [ ] Array multi-dimensi
- [ ] Garbage collection
- [ ] Advanced debugger
- [ ] Full self-hosted compiler
- [ ] WebAssembly target
- [ ] Package manager
- [ ] Standard library docs

---

## 📄 Lisensi

OuroLang dilisensikan di bawah **MIT License**. Lihat file [LICENSE](LICENSE) untuk detail.

---

## 🙏 Kredit

**Dibuat dari HP Android + Termux** oleh komunitas OuroLang.

> *"Bahasa ini lahir bukan di server room, bukan di laptop mahal, tapi di genggaman tangan, di layar 6 inci, di terminal Termux. OuroLang adalah bukti bahwa kreativitas tidak terbatas perangkat."*

---

## 📞 Kontak & Support

- **Issues**: [GitHub Issues](https://github.com/ngaturjiwo77-hue/OuroLang/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ngaturjiwo77-hue/OuroLang/discussions)
- **Author**: [@ngaturjiwo77-hue](https://github.com/ngaturjiwo77-hue)

---

**Happy Coding! 🎉**

*OuroLang - Bahasa Pemrograman Indonesia untuk semua.*
