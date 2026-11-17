"""Compila los diagramas TikZ y exporta dos PNG para la guía Markdown."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build"
OUTPUT = ROOT / "output" / "pdf"
ASSETS = ROOT / "assets"
for directory in (BUILD, OUTPUT, ASSETS):
    directory.mkdir(parents=True, exist_ok=True)

result = subprocess.run(
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
     f"-output-directory={BUILD}", str(ROOT / "diagramas.tex")],
    cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
)
(BUILD / "compilacion.txt").write_text(result.stdout)
if result.returncode:
    raise SystemExit(result.stdout[-6000:])
log = (BUILD / "diagramas.log").read_text()
if re.search(r"Overfull|Missing character", log):
    raise SystemExit("Revisar desbordamientos o caracteres faltantes en build/diagramas.log")
pdf = BUILD / "diagramas.pdf"
info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
if not re.search(r"Pages:\s+2\b", info):
    raise SystemExit("Se esperaban exactamente dos páginas")
(OUTPUT / "diagramas.pdf").write_bytes(pdf.read_bytes())
subprocess.run(["pdftoppm", "-scale-to", "2000", "-png", str(pdf), str(ASSETS / "recorrido")], check=True)
print("PDF de dos páginas y dos PNG generados. Revisar visualmente ambos PNG.")
