import struct
f = open('build/ouroc.obf', 'wb')
f.write(b'\x00' * 17)
pos = 17
L = {}
P = []

def op(b):
    global pos; f.write(bytes([b])); pos += 1
def i32(v):
    global pos; f.write(struct.pack('<i', v)); pos += 4
def s(t):
    global pos; f.write(t.encode()); f.write(b'\x00'); pos += len(t) + 1
def l(n): L[n] = pos
def j(l): op(31); p=pos; i32(0); P.append((p,l))
def jn(v,c,l): op(32); s(v); i32(c); p=pos; i32(0); P.append((p,l))
def jy(v,c,l): op(34); s(v); i32(c); p=pos; i32(0); P.append((p,l))

op(61); s('OUROC v1.0\n')
op(70); s('input.ouro'); op(73); s('output.obf')

op(10); s('I'); i32(0)
l('hdr')
op(10); s('FD'); i32(1); op(74); i32(0)
op(11); s('I'); i32(1); jn('I',17,'hdr')

l('loop')
op(10); s('FD'); i32(0); op(71)
jy('KAR',-1,'finish'); jy('KAR',32,'loop'); jy('KAR',10,'loop'); jy('KAR',13,'loop')

op(80)
l('kumpul')
op(84); s('KAR'); op(71)
jy('KAR',-1,'deteksi'); jy('KAR',32,'deteksi'); jy('KAR',10,'deteksi'); jy('KAR',13,'deteksi')
j('kumpul')

l('deteksi')
op(83); s('CETAK_TEKS'); jy('CMP_RESULT',1,'do_cetak')
op(83); s('CETAK_ANGKA'); jy('CMP_RESULT',1,'do_angka')
op(83); s('SIMPAN'); jy('CMP_RESULT',1,'do_simpan')
op(83); s('TAMBAH_VAR'); jy('CMP_RESULT',1,'do_tambah_var')
op(83); s('TAMBAH'); jy('CMP_RESULT',1,'do_tambah')
op(83); s('BATAS_PROGRAM'); jy('CMP_RESULT',1,'do_batas')
op(83); s('PROGRAM_UTAMA'); jy('CMP_RESULT',1,'loop')
j('loop')

# CETAK_TEKS
l('do_cetak')
op(10); s('FD'); i32(1); op(74); i32(61)
l('cs')
op(10); s('FD'); i32(0); op(71)
jy('KAR',-1,'tn'); jy('KAR',32,'cs'); jy('KAR',10,'cs')
jy('KAR',34,'sq')
op(80)
l('sp')
op(84); s('KAR'); op(71)
jy('KAR',-1,'tb'); jy('KAR',32,'tb'); jy('KAR',10,'tb')
j('sp')
l('sq')
op(80)
l('sql')
op(10); s('FD'); i32(0); op(71)
jy('KAR',-1,'tb'); jy('KAR',34,'tb')
op(84); s('KAR'); j('sql')
l('tb')
op(10); s('FD'); i32(1); op(86); j('loop')
l('tn')
op(10); s('FD'); i32(1); op(74); i32(0); j('loop')

# CETAK_ANGKA
l('do_angka')
op(10); s('FD'); i32(1); op(74); i32(62)
# Baca nama var
l('as')
op(10); s('FD'); i32(0); op(71)
jy('KAR',32,'as'); jy('KAR',10,'as')
op(80)
l('av')
op(84); s('KAR'); op(71)
jy('KAR',-1,'ad'); jy('KAR',32,'ad'); jy('KAR',10,'ad')
j('av')
l('ad')
op(10); s('FD'); i32(1); op(86); j('loop')

# SIMPAN
l('do_simpan')
op(10); s('FD'); i32(1); op(74); i32(10)
# Baca var
l('ss')
op(10); s('FD'); i32(0); op(71)
jy('KAR',32,'ss'); jy('KAR',10,'ss')
op(80)
l('sv')
op(84); s('KAR'); op(71)
jy('KAR',-1,'sd'); jy('KAR',32,'sd'); jy('KAR',10,'sd')
j('sv')
l('sd')
op(10); s('FD'); i32(1); op(86)
# Baca nilai
l('sn_skip')
op(10); s('FD'); i32(0); op(71)
jy('KAR',32,'sn_skip'); jy('KAR',10,'sn_skip')
op(80)
l('sn_loop')
op(84); s('KAR'); op(71)
jy('KAR',-1,'sn_done'); jy('KAR',32,'sn_done'); jy('KAR',10,'sn_done')
j('sn_loop')
l('sn_done')
op(88)
op(10); s('FD'); i32(1)
op(75); s("NILAI_ANGKA")
j('loop')

# TAMBAH
l('do_tambah')
op(10); s('FD'); i32(1); op(74); i32(11)
j('ss')  # reuse SIMPAN logic

# TAMBAH_VAR
l('do_tambah_var')
op(10); s('FD'); i32(1); op(74); i32(12)
# Baca var A
l('ta_skip')
op(10); s('FD'); i32(0); op(71)
jy('KAR',32,'ta_skip'); jy('KAR',10,'ta_skip')
op(80)
l('ta_loop')
op(84); s('KAR'); op(71)
jy('KAR',-1,'ta_done'); jy('KAR',32,'ta_done'); jy('KAR',10,'ta_done')
j('ta_loop')
l('ta_done')
op(10); s('FD'); i32(1); op(86)
# Baca var B
l('tb_skip')
op(10); s('FD'); i32(0); op(71)
jy('KAR',32,'tb_skip'); jy('KAR',10,'tb_skip')
op(80)
l('tb_loop')
op(84); s('KAR'); op(71)
jy('KAR',-1,'tb_done'); jy('KAR',32,'tb_done'); jy('KAR',10,'tb_done')
j('tb_loop')
l('tb_done')
op(10); s('FD'); i32(1); op(86)
j('loop')

# BATAS_PROGRAM
l('do_batas')
op(10); s('FD'); i32(1); op(74); i32(60); j('loop')

l('finish')
op(10); s('FD'); i32(1); op(74); i32(255)
op(10); s('FD'); i32(1); op(72); op(10); s('FD'); i32(0); op(72)
op(61); s('\n[OK]\n')
op(60); op(255)

for pp,l in P:
    t = L.get(l,0); cur = f.tell(); f.seek(pp)
    f.write(struct.pack('<i',t)); f.seek(cur)
f.close()
print('OK')
