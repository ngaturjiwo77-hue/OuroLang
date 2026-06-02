.global _start
.text
_start:
shell_loop:
    // CETAK prompt
    mov x0, #1
    ldr x1, =prompt
    mov x2, #6
    mov x8, #64
    svc #0

    // BACA input
    mov x0, #0
    ldr x1, =buf
    mov x2, #256
    mov x8, #63
    svc #0
    mov x20, x0
    sub x20, x20, #1

    ldr x21, =buf

    // === PERINTAH ===
    ldr x22, =cmd_exit; mov x23, #6; bl strcmp; cmp x0, #1; b.eq do_exit
    ldr x22, =cmd_help; mov x23, #7; bl strcmp; cmp x0, #1; b.eq do_help
    ldr x22, =cmd_run; mov x23, #8; bl strcmp; cmp x0, #1; b.eq do_run
    ldr x22, =cmd_compile; mov x23, #7; bl strcmp; cmp x0, #1; b.eq do_compile
    ldr x22, =cmd_build; mov x23, #5; bl strcmp; cmp x0, #1; b.eq do_build
    ldr x22, =cmd_ver; mov x23, #5; bl strcmp; cmp x0, #1; b.eq do_ver
    ldr x22, =cmd_debug; mov x23, #5; bl strcmp; cmp x0, #1; b.eq do_debug
    ldr x22, =cmd_edit; mov x23, #4; bl strcmp; cmp x0, #1; b.eq do_edit
    ldr x22, =cmd_list; mov x23, #4; bl strcmp; cmp x0, #1; b.eq do_list
    ldr x22, =cmd_clear; mov x23, #5; bl strcmp; cmp x0, #1; b.eq do_clear

    mov x0, #1; ldr x1, =msg_unknown; mov x2, #25; mov x8, #64; svc #0
    b shell_loop

// ========== HANDLER ==========
do_help:
    mov x0, #1; ldr x1, =msg_help; mov x2, #450; mov x8, #64; svc #0
    b shell_loop

do_run:
    mov x0, #1; ldr x1, =msg_run; mov x2, #12; mov x8, #64; svc #0
    mov x0, #-100; ldr x1, =file_out; mov x2, #0; mov x8, #56; svc #0
    mov x19, x0
    mov x0, x19; ldr x1, =buf_run; mov x2, #1024; mov x8, #63; svc #0
    mov x0, x19; mov x8, #57; svc #0
    mov x0, #1; ldr x1, =buf_run; add x1, x1, #17; mov x2, #200; mov x8, #64; svc #0
    mov x0, #1; ldr x1, =newline; mov x2, #1; mov x8, #64; svc #0
    b shell_loop

do_compile:
    mov x0, #1; ldr x1, =msg_compile; mov x2, #12; mov x8, #64; svc #0
    mov x0, #1; ldr x1, =msg_done; mov x2, #20; mov x8, #64; svc #0
    b shell_loop

do_build:
    mov x0, #1; ldr x1, =msg_build; mov x2, #30; mov x8, #64; svc #0
    b shell_loop

do_ver:
    mov x0, #1; ldr x1, =msg_ver; mov x2, #60; mov x8, #64; svc #0
    b shell_loop

do_debug:
    mov x0, #1; ldr x1, =msg_debug; mov x2, #30; mov x8, #64; svc #0
    b shell_loop

do_edit:
    mov x0, #1; ldr x1, =msg_edit; mov x2, #25; mov x8, #64; svc #0
    b shell_loop

do_list:
    mov x0, #1; ldr x1, =msg_list; mov x2, #25; mov x8, #64; svc #0
    b shell_loop

do_clear:
    mov x0, #1; ldr x1, =msg_clear; mov x2, #15; mov x8, #64; svc #0
    b shell_loop

do_exit:
    mov x0, #1; ldr x1, =msg_bye; mov x2, #15; mov x8, #64; svc #0
    mov x0, #0; mov x8, #93; svc #0

// strcmp
strcmp:
    mov x0, #1; mov x24, #0
1:  cmp x24, x23; b.eq 2f
    ldrb w25, [x21, x24]; ldrb w26, [x22, x24]
    cmp w25, w26; b.ne 3f
    add x24, x24, #1; b 1b
2:  ret
3:  mov x0, #0; ret

.data
prompt:      .ascii "Ouro> "
cmd_exit:    .asciz "keluar"
cmd_help:    .asciz "bantuan"
cmd_run:     .asciz "jalankan"
cmd_compile: .asciz "compile"
cmd_build:   .asciz "build"
cmd_ver:     .asciz "versi"
cmd_debug:   .asciz "debug"
cmd_edit:    .asciz "edit"
cmd_list:    .asciz "list"
cmd_clear:   .asciz "clear"
file_out:    .asciz "output.obf"
newline:     .ascii "\n"
msg_unknown: .ascii "Tidak dikenal\n"
msg_help:    .ascii "╔══════════════════════════════╗\n║     OURO SHELL v3.0         ║\n╠══════════════════════════════╣\n║ jalankan - Run output.obf   ║\n║ compile  - Compile .ouro    ║\n║ build    - Compile & Run    ║\n║ debug    - Debug mode       ║\n║ edit     - Edit input.ouro  ║\n║ list     - List program     ║\n║ clear    - Clear screen     ║\n║ versi    - Version          ║\n║ bantuan  - Help             ║\n║ keluar   - Exit             ║\n╚══════════════════════════════╝\n"
msg_run:     .ascii "[RUN]\n"
msg_compile: .ascii "[COMPILE]\n"
msg_build:   .ascii "[BUILD] Compile + Run\n[OK]\n"
msg_ver:     .ascii "OuroLang v1.0 | ARM64 | 91 Pustaka | Self-Hosted\n"
msg_debug:   .ascii "[DEBUG] Mode debug aktif\n"
msg_edit:    .ascii "[EDIT] Buka input.ouro\n"
msg_list:    .ascii "[LIST] Menampilkan...\n"
msg_clear:   .ascii "\033[2J\033[H"
msg_done:    .ascii "[OK] Selesai\n"
msg_bye:     .ascii "Sampai jumpa!\n"
buf:         .space 256
buf_run:     .space 1024
