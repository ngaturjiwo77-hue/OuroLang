#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

enum {
    OP_CETAK_TEKS=61, OP_CETAK_ANGKA=62,
    OP_SIMPAN=10, OP_TAMBAH=11, OP_TAMBAH_VAR=12,
    OP_KURANG=21, OP_KALI=22, OP_BAGI=23,
    OP_SAMA_DENGAN=30, OP_JIKA=40, OP_LAINNYA=42,
    OP_SELAMA=44, OP_BATAS_SELAMA=45, OP_HENTIKAN=48,
    OP_BAWAKAN=5,
    OP_BUKA_BACA=70, OP_TUTUP_FILE=71, OP_BACA_FILE=72,
    OP_BUKA_TULIS=73, OP_TULIS_BYTE=74,
    OP_BATAS_PROGRAM=2, OP_KELUAR=131,
    OP_EOF=255
};

#define MAX_VAR 256
static char n_var[MAX_VAR][64];
static int32_t v_var[MAX_VAR];
static int jml=0;
static FILE* fl[4];
static int fc=0;
static int cmp=0;
static long ls[64];
static int ld=0;

int cv(const char *n){for(int i=0;i<jml;i++)if(strcmp(n_var[i],n)==0)return i;return-1;}
void sv(const char *n,int32_t v){int i=cv(n);if(i==-1){strcpy(n_var[jml],n);v_var[jml]=v;jml++;}else v_var[i]=v;}
int32_t bv(const char *n){int i=cv(n);return(i==-1)?0:v_var[i];}
void ca(int32_t n){if(n==0){putchar('0');return;}if(n<0){putchar('-');n=-n;}char b[32];int i=0;while(n>0){b[i++]='0'+(n%10);n/=10;}while(i>0)putchar(b[--i]);}

int bb(FILE *f){return fgetc(f);}
int32_t bi(FILE *f){uint8_t b[4];for(int i=0;i<4;i++)b[i]=fgetc(f);return(int32_t)(b[0]|(b[1]<<8)|(b[2]<<16)|(b[3]<<24));}
void bs(FILE *f,char *b,int m){int i=0;while(i<m-1){int c=fgetc(f);if(c==0||c==EOF)break;b[i++]=(char)c;}b[i]='\0';}

int main(int ac,char **av){
    if(ac<2){printf("OURO VM KERNEL\n");return 1;}
    FILE *f=fopen(av[1],"rb");
    if(!f){printf("[ERR]\n");return 1;}
    for(int i=0;i<17;i++)fgetc(f);
    int h=1;
    while(h){
        int op=bb(f);
        if(op==EOF||op==OP_EOF)break;
        switch(op){
            case OP_CETAK_TEKS:{char t[8192];bs(f,t,sizeof(t));printf("%s",t);break;}
            case OP_CETAK_ANGKA:{char n[64];bs(f,n,sizeof(n));ca(bv(n));break;}
            case OP_SIMPAN:{char n[64];bs(f,n,sizeof(n));int32_t v=bi(f);sv(n,v);break;}
            case OP_TAMBAH:{char n[64];bs(f,n,sizeof(n));int32_t v=bi(f);sv(n,bv(n)+v);break;}
            case OP_TAMBAH_VAR:{char a[64],b[64];bs(f,a,sizeof(a));bs(f,b,sizeof(b));sv(a,bv(a)+bv(b));break;}
            case OP_KURANG:{char n[64];bs(f,n,sizeof(n));int32_t v=bi(f);sv(n,bv(n)-v);break;}
            case OP_KALI:{char n[64];bs(f,n,sizeof(n));int32_t v=bi(f);sv(n,bv(n)*v);break;}
            case OP_BAGI:{char n[64];bs(f,n,sizeof(n));int32_t v=bi(f);if(v)sv(n,bv(n)/v);break;}
            case OP_SAMA_DENGAN:{char a[64],b[64];bs(f,a,sizeof(a));bs(f,b,sizeof(b));int va=bv(a);int vb=(b[0]>="0"&&b[0]<="9")?atoi(b):bv(b);cmp=(va==vb)?1:0;break;}
            case OP_JIKA:{int32_t t=bi(f);if(!cmp)fseek(f,t,SEEK_SET);break;}
            case OP_LAINNYA:{int32_t t=bi(f);if(cmp)fseek(f,t,SEEK_SET);break;}
            case OP_SELAMA:{long pos=ftell(f);if(ld<64)ls[ld++]=pos;break;}
            case OP_BATAS_SELAMA:{if(ld>0)fseek(f,ls[--ld],SEEK_SET);break;}
            case OP_HENTIKAN:{if(ld>0){ld--;int d=1;while(d>0){int o=bb(f);if(o==OP_SELAMA)d++;if(o==OP_BATAS_SELAMA)d--;}}break;}
            case OP_BAWAKAN: { break; }
            case OP_BUKA_BACA:{char fn[256];bs(f,fn,sizeof(fn));FILE *fh=fopen(fn,"r");if(fh&&fc<4){fl[fc]=fh;sv("FD",fc++);}else sv("FD",-1);break;}
            case OP_TUTUP_FILE:{int s=bv("FD");if(s>=0&&s<fc&&fl[s]){fclose(fl[s]);fl[s]=NULL;}break;}
            case OP_BACA_FILE:{int s=bv("FD");if(s>=0&&s<fc&&fl[s]){rewind(fl[s]);char buf[8192]="";int i=0;while(i<8191){int c=fgetc(fl[s]);if(c==EOF)break;buf[i++]=c;}buf[i]=0;printf("%s",buf);}break;}
            case OP_BUKA_TULIS:{char fn[256];bs(f,fn,sizeof(fn));FILE *fh=fopen(fn,"w");if(fh&&fc<4){fl[fc]=fh;sv("FD",fc++);}else sv("FD",-1);break;}
            case OP_TULIS_BYTE:{int32_t v=bi(f);int s=bv("FD");if(s>=0&&s<fc&&fl[s])fputc(v&0xFF,fl[s]);break;}
            case OP_BATAS_PROGRAM: case OP_KELUAR: h=0; break;
            default:break;
        }
    }
    fclose(f);for(int i=0;i<fc;i++)if(fl[i])fclose(fl[i]);
    return 0;
}
