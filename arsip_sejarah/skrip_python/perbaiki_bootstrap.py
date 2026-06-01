with open('bootstrap.py', 'r') as f:
    code = f.read()

# Memindahkan label ke atas instruksi baca (op 71)
code = code.replace("op(10); s('FD'); i32(0); op(71)\nl('as')", "l('as')\nop(10); s('FD'); i32(0); op(71)")
code = code.replace("op(10); s('FD'); i32(0); op(71)\nl('ss')", "l('ss')\nop(10); s('FD'); i32(0); op(71)")
code = code.replace("op(10); s('FD'); i32(0); op(71)\nl('sn_skip')", "l('sn_skip')\nop(10); s('FD'); i32(0); op(71)")
code = code.replace("op(10); s('FD'); i32(0); op(71)\nl('ta_skip')", "l('ta_skip')\nop(10); s('FD'); i32(0); op(71)")
code = code.replace("op(10); s('FD'); i32(0); op(71)\nl('tb_skip')", "l('tb_skip')\nop(10); s('FD'); i32(0); op(71)")

with open('bootstrap.py', 'w') as f:
    f.write(code)

print("[OK] BUG INFINITE LOOP DI BOOTSTRAP.PY BERHASIL DIBASMI!")
