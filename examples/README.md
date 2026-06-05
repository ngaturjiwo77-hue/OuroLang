# 📖 OuroLang Examples Guide

Folder ini berisi **30+ contoh program** untuk mempelajari OuroLang dari pemula hingga advanced.

## 🎯 Contoh Berdasarkan Tingkat Kesulitan

### ⭐ Beginner (Pemula)

| File | Deskripsi | Belajar |
|------|-----------|--------|
| `halo.ouro` | Hello World | Dasar print |
| `tes_aritmatika.ouro` | Operasi matematika | Arithmetic operations |
| `tes_logika.ouro` | Logika boolean | Boolean logic |
| `tes_loop.ouro` | Loop dasar | Loop structure |
| `array.ouro` | Array operations | Array handling |
| `test_math.ouro` | Math functions | Math library |

### ⭐⭐ Intermediate (Menengah)

| File | Deskripsi | Belajar |
|------|-----------|--------|
| `loop_test.ouro` | Advanced looping | Loop patterns |
| `kode.ouro` | Code patterns | Programming patterns |
| `lexer_test.ouro` | Lexer testing | Tokenization |
| `generator.ouro` | Data generation | Generator pattern |
| `tabel_simbol.ouro` | Symbol tables | Symbol management |
| `catatan.ouro` | Note taking app | Simple application |

### ⭐⭐⭐ Advanced (Lanjutan)

| File | Deskripsi | Belajar |
|------|-----------|--------|
| `program.ouro` | Full program | Integration |
| `self_hosted_demo.ouro` | Self-hosted example | Bootstrap concept |
| `demo_final.ouro` | Comprehensive demo | Complete application |
| `api_client.ouro` | HTTP client | Network programming |
| `api_server.ouro` | HTTP server | Server implementation |
| `api_rest.ouro` | REST API | Web services |
| `db_manager.ouro` | Database ops | Database handling |
| `password_manager.ouro` | Secure app | Security basics |
| `image_processor.ouro` | Image processing | Media handling |
| `web_scraper.ouro` | Web scraping | Data extraction |
| `ai_prediksi.ouro` | AI prediction | ML basics |

---

## 🚀 Cara Menjalankan Contoh

### Dari Command Line
```bash
# Jalankan example
./ouro run examples/halo.ouro

# Compile dan save bytecode
./ouroc examples/halo.ouro -o build/halo.obf

# Run bytecode
./bin/ouro_vm build/halo.obf
```

### Dari Shell
```bash
# Start shell
./native/ouro_shell

# Di dalam shell, ketik nama file
halo.ouro
```

---

## 📚 Pembelajaran Terstruktur

### Tahap 1: Fundamentals
```bash
./ouro run examples/halo.ouro
./ouro run examples/tes_aritmatika.ouro
./ouro run examples/tes_logika.ouro
./ouro run examples/tes_loop.ouro
```

### Tahap 2: Data Structures
```bash
./ouro run examples/array.ouro
./ouro run examples/tabel_simbol.ouro
```

### Tahap 3: Advanced Features
```bash
./ouro run examples/api_client.ouro
./ouro run examples/db_manager.ouro
./ouro run examples/ai_prediksi.ouro
```

---

## 🔍 Deskripsi Detail Setiap File

### `halo.ouro` - Hello World
Program sederhana untuk mencetak "Halo dari OuroLang".

### `tes_aritmatika.ouro` - Arithmetic Tests
Test operasi matematika dasar: tambah, kurang, kali, bagi.

### `tes_logika.ouro` - Logic Tests
Test perbandingan logika dan conditional statements.

### `tes_loop.ouro` - Loop Tests
Test berbagai jenis loop dan iterasi.

### `array.ouro` - Array Operations
Demonstrasi array creation, access, dan manipulation.

### `test_math.ouro` - Math Functions
Test fungsi matematika dari library `math.ouro`.

### `loop_test.ouro` - Advanced Looping
Contoh loop yang lebih kompleks dengan nested loops.

### `lexer_test.ouro` - Lexer Testing
Test tokenization dan lexical analysis.

### `generator.ouro` - Data Generation
Demonstrasi generator pattern untuk create data.

### `tabel_simbol.ouro` - Symbol Tables
Contoh symbol table management dan lookup.

### `api_client.ouro` - HTTP Client
Contoh menggunakan HTTP client untuk request ke API.

### `api_server.ouro` - HTTP Server
Setup basic HTTP server dengan routing.

### `api_rest.ouro` - REST API
Full REST API implementation dengan CRUD operations.

### `db_manager.ouro` - Database Management
Database connection dan query operations.

### `password_manager.ouro` - Password Manager
Secure password storage dan encryption.

### `image_processor.ouro` - Image Processing
Image manipulation dan processing.

### `web_scraper.ouro` - Web Scraping
Extract data dari website.

### `ai_prediksi.ouro` - AI Prediction
Machine learning prediction model.

### `demo_final.ouro` - Final Demo
Comprehensive demo menggabungkan semua fitur.

---

## 💡 Tips Pembelajaran

1. **Mulai dari sederhana** - Pahami `halo.ouro` terlebih dahulu
2. **Eksperimen** - Ubah nilai dan jalankan kembali
3. **Trace eksekusi** - Gunakan `debug` library untuk trace
4. **Baca source** - Pahami kode sebelum menjalankan
5. **Combine concepts** - Mix berbagai contoh jadi program baru

---

## 📝 Membuat Contoh Baru

Jika ingin membuat contoh baru:

1. Buat file `examples/nama_program.ouro`
2. Tulis program dengan prefix dokumentasi
3. Test dengan `./ouro run examples/nama_program.ouro`
4. Add deskripsi ke README ini

---

## 🔗 Resources

- **Docs**: [DOKUMENTASI_OUROLANG.md](../DOKUMENTASI_OUROLANG.md)
- **Apps**: [../apps](../apps) - Production examples
- **Lib**: [../lib](../lib) - Standard libraries
- **Main README**: [../README.md](../README.md)

---

**Happy Learning! 🎉**

*Explore examples dan discover OuroLang capabilities.*
