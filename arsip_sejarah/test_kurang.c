#include <stdio.h>
#include <stdint.h>

int main() {
    FILE *f = fopen("test_kurang.obf", "wb");
    // Header 17 byte
    for (int i = 0; i < 17; i++) fputc(0, f);
    // SIMPAN X 100
    fputc(10, f); fputs("X", f); fputc(0, f);
    int32_t v = 100; fwrite(&v, 4, 1, f);
    // KURANG X 30
    fputc(21, f); fputs("X", f); fputc(0, f);
    v = 30; fwrite(&v, 4, 1, f);
    // CETAK_ANGKA X
    fputc(62, f); fputs("X", f); fputc(0, f);
    // BATAS_PROGRAM
    fputc(2, f);
    // EOF
    fputc(255, f);
    fclose(f);
    printf("OK\n");
    return 0;
}
