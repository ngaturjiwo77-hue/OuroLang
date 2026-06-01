#include <stdio.h>
#include <stdint.h>
int main() {
    FILE *f = fopen("test_kurang.obf", "wb");
    for (int i = 0; i < 17; i++) fputc(0, f);
    fputc(10, f); fputs("I", f); fputc(0, f); int32_t v=5; fwrite(&v,4,1,f);
    fputc(21, f); fputs("I", f); fputc(0, f); v=1; fwrite(&v,4,1,f);
    fputc(62, f); fputs("I", f); fputc(0, f);
    fputc(2, f); fputc(255, f);
    fclose(f);
    return 0;
}
