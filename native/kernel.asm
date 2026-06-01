.global _start
.text

_start:
    // CETAK_TEKS "O"
    mov x0, #1          // stdout
    ldr x1, =msg        // pointer teks
    mov x2, #15         // panjang
    mov x8, #64         // syscall write
    svc #0

    // Keluar
    mov x0, #0
    mov x8, #93         // syscall exit
    svc #0

.data
msg:
    .ascii "Kernel Ouro!\n"
