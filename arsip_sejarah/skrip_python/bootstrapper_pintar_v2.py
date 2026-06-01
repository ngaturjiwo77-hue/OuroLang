import struct
import re

def compile_ouro(input_file, output_file):
    with open(input_file, 'r') as f:
        source = f.read()

    # Ekstrak token dengan aman (menjaga kalimat utuh di dalam tanda kutip)
    tokens = [m.group(0) for m in re.finditer(r'"[^"]*"|\S+', source)]
    
    out = bytearray(b'\x00' * 17) # Header

    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token == "PROGRAM_UTAMA":
            pass # Hanya penanda, tidak butuh opcode di VM
        elif token == "BATAS_PROGRAM":
            out.append(60) # Opcode BATAS_PROGRAM
            out.append(255) # Tanda akhir file (EOF)
        elif token == "CETAK_TEKS":
            out.append(61) # <--- Opcode 61 yang benar untuk VM Anda!
            i += 1
            teks = tokens[i].strip('"').replace('\\n', '\n')
            out.extend(teks.encode('utf-8'))
            out.append(0)
        elif token == "CETAK_ANGKA":
            out.append(62)
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
        i += 1

    with open(output_file, 'wb') as f:
        f.write(out)
    print(f"[OK] Bootstrapper Pintar V2 merakit {len(out)} bytes!")

if __name__ == "__main__":
    compile_ouro("examples/test_math.ouro", "build/ouroc_universal.obf")
