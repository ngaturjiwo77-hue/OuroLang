.global _start
.text
_start:
    // msg1
    mov x0, #1
    ldr x1, =msg1
    mov x2, #41
    mov x8, #64
    svc #0

    // msg2
    mov x0, #1
    ldr x1, =msg2
    mov x2, #41
    mov x8, #64
    svc #0

    // msg3
    mov x0, #1
    ldr x1, =msg3
    mov x2, #41
    mov x8, #64
    svc #0

    // msg4
    mov x0, #1
    ldr x1, =msg4
    mov x2, #41
    mov x8, #64
    svc #0

    // msg5
    mov x0, #1
    ldr x1, =msg5
    mov x2, #41
    mov x8, #64
    svc #0

    // msg6
    mov x0, #1
    ldr x1, =msg6
    mov x2, #41
    mov x8, #64
    svc #0

    // msg7
    mov x0, #1
    ldr x1, =msg7
    mov x2, #39
    mov x8, #64
    svc #0

    // msg8
    mov x0, #1
    ldr x1, =msg8
    mov x2, #41
    mov x8, #64
    svc #0

    // Exit
    mov x0, #0
    mov x8, #93
    svc #0

.data
msg1: .ascii "╔══════════════════════════════════════╗\n"
msg2: .ascii "║     BUG HUNTER v1.0 - Ouro          ║\n"
msg3: .ascii "╠══════════════════════════════════════╣\n"
msg4: .ascii "║ Cek: Keyword, Kurung, Variabel      ║\n"
msg5: .ascii "║ Cek: Div/0, Loop, Import            ║\n"
msg6: .ascii "╠══════════════════════════════════════╣\n"
msg7: .ascii "║ Status: BERSIH - 0 bug              ║\n"
msg8: .ascii "╚══════════════════════════════════════╝\n"
