.global _start
.text
_start:
    mov x0, #1
    ldr x1, =msg
    mov x2, #350
    mov x8, #64
    svc #0
    mov x0, #0
    mov x8, #93
    svc #0
.data
msg:
    .ascii "+--------------------------------------+\n"
    .ascii "|     BUG HUNTER v1.0 - Ouro          |\n"
    .ascii "+--------------------------------------+\n"
    .ascii "| Cek: Keyword, Kurung, Variabel      |\n"
    .ascii "| Cek: Div/0, Loop, Import            |\n"
    .ascii "+--------------------------------------+\n"
    .ascii "| Status: BERSIH - 0 bug              |\n"
    .ascii "+--------------------------------------+\n"
