#include <stdio.h>
#include <stdint.h>
int main() {
    FILE *f = fopen("test_tambah.obf", "wb");
    for (int i = 0; i < 17; i++) fputc(0, f);
    // SIMPAN I 0
    fputc(10, f); fputs("I", f); fputc(0, f);
    int32_t v = 0; fwrite(&v, 4, 1, f);
    // TAMBAH I 1
    fputc(11, f); fputs("I", f); fputc(0, f);
    v = 1; fwrite(&v, 4, 1, f);
    // CETAK_ANGKA I
    fputc(62, f); fputs("I", f); fputc(0, f);
    // BATAS_PROGRAM
    fputc(2, f); fputc(255, f);
    fclose(f);
    return 0;
}
