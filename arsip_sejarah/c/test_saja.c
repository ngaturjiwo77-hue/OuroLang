#include <stdio.h>
#include <stdint.h>
int main() {
    FILE *f = fopen("test_saja.obf", "wb");
    for (int i = 0; i < 17; i++) fputc(0, f);
    // SIMPAN I 5
    fputc(10, f); fputs("I", f); fputc(0, f); int32_t v=5; fwrite(&v,4,1,f);
    // SAMA_DENGAN I 5
    fputc(30, f); fputs("I", f); fputc(0, f); fputs("5", f); fputc(0, f);
    // JIKA -> lompat ke "BENAR"
    long pos_jika = ftell(f);
    fputc(40, f); v=0; fwrite(&v,4,1,f);
    // CETAK_TEKS "SALAH"
    fputc(61, f); fputs("SALAH", f); fputc(0, f);
    fputc(2, f); fputc(255, f);
    // Label BENAR:
    long pos_benar = ftell(f);
    fputc(61, f); fputs("BENAR", f); fputc(0, f);
    fputc(2, f); fputc(255, f);
    // Patch JIKA -> pos_benar
    fseek(f, pos_jika+1, SEEK_SET);
    fwrite(&pos_benar, 4, 1, f);
    fclose(f);
    printf("pos_jika=%ld, pos_benar=%ld\n", pos_jika, pos_benar);
    return 0;
}
