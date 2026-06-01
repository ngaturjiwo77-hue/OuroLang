import struct
import sys

def compile_ouro(input_file, output_file):
    with open(input_file, 'r') as f:
        source = f.read()

    tokens = source.split()
    out = bytearray(b'\x00' * 17) # Header kosong

    # Ini adalah simulasi dari apa yang kompilator.ouro V4 lakukan!
    # Menggunakan sidik jari / keyword yang sama.
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token == "PROGRAM_UTAMA":
            out.append(255)
        elif token == "BATAS_PROGRAM":
            out.append(60)
        elif token == "CETAK_TEKS":
            out.append(21)
            i += 1
            # Ambil string (hilangkan tanda kutip dan tangani \n)
            teks = tokens[i].strip('"').replace('\\n', '\n')
            out.extend(teks.encode('utf-8'))
            out.append(0)
        elif token == "CETAK_ANGKA":
            out.append(22)
            i += 1
            out.extend(tokens[i].encode('utf-8'))
            out.append(0)
        elif token == "SIMPAN":
            out.append(10)
            i += 1
            out.extend(tokens[i].encode('utf-8'))
            out.append(0)
            i += 1
            out.extend(struct.pack("<i", int(tokens[i])))
        elif token == "TAMBAH":
            out.append(11)
            i += 1
            out.extend(tokens[i].encode('utf-8'))
            out.append(0)
            i += 1
            out.extend(struct.pack("<i", int(tokens[i])))
        elif token == "KURANG":
            out.append(12)
            i += 1
            out.extend(tokens[i].encode('utf-8'))
            out.append(0)
            i += 1
            out.extend(struct.pack("<i", int(tokens[i])))
        # Anda bisa menambahkan sidik jari lain di sini nanti
        
        i += 1

    with open(output_file, 'wb') as f:
        f.write(out)
    print(f"[OK] Bootstrapper Pintar merakit {len(out)} bytes!")

if __name__ == "__main__":
    compile_ouro("examples/test_math.ouro", "build/ouroc_universal.obf")
