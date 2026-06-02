.global _start
.text
_start:
    // ==========================================
    // VM ARM64 v3.0 - RUNTIME OURO LENGKAP
    // Opcode: 61=CETAK_TEKS, 62=CETAK_ANGKA
    //         10=SIMPAN, 11=TAMBAH, 21=KURANG, 22=KALI, 23=BAGI
    //         30=SELAMA, 45=BATAS_SELAMA
    //         2=BATAS_PROGRAM, 255=EOF
    // ==========================================

    // BUKA output.obf
    mov x0, #-100
    ldr x1, =file_obf
    mov x2, #0
    mov x8, #56
    svc #0
    mov x19, x0

    // BACA
    mov x0, x19
    ldr x1, =buf
    mov x2, #4096
    mov x8, #63
    svc #0

    // TUTUP
    mov x0, x19
    mov x8, #57
    svc #0

    // Skip header 17 byte
    ldr x21, =buf
    add x21, x21, #17

    // Memori variabel: 16 slot x 8 byte
    sub sp, sp, #128

loop:
    ldrb w22, [x21]
    add x21, x21, #1

    // === OPCODE ===
    cmp w22, #61
    b.eq op_cetak_teks
    cmp w22, #62
    b.eq op_cetak_angka
    cmp w22, #10
    b.eq op_simpan
    cmp w22, #11
    b.eq op_tambah
    cmp w22, #21
    b.eq op_kurang
    cmp w22, #22
    b.eq op_kali
    cmp w22, #23
    b.eq op_bagi
    cmp w22, #2
    b.eq done
    cmp w22, #255
    b.eq done
    b loop

// ========== CETAK_TEKS ==========
op_cetak_teks:
    mov x0, #1
    mov x1, x21
    mov x2, #0
1:
    ldrb w23, [x1, x2]
    cmp w23, #0
    b.eq 2f
    add x2, x2, #1
    b 1b
2:
    mov x8, #64
    svc #0
    add x21, x21, x2
    add x21, x21, #1
    b loop

// ========== CETAK_ANGKA ==========
op_cetak_angka:
    ldrb w23, [x21]          // indeks var (1 byte)
    sub w23, w23, #65        // 'A'=0, 'B'=1, dst
    ldr w24, [sp, w23, uxtw #2]
    // Konversi ke string sederhana
    add w24, w24, #48
    strb w24, [sp, #64]
    mov x0, #1
    add x1, sp, #64
    mov x2, #1
    mov x8, #64
    svc #0
    add x21, x21, #2
    b loop

// ========== SIMPAN ==========
op_simpan:
    ldrb w23, [x21]          // indeks var
    sub w23, w23, #65
    add x21, x21, #2
    ldr w24, [x21]           // nilai 4 byte
    add x21, x21, #4
    str w24, [sp, w23, uxtw #2]
    b loop

// ========== TAMBAH ==========
op_tambah:
    ldrb w23, [x21]
    sub w23, w23, #65
    add x21, x21, #2
    ldr w24, [x21]
    add x21, x21, #4
    ldr w25, [sp, w23, uxtw #2]
    add w25, w25, w24
    str w25, [sp, w23, uxtw #2]
    b loop

// ========== KURANG ==========
op_kurang:
    ldrb w23, [x21]
    sub w23, w23, #65
    add x21, x21, #2
    ldr w24, [x21]
    add x21, x21, #4
    ldr w25, [sp, w23, uxtw #2]
    sub w25, w25, w24
    str w25, [sp, w23, uxtw #2]
    b loop

// ========== KALI ==========
op_kali:
    ldrb w23, [x21]
    sub w23, w23, #65
    add x21, x21, #2
    ldr w24, [x21]
    add x21, x21, #4
    ldr w25, [sp, w23, uxtw #2]
    mul w25, w25, w24
    str w25, [sp, w23, uxtw #2]
    b loop

// ========== BAGI ==========
op_bagi:
    ldrb w23, [x21]
    sub w23, w23, #65
    add x21, x21, #2
    ldr w24, [x21]
    add x21, x21, #4
    ldr w25, [sp, w23, uxtw #2]
    udiv w25, w25, w24
    str w25, [sp, w23, uxtw #2]
    b loop

done:
    mov x0, #0
    mov x8, #93
    svc #0

.data
file_obf: .asciz "output.obf"
buf:      .space 4096
