#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char T[50000][128]; int t_c=0;

// Tokenizer dengan ALARM MODUL HILANG
void tokenize(const char* fn) {
    FILE *f = fopen(fn, "r"); 
    if(!f) { 
        printf("\n[!!!] FATAL: File Modul '%s' TIDAK DITEMUKAN!\n", fn);
        printf("[!!!] Periksa kembali path BAWAKAN di dalam kompilator.ouro Anda.\n");
        return; 
    }
    int c;
    while(1) {
        while((c=fgetc(f))!=EOF && (c==' '||c=='\n'||c=='\r'||c=='\t'));
        if(c==EOF) break;
        if(c=='#') { while((c=fgetc(f))!=EOF && c!='\n'); continue; }
        
        char buf[4096]; int p=0;
        if(c=='"') {
            buf[p++]=c;
            while((c=fgetc(f))!=EOF) { buf[p++]=c; if(c=='"') break; if(c=='\\') buf[p++]=fgetc(f); }
        } else {
            buf[p++]=c;
            while((c=fgetc(f))!=EOF && !(c==' '||c=='\n'||c=='\r'||c=='\t')) buf[p++]=c;
        }
        buf[p]='\0';
        
        if(strcmp(buf, "BAWAKAN")==0) {
            while((c=fgetc(f))!=EOF && (c==' '||c=='\n'||c=='\r'||c=='\t'));
            p=0; buf[p++]=c;
            while((c=fgetc(f))!=EOF && !(c==' '||c=='\n'||c=='\r'||c=='\t')) buf[p++]=c;
            buf[p]='\0';
            if(buf[0]=='"') { buf[strlen(buf)-1]='\0'; tokenize(buf+1); } 
            else tokenize(buf);
        } else {
            strcpy(T[t_c++], buf);
        }
    }
    fclose(f);
}

void ws(FILE* o, char* s) { if(s[0]=='"') { s++; s[strlen(s)-1]='\0'; fprintf(o,"%s",s); } else fprintf(o,"%s",s); fputc(0, o); }
void wi(FILE* o, char* s) { int v=atoi(s); fwrite(&v,4,1,o); }
int arity(const char* fn) { if(strcmp(fn,"DAFTAR_MAKRO")==0||strcmp(fn,"TULIS_BYTE")==0||strcmp(fn,"TULIS_ANGKA_4BYTE")==0) return 2; if(strcmp(fn,"CARI_MAKRO")==0||strcmp(fn,"TULIS_ELF_HEADER")==0||strcmp(fn,"TULIS_BUFFER_KODE")==0||strcmp(fn,"BACA_TOKEN")==0) return 1; return 0; }
struct { char n[64]; int ac; char a[5][64]; long adr; } fnc[50]; int fc=0;
struct { long p; int fid; } calls[1000]; int cc=0;

int main(int argc, char** argv) {
    printf("-> Membaca sumber: %s\n", argv[1]);
    tokenize(argv[1]);
    if(t_c < 100) { printf("[!] Peringatan: Hanya merakit %d token. Kemungkinan modul gagal dimuat!\n", t_c); }
    
    FILE *o = fopen(argv[2], "wb"); for(int i=0;i<17;i++) fputc(0,o);
    for(int i=0; i<t_c; i++) { if(strcmp(T[i],"FUNGSI_PARAM")==0 || strcmp(T[i],"FUNGSI_KEMBALI")==0) { i++; strcpy(fnc[fc].n, T[i]); fnc[fc].ac = arity(T[i]); for(int a=0; a<fnc[fc].ac; a++) { i++; strcpy(fnc[fc].a[a], T[i]); } fc++; } }
    long jmp[256]; int jp=0; long ls[256], lh[256]; int lsp=0; int uc=0; long current_fn_jump = 0;
    
    for(int i=0; i<t_c; i++) {
        char* t = T[i];
        if(strcmp(t,"PROGRAM_UTAMA")==0) fputc(1,o);
        else if(strcmp(t,"BATAS_PROGRAM")==0) { fputc(2,o); fputc(255,o); }
        else if(strcmp(t,"CETAK_TEKS")==0) { fputc(61,o); i++; ws(o,T[i]); }
        else if(strcmp(t,"CETAK_ANGKA")==0) { fputc(62,o); i++; ws(o,T[i]); }
        else if(strcmp(t,"SIMPAN")==0) { fputc(10,o); i++; ws(o,T[i]); i++; wi(o,T[i]); }
        else if(strcmp(t,"UBAH")==0) { fputc(10,o); i++; ws(o,T[i]); wi(o,"0"); fputc(12,o); ws(o,T[i]); i++; ws(o,T[i]); }
        else if(strcmp(t,"TAMBAH")==0) { fputc(11,o); i++; ws(o,T[i]); i++; wi(o,T[i]); }
        else if(strcmp(t,"KURANG")==0) { fputc(24,o); i++; ws(o,T[i]); i++; wi(o,T[i]); }
        else if(strcmp(t,"KALI")==0) { fputc(22,o); i++; ws(o,T[i]); i++; wi(o,T[i]); }
        else if(strcmp(t,"BAGI")==0) { fputc(23,o); i++; ws(o,T[i]); i++; wi(o,T[i]); }
        else if(strcmp(t,"NAIK")==0) { fputc(11,o); i++; ws(o,T[i]); wi(o,"1"); }
        else if(strcmp(t,"TURUN")==0) { fputc(24,o); i++; ws(o,T[i]); wi(o,"1"); }
        else if(strcmp(t,"ARRAY_SIMPAN")==0) { fputc(91,o); i++; ws(o,T[i]); i++; ws(o,T[i]); i++; ws(o,T[i]); }
        else if(strcmp(t,"ARRAY_AMBIL")==0 || strcmp(t,"BACA_ARRAY")==0) { fputc(93,o); i++; ws(o,T[i]); i++; ws(o,T[i]); i++; ws(o,T[i]); }
        else if(strcmp(t,"GLOBAL_ARRAY")==0) { fputc(90,o); i++; ws(o,T[i]); i++; }
        else if(strcmp(t,"GLOBAL")==0) { fputc(10,o); i++; ws(o,T[i]); i++; wi(o,T[i]); }
        else if(strcmp(t,"TUMPUK_FILE")==0) { fputc(102,o); i++; ws(o,T[i]); }
        else if(strcmp(t,"PULIH_FILE")==0) { fputc(103,o); i++; ws(o,T[i]); }
        else if(strcmp(t,"BUKA_BACA")==0) { fputc(70,o); i++; ws(o,T[i]); i++; ws(o,T[i]); }
        else if(strcmp(t,"BUKA_TULIS")==0) { fputc(73,o); i++; ws(o,T[i]); i++; ws(o,T[i]); }
        else if(strcmp(t,"TUTUP_FILE")==0) { fputc(72,o); }
        else if(strcmp(t,"BACA_KARAKTER")==0) { fputc(71,o); }
        else if(strcmp(t,"TULIS_KARAKTER")==0) { fputc(74,o); i++; ws(o,T[i]); i++; ws(o,T[i]); }
        else if(strcmp(t,"BILA_SAMA")==0 || strcmp(t,"SELAMA_SAMA")==0 || strcmp(t,"BILA_LEBIH_SAMA")==0 || strcmp(t,"SELAMA_KURANG")==0) { int is_lp = (strncmp(t,"SELAMA",6)==0); long l_st = ftell(o); if(strcmp(t,"BILA_SAMA")==0||strcmp(t,"SELAMA_SAMA")==0) fputc(32,o); else if(strcmp(t,"SELAMA_KURANG")==0) fputc(34,o); else fputc(35,o); i++; ws(o,T[i]); i++; wi(o,T[i]); long h = ftell(o); wi(o,"0"); if(is_lp) { ls[lsp]=l_st; lh[lsp++]=h; } else jmp[jp++]=h; }
        else if(strcmp(t,"LANJUTKAN")==0) { fputc(31,o); int jxl=(int)ls[lsp-1]; fwrite(&jxl,4,1,o); } else if(strcmp(t,"LANJUTKAN")==0) { fputc(31,o); int jxl=(int)ls[lsp-1]; fwrite(&jxl,4,1,o); } else if(strcmp(t,"BATAS_BILA")==0) { long c=ftell(o); long h=jmp[--jp]; fseek(o,h,SEEK_SET); int j=(int)c; fwrite(&j,4,1,o); fseek(o,c,SEEK_SET); }
        else if(strcmp(t,"BATAS_SELAMA")==0) { lsp--; fputc(31,o); int js=(int)ls[lsp]; fwrite(&js,4,1,o); long c=ftell(o); fseek(o,lh[lsp],SEEK_SET); int je=(int)c; fwrite(&je,4,1,o); fseek(o,c,SEEK_SET); }
        else if(strcmp(t,"FUNGSI_PARAM")==0 || strcmp(t,"FUNGSI_KEMBALI")==0) { fputc(31,o); current_fn_jump=ftell(o); int z=0; fwrite(&z,4,1,o); i++; int fid=-1; for(int k=0;k<fc;k++) if(strcmp(fnc[k].n,T[i])==0) fid=k; fnc[fid].adr=ftell(o); for(int a=0;a<fnc[fid].ac;a++) i++; }
        else if(strcmp(t,"BATAS_FUNGSI")==0) { fputc(101,o); long cur=ftell(o); fseek(o,current_fn_jump,SEEK_SET); int cpi=(int)cur; fwrite(&cpi,4,1,o); fseek(o,cur,SEEK_SET); }
        else if(strcmp(t,"KEMBALIKAN")==0) { i++; int iv=(T[i][0]=='"'||(T[i][0]>='0'&&T[i][0]<='9')||T[i][0]=='-'); if(iv){fputc(10,o);ws(o,"RET_VAL");wi(o,T[i]);}else{fputc(10,o);ws(o,"RET_VAL");wi(o,"0");fputc(12,o);ws(o,"RET_VAL");ws(o,T[i]);} fputc(101,o); }
        else if(strcmp(t,"PANGGIL_PARAM")==0 || strcmp(t,"PANGGIL_KEMBALI")==0) { int is_ret=(strcmp(t,"PANGGIL_KEMBALI")==0); char rv[64]; if(is_ret){i++;strcpy(rv,T[i]);} i++; char* fn=T[i]; int fid=-1; for(int k=0;k<fc;k++) if(strcmp(fnc[k].n,fn)==0) fid=k; for(int a=0;a<fnc[fid].ac;a++) { i++; int iv=(T[i][0]=='"'||(T[i][0]>='0'&&T[i][0]<='9')||T[i][0]=='-'); if(iv){fputc(10,o);ws(o,fnc[fid].a[a]);wi(o,T[i]);}else if(strcmp(fnc[fid].a[a],T[i])!=0){fputc(10,o);ws(o,fnc[fid].a[a]);wi(o,"0");fputc(12,o);ws(o,fnc[fid].a[a]);ws(o,T[i]);} } fputc(100,o); calls[cc].p=ftell(o); calls[cc].fid=fid; cc++; wi(o,"0"); if(is_ret){fputc(10,o);ws(o,rv);wi(o,"0");fputc(12,o);ws(o,rv);ws(o,"RET_VAL");} }
    }
    for(int c=0;c<cc;c++){fseek(o,calls[c].p,SEEK_SET);int a=(int)fnc[calls[c].fid].adr;fwrite(&a,4,1,o);}
    long ukuran_asli = ftell(o); fclose(o);
    long sz = ukuran_asli;
    printf("-> Perakitan Selesai! Ukuran Biner: %ld bytes\n", sz);
    return 0;
}
