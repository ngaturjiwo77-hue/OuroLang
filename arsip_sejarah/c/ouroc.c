#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

enum {
    OP_SIMPAN=10, OP_TAMBAH=11, OP_TAMBAH_VAR=12,
    OP_KURANG=21, OP_KURANG_VAR=25, OP_KALI=22, OP_KALI_VAR=26,
    OP_BAGI=23, OP_BAGI_VAR=27,
    OP_SAMA_DENGAN=30, OP_TIDAK_SAMA=31, OP_LEBIH_BESAR=32, OP_LEBIH_KECIL=33,
    OP_JIKA=40, OP_LAINNYA=42, OP_SELAMA=44, OP_BATAS_SELAMA=45, OP_SELAMA_KONDISI=46,
    OP_HENTIKAN=48, OP_LANJUTKAN=49,
    OP_CETAK_TEKS=61, OP_CETAK_ANGKA=62,
    OP_BAWAKAN=5, OP_BACA=65, OP_MASUKAN=69,
    OP_BATAS_PROGRAM=2, OP_PROGRAM_UTAMA=1,
    OP_KELUAR=131, OP_TUNDA=121,
    OP_EOF=255
};

void tulis_byte(FILE *out, uint8_t b) { fputc(b, out); }
void tulis_int32(FILE *out, int32_t v) {
    fputc(v & 0xFF, out); fputc((v>>8) & 0xFF, out);
    fputc((v>>16) & 0xFF, out); fputc((v>>24) & 0xFF, out);
}
void tulis_string(FILE *out, const char *s) {
    while (*s) fputc(*s++, out);
    fputc(0, out);
}

int main() {
    FILE *in = fopen("input.ouro", "r");
    FILE *out = fopen("output.obf", "wb");
    if (!in || !out) { printf("[ERR]\n"); return 1; }
    
    for (int i = 0; i < 17; i++) tulis_byte(out, 0);
    
    char kata[256];
    while (fscanf(in, "%s", kata) != EOF) {
        int len = strlen(kata);
        
        // String literal (diawali kutip)
        if (kata[0] == '"') {
            kata[len-1] = '\0';
            tulis_byte(out, OP_CETAK_TEKS);
            tulis_string(out, kata + 1);
            continue;
        }
        
        // Deteksi keyword
        if (strcmp(kata, "PROGRAM_UTAMA") == 0) continue;
        
        #define SCAN_VAR fscanf(in, "%s", var)
        #define SCAN_VAR_VAL fscanf(in, "%s %d", var, &val)
        #define SCAN_VAR_VAR fscanf(in, "%s %s", a, b)
        #define EMIT_VAR tulis_string(out, var)
        #define EMIT_VAL tulis_int32(out, val)
        #define EMIT_VAR_VAR tulis_string(out, a); tulis_string(out, b)
        
        char var[64], a[64], b[64]; int val;
        
        if (strcmp(kata, "CETAK_TEKS") == 0) {
            fscanf(in, "%s", kata);
            len = strlen(kata);
            if (kata[0] == '"') { kata[len-1] = '\0'; tulis_byte(out, OP_CETAK_TEKS); tulis_string(out, kata + 1); }
            else { tulis_byte(out, OP_CETAK_TEKS); tulis_string(out, kata); }
        }
        else if (strcmp(kata, "CETAK_ANGKA") == 0) { SCAN_VAR; tulis_byte(out, OP_CETAK_ANGKA); EMIT_VAR; }
        else if (strcmp(kata, "SIMPAN") == 0) { SCAN_VAR_VAL; tulis_byte(out, OP_SIMPAN); EMIT_VAR; EMIT_VAL; }
        else if (strcmp(kata, "TAMBAH") == 0) { SCAN_VAR_VAL; tulis_byte(out, OP_TAMBAH); EMIT_VAR; EMIT_VAL; }
        else if (strcmp(kata, "TAMBAH_VAR") == 0) { SCAN_VAR_VAR; tulis_byte(out, OP_TAMBAH_VAR); EMIT_VAR_VAR; }
        else if (strcmp(kata, "KURANG") == 0) { SCAN_VAR_VAL; tulis_byte(out, OP_KURANG); EMIT_VAR; EMIT_VAL; }
        else if (strcmp(kata, "KURANG_VAR") == 0) { SCAN_VAR_VAR; tulis_byte(out, OP_KURANG_VAR); EMIT_VAR_VAR; }
        else if (strcmp(kata, "KALI") == 0) { SCAN_VAR_VAL; tulis_byte(out, OP_KALI); EMIT_VAR; EMIT_VAL; }
        else if (strcmp(kata, "KALI_VAR") == 0) { SCAN_VAR_VAR; tulis_byte(out, OP_KALI_VAR); EMIT_VAR_VAR; }
        else if (strcmp(kata, "BAGI") == 0) { SCAN_VAR_VAL; tulis_byte(out, OP_BAGI); EMIT_VAR; EMIT_VAL; }
        else if (strcmp(kata, "BAGI_VAR") == 0) { SCAN_VAR_VAR; tulis_byte(out, OP_BAGI_VAR); EMIT_VAR_VAR; }
        else if (strcmp(kata, "SAMA_DENGAN") == 0) { SCAN_VAR_VAR; tulis_byte(out, OP_SAMA_DENGAN); EMIT_VAR_VAR; }
        else if (strcmp(kata, "JIKA") == 0) { tulis_byte(out, OP_JIKA); tulis_int32(out, 0); }
        else if (strcmp(kata, "LAINNYA") == 0) { tulis_byte(out, OP_LAINNYA); tulis_int32(out, 0); }
        else if (strcmp(kata, "SELAMA") == 0) { tulis_byte(out, OP_SELAMA); tulis_int32(out, 0); }
        else if (strcmp(kata, "SELAMA_KONDISI") == 0) { tulis_byte(out, OP_SELAMA_KONDISI); tulis_int32(out, 0); }
        else if (strcmp(kata, "BATAS_SELAMA") == 0) { tulis_byte(out, OP_BATAS_SELAMA); }
        else if (strcmp(kata, "HENTIKAN") == 0) { tulis_byte(out, OP_HENTIKAN); }
        else if (strcmp(kata, "LANJUTKAN") == 0) { tulis_byte(out, OP_LANJUTKAN); }
        else if (strcmp(kata, "BACA") == 0) { SCAN_VAR; tulis_byte(out, OP_BACA); EMIT_VAR; }
        else if (strcmp(kata, "MASUKAN") == 0) { SCAN_VAR; tulis_byte(out, OP_MASUKAN); EMIT_VAR; }
        else if (strcmp(kata, "KELUAR") == 0) { tulis_byte(out, OP_KELUAR); }
        else if (strcmp(kata, "TUNDA") == 0) { int v; fscanf(in, "%d", &v); tulis_byte(out, OP_TUNDA); tulis_int32(out, v); }
        else if (strcmp(kata, "BAWAKAN") == 0) { fscanf(in, "%s", kata); tulis_byte(out, OP_BAWAKAN); tulis_string(out, kata); }
        else if (strcmp(kata, "BATAS_PROGRAM") == 0) { tulis_byte(out, OP_BATAS_PROGRAM); }
    }
    
    tulis_byte(out, OP_EOF);
    fclose(in); fclose(out);
    printf("OUROC C v2.0\n[OK]\n");
    return 0;
}
