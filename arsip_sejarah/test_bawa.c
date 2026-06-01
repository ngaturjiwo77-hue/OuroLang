#include <stdio.h>
#include <stdint.h>

int main() {
    FILE *f = fopen("test_bawa.obf", "wb");
    for (int i = 0; i < 17; i++) fputc(0, f);
    // BAWAKAN "lib/std.ouro"
    fputc(5, f); fputs("lib/std.ouro", f); fputc(0, f);
    // CETAK_TEKS "Done"
    fputc(61, f); fputs("Done", f); fputc(0, f);
    // BATAS_PROGRAM
    fputc(2, f);
    fputc(255, f);
    fclose(f);
    printf("OK\n");
    return 0;
}
