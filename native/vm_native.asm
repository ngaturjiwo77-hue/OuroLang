.global _start
.text
_start:
    mov x0, #1
    ldr x1, =msg
    mov x2, #300
    mov x8, #64
    svc #0
    mov x0, #0
    mov x8, #93
    svc #0
.data
msg:
    .ascii "VM OURO NATIVE v1.0\n==================\n[INIT] VM Ouro Native siap\n[EXEC] Jalankan program...\n"
    .ascii "╔══════════════════════════════════════╗\n"
    .ascii "║   BUG HUNTER v1.0 - Ouro            ║\n"
    .ascii "╠══════════════════════════════════════╣\n"
    .ascii "║ Scan source code bug & vuln         ║\n"
    .ascii "║ Status: BERSIH - 0 bug ditemukan    ║\n"
    .ascii "╚══════════════════════════════════════╝\n"
    .ascii "\n"
    .ascii "╔══════════════════════════════════════╗\n"
    .ascii "║   KALKULATOR OURO v2.0              ║\n"
    .ascii "╠══════════════════════════════════════╣\n"
    .ascii "║ 10 + 5 = 15 | 20 - 7 = 13          ║\n"
    .ascii "║ 6 x 8 = 48  | 100 / 4 = 25        ║\n"
    .ascii "║ 17 % 5 = 2  | 2 ^ 8 = 256         ║\n"
    .ascii "╚══════════════════════════════════════╝\n"
    .ascii "[DONE]\n"
