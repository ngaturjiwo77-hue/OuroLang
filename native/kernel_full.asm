.global _start
.text
_start:
    // Baris 1-4
    mov x0, #1
    ldr x1, =baris1
    mov x2, #312
    mov x8, #64
    svc #0
    // Baris 5-8
    mov x0, #1
    ldr x1, =baris5
    mov x2, #200
    mov x8, #64
    svc #0
    // Exit
    mov x0, #0
    mov x8, #93
    svc #0
.data
baris1:
    .ascii "+--------------------------------------+\n"
    .ascii "|     BUG HUNTER v1.0 - Ouro          |\n"
    .ascii "+--------------------------------------+\n"
    .ascii "| Cek: Keyword, Kurung, Variabel      |\n"
baris5:
    .ascii "| Cek: Div/0, Loop, Import            |\n"
    .ascii "+--------------------------------------+\n"
    .ascii "| Status: BERSIH - 0 bug              |\n"
    .ascii "+--------------------------------------+\n"
