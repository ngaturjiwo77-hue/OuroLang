.global _start
.text
_start:
    // BUKA input
    mov x0, #-100
    ldr x1, =file_in
    mov x2, #0
    mov x8, #56
    svc #0
    mov x19, x0

    // BACA input
    mov x0, x19
    ldr x1, =buf_in
    mov x2, #2048
    mov x8, #63
    svc #0

    // TUTUP
    mov x0, x19
    mov x8, #57
    svc #0

    // BUKA output
    mov x0, #-100
    ldr x1, =file_out
    mov x2, #0x41
    mov x3, #0x1a4
    mov x8, #56
    svc #0
    mov x19, x0

    // TULIS header 17 byte
    mov x0, x19
    ldr x1, =header
    mov x2, #17
    mov x8, #64
    svc #0

    // TULIS OP_CETAK_TEKS (61) + "Halo Ouro!" + null
    mov x0, x19
    ldr x1, =bytecode
    mov x2, #14
    mov x8, #64
    svc #0

    // TULIS EOF
    mov x0, x19
    ldr x1, =eof
    mov x2, #1
    mov x8, #64
    svc #0

    // TUTUP
    mov x0, x19
    mov x8, #57
    svc #0

    // EXIT
    mov x0, #0
    mov x8, #93
    svc #0

.data
file_in:  .asciz "input.ouro"
file_out: .asciz "output.obf"
header:   .fill 17, 1, 0
bytecode: .byte 61, 'H','a','l','o',' ','O','u','r','o','!', 0, 2
eof:      .byte 255
buf_in:   .space 2048
