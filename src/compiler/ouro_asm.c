#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STACK 256
long jump_stack[MAX_STACK]; int js_p = 0;
long loop_start_stack[MAX_STACK]; long loop_hole_stack[MAX_STACK]; int ls_p = 0;

int parse_int(const char* s) { if(s[0] == '-' || (s[0] >= '0' && s[0] <= '9')) return atoi(s); return 0; }
void b_str(FILE* in, FILE* out) { char a[256]; fscanf(in, "%s", a); fprintf(out, "%s", a); fputc(0, out); }
void b_int(FILE* in, FILE* out) { char a[256]; fscanf(in, "%s", a); int v = parse_int(a); fwrite(&v, 4, 1, out); }

int main(int argc, char **argv) {
    FILE *in = fopen(argv[1], "r"); FILE *out = fopen(argv[2], "wb+");
    for(int i=0; i<17; i++) fputc(0, out);
    char t[256];
    while(fscanf(in, "%s", t) != EOF) {
        if(strcmp(t, "PROGRAM_UTAMA") == 0) fputc(1, out);
        else if(strcmp(t, "BATAS_PROGRAM") == 0) { fputc(2, out); fputc(255, out); }
        else if(strcmp(t, "CETAK_TEKS") == 0) { fputc(61, out); char c; while((c=fgetc(in))==' '); while(c!=EOF&&c!='"')c=fgetc(in); while((c=fgetc(in))!=EOF&&c!='"'){ if(c=='\\'){c=fgetc(in);if(c=='n')fputc('\n',out);else fputc(c,out);}else fputc(c,out); } fputc(0, out); }
        else if(strcmp(t, "CETAK_ANGKA") == 0) { fputc(62, out); b_str(in, out); }
        else if(strcmp(t, "SIMPAN") == 0) { fputc(10, out); b_str(in, out); b_int(in, out); }
        else if(strcmp(t, "TAMBAH") == 0) { fputc(11, out); b_str(in, out); b_int(in, out); }
        else if(strcmp(t, "KURANG") == 0) { fputc(24, out); b_str(in, out); b_int(in, out); }
        else if(strcmp(t, "TAMBAH_VAR") == 0) { fputc(12, out); b_str(in, out); b_str(in, out); }
        else if(strcmp(t, "KURANG_VAR") == 0) { fputc(25, out); b_str(in, out); b_str(in, out); }
        else if(strcmp(t, "KALI_VAR") == 0) { fputc(26, out); b_str(in, out); b_str(in, out); }
        
        else if(strcmp(t, "BILA_SAMA") == 0 || strcmp(t, "BILA_LEBIH_SAMA") == 0 || strcmp(t, "SELAMA_SAMA") == 0 || strcmp(t, "SELAMA_KURANG") == 0) {
            int is_loop = (strncmp(t, "SELAMA", 6) == 0); long l_start = ftell(out);
            if(strcmp(t, "BILA_SAMA")==0 || strcmp(t, "SELAMA_SAMA")==0) fputc(32, out); else fputc(35, out);
            b_str(in, out); b_int(in, out);
            long hole = ftell(out); int zero = 0; fwrite(&zero, 4, 1, out);
            if(is_loop) { loop_start_stack[ls_p] = l_start; loop_hole_stack[ls_p++] = hole; } else { jump_stack[js_p++] = hole; }
        }
        else if(strcmp(t, "BATAS_BILA") == 0) { if(js_p>0) { long c = ftell(out); long h = jump_stack[--js_p]; fseek(out, h, SEEK_SET); int j = (int)c; fwrite(&j, 4, 1, out); fseek(out, c, SEEK_SET); } }
        else if(strcmp(t, "BATAS_SELAMA") == 0) { if(ls_p>0) { ls_p--; long ls = loop_start_stack[ls_p]; long lh = loop_hole_stack[ls_p]; fputc(31, out); int js = (int)ls; fwrite(&js, 4, 1, out); long c = ftell(out); fseek(out, lh, SEEK_SET); int je = (int)c; fwrite(&je, 4, 1, out); fseek(out, c, SEEK_SET); } }
        
        // --- LOGIKA PENGUPAS KUTIP DIKEMBALIKAN! ---
        else if(strcmp(t, "BUKA_BACA") == 0) { fputc(70, out); char a[256]; fscanf(in, "%s", a); int l=strlen(a); if(a[0]=='"'){a[l-1]='\0';fprintf(out,"%s",a+1);}else fprintf(out,"%s",a); fputc(0,out); }
        else if(strcmp(t, "BUKA_TULIS") == 0) { fputc(73, out); char a[256]; fscanf(in, "%s", a); int l=strlen(a); if(a[0]=='"'){a[l-1]='\0';fprintf(out,"%s",a+1);}else fprintf(out,"%s",a); fputc(0,out); }
        
        else if(strcmp(t, "TUTUP_FILE") == 0) fputc(72, out);
        else if(strcmp(t, "BACA_KARAKTER") == 0) fputc(71, out);
        else if(strcmp(t, "TULIS_BYTE") == 0) { fputc(74, out); b_int(in, out); }
        else if(strcmp(t, "TULIS_BYTE_VAR") == 0) { fputc(76, out); b_str(in, out); }
        else if(strcmp(t, "TULIS_INT32") == 0) { fputc(75, out); b_str(in, out); }
        else if(strcmp(t, "POSISI_FILE") == 0) { fputc(77, out); b_str(in, out); }
        else if(strcmp(t, "GESER_FILE") == 0) { fputc(78, out); b_str(in, out); }
        else if(strcmp(t, "STRING_MULAI") == 0) fputc(80, out);
        else if(strcmp(t, "STRING_TAMBAH_VAR") == 0) { fputc(84, out); b_str(in, out); }
        else if(strcmp(t, "KONVERSI_STR_KE_INT") == 0) fputc(88, out);
        else if(strcmp(t, "ARRAY_BUAT") == 0) { fputc(90, out); b_str(in, out); b_int(in, out); }
        else if(strcmp(t, "ARRAY_SIMPAN") == 0) { fputc(91, out); b_str(in, out); b_str(in, out); b_str(in, out); }
        else if(strcmp(t, "ARRAY_AMBIL") == 0) { fputc(93, out); b_str(in, out); b_str(in, out); b_str(in, out); }
    }
    fclose(in); fclose(out); return 0;
}
