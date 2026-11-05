"""Compila las diecisiete diapositivas con LuaLaTeX y latexmk, sin shell-escape."""
from pathlib import Path
import shutil
import subprocess


def main():
    source = Path(__file__).resolve().parent
    build = source.parent / "build" / "sandbox-permisos-app"
    for tool in ("latexmk", "lualatex", "pdfinfo"):
        if not shutil.which(tool):
            raise SystemExit(f"Falta {tool} en PATH.")
    build.mkdir(parents=True, exist_ok=True)
    stem = "sandbox-permisos-app"
    command = ["latexmk", "-g", "-lualatex", "-interaction=nonstopmode",
               "-halt-on-error", "-file-line-error", "-no-shell-escape",
               f"-outdir={build}", f"{stem}.tex"]
    result = subprocess.run(command, cwd=source, capture_output=True, text=True)
    (build / "compilacion.txt").write_text(result.stdout + result.stderr)
    if result.returncode:
        print("\n".join((result.stdout + result.stderr).splitlines()[-40:]))
        raise SystemExit(result.returncode)
    log = (build / f"{stem}.log").read_text(errors="replace")
    problems = [line for line in log.splitlines() if any(
        tag in line for tag in ("Overfull", "Missing character:", "Undefined control sequence"))]
    if problems:
        raise SystemExit("\n".join(problems))
    info = subprocess.run(["pdfinfo", str(build / f"{stem}.pdf")],
                          capture_output=True, text=True, check=True).stdout
    pages = next(line.split(":", 1)[1].strip() for line in info.splitlines()
                 if line.startswith("Pages:"))
    if pages != "17":
        raise SystemExit(f"Se esperaban 17 páginas, se obtuvieron {pages}.")
    shutil.copyfile(build / f"{stem}.pdf", source / f"{stem}.pdf")
    print(f"Generado: {source / f'{stem}.pdf'}")


if __name__ == "__main__":
    main()
