.global _start
.text
_start:
    mov x0, #1
    ldr x1, =msg
    mov x2, #400
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
    .ascii "\n"
    .ascii "+--------------------------------------+\n"
    .ascii "|   KALKULATOR OURO v2.0              |\n"
    .ascii "+--------------------------------------+\n"
    .ascii "| 10+5=15 | 20-7=13                   |\n"
    .ascii "| 6x8=48  | 100/4=25                 |\n"
    .ascii "+--------------------------------------+\n"
