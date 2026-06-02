import markdown
from xhtml2pdf import pisa

print("[INIT] Membaca DOKUMENTASI_OUROLANG.md...")

# 1. Baca file markdown
with open('DOKUMENTASI_OUROLANG.md', 'r', encoding='utf-8') as f:
    md_text = f.read()

# 2. Konversi Markdown ke HTML (dengan dukungan tabel dan blok kode)
html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

# 3. Injeksi CSS Kustom (Tema Profesional)
html_template = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    @page {{ size: a4 portrait; margin: 2cm; }}
    body {{ font-family: Helvetica, sans-serif; color: #1a1a1a; line-height: 1.6; font-size: 12px; }}
    h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 5px; }}
    h2 {{ color: #2980b9; margin-top: 20px; }}
    blockquote {{ border-left: 4px solid #3498db; margin-left: 0; padding-left: 10px; color: #555; font-style: italic; }}
    pre {{ background-color: #1e1e1e; color: #d4d4d4; padding: 10px; border-radius: 5px; font-family: "Courier New", monospace; font-size: 10px; white-space: pre-wrap; word-wrap: break-word; }}
    code {{ font-family: "Courier New", monospace; background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px; color: #c7254e; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 15px; margin-bottom: 15px; }}
    th, td {{ border: 1px solid #dddddd; padding: 8px; text-align: left; }}
    th {{ background-color: #f2f2f2; color: #333; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

# 4. Render ke PDF
output_filename = "DOKUMENTASI_OUROLANG.pdf"
print(f"[GENERATE] Menulis ke {output_filename}...")

with open(output_filename, "w+b") as result_file:
    pisa_status = pisa.CreatePDF(html_template, dest=result_file)

if pisa_status.err:
    print("[ERROR] Terjadi kesalahan saat membuat PDF.")
else:
    print(f"[OK] PDF BERHASIL DIBUAT! Tersimpan sebagai: {output_filename}")
