#include <stdio.h>
#include <stdint.h>
int main() {
    FILE *f = fopen("test_sama.obf", "wb");
    for (int i = 0; i < 17; i++) fputc(0, f);
    // SIMPAN I 0
    fputc(10, f); fputs("I", f); fputc(0, f); int32_t v=0; fwrite(&v,4,1,f);
    // SELAMA
    fputc(44, f);
    // CETAK_TEKS "X"
    fputc(61, f); fputs("X", f); fputc(0, f);
    // TAMBAH I 1
    fputc(11, f); fputs("I", f); fputc(0, f); v=1; fwrite(&v,4,1,f);
    // SAMA_DENGAN I 2
    fputc(30, f); fputs("I", f); fputc(0, f); fputs("2", f); fputc(0, f);
    // JIKA -> target setelah HENTIKAN
    fputc(40, f); v=99; fwrite(&v,4,1,f); // placeholder
    // HENTIKAN
    fputc(48, f);
    // BATAS_JIKA (no-op)
    // BATAS_SELAMA
    fputc(45, f);
    // CETAK_TEKS "Done"
    fputc(61, f); fputs("Done", f); fputc(0, f);
    fputc(2, f); fputc(255, f);
    fclose(f);
    return 0;
}
