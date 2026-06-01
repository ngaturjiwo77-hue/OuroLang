# === OUROLANG MAKEFILE ===
# Universal: Linux / macOS / Windows (MinGW)

CC = gcc
CFLAGS = -Wall -O2
TARGET = ouro_vm
SRC = src/vm/ouro_vm_portable.c

# Deteksi OS
ifeq ($(OS),Windows_NT)
    TARGET_EXT = .exe
    RM = del /Q
else
    TARGET_EXT =
    RM = rm -f
endif

all: vm

vm: $(SRC)
	$(CC) $(CFLAGS) -o bin/$(TARGET)$(TARGET_EXT) $(SRC)
	@echo "[OK] VM terkompilasi: bin/$(TARGET)$(TARGET_EXT)"

run-vm: vm
	./bin/$(TARGET) build/hasil_kompilasi.obf

bersih:
	$(RM) bin/$(TARGET)$(TARGET_EXT)
	$(RM) build/*.obf
	@echo "[OK] Bersih."

help:
	@echo "OUROLANG - Makefile"
	@echo "  make         : Kompilasi VM portable"
	@echo "  make run-vm  : Jalankan VM dengan bytecode"
	@echo "  make bersih  : Hapus hasil kompilasi"
