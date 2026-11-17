"""Compila una fuente de 12 láminas y su exportación con notas; revisa logs y páginas."""
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
BUILD = ROOT.parent / "build" / "openai-y-sandbox"
EXPECTED = 12

def main():
    for tool in ("latexmk", "lualatex", "pdfinfo", "pdftoppm"):
        if not shutil.which(tool):
            raise SystemExit(f"Falta {tool} en PATH.")
    BUILD.mkdir(parents=True, exist_ok=True)
    for stem in ("openai-sandbox", "openai-sandbox-notas"):
        result = subprocess.run([
            "latexmk", "-g", "-lualatex", "-interaction=nonstopmode",
            "-halt-on-error", "-file-line-error", "-no-shell-escape",
            f"-outdir={BUILD}", f"{stem}.tex"
        ], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (BUILD / f"{stem}.compilacion.txt").write_text(result.stdout)
        if result.returncode:
            raise SystemExit(result.stdout[-6000:])
        log = (BUILD / f"{stem}.log").read_text(errors="replace")
        problems = [line for line in log.splitlines() if re.search(
            r"Overfull|Missing character:|Undefined control sequence|LaTeX Warning:.*undefined", line)]
        if problems:
            raise SystemExit("\n".join(problems))
        pdf = BUILD / f"{stem}.pdf"
        info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
        if not re.search(rf"Pages:\s+{EXPECTED}\b", info):
            raise SystemExit(f"Se esperaban {EXPECTED} páginas: {stem}")
        shutil.copyfile(pdf, ROOT / f"{stem}.pdf")
        subprocess.run(["pdftoppm", "-scale-to", "1600", "-png", str(pdf), str(BUILD / stem)], check=True)
        print(f"Generado y renderizado: {stem}.pdf ({EXPECTED} páginas)")
    print("Revisar visualmente ambas exportaciones antes de entregar.")

if __name__ == "__main__":
    main()
