komp_path = 'src/compiler/kompilator.ouro'
with open(komp_path, 'r') as f: komp = f.read()

# 1. Update FILE_IN setelah BAWAKAN
if "SIMPAN FILE_IN FD" not in komp:
    komp = komp.replace("BAWAKAN_FILE", "BAWAKAN_FILE\n                SIMPAN FILE_IN FD")
    # 2. Update FILE_IN setelah PULIH_FILE (Kembali dari EOF)
    komp = komp.replace("PULIH_FILE FILE_IN\n                TURUN LEVEL_FILE", 
                        "PULIH_FILE FILE_IN\n                SIMPAN FILE_IN FD\n                TURUN LEVEL_FILE")
    with open(komp_path, 'w') as f: f.write(komp)
    print("✅ [KOMPILATOR] Saraf File Descriptor (FD) telah disinkronkan!")
