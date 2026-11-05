"""Prepara dos proyectos sintéticos y abre Codex sin editar config global."""
import argparse
import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tomllib

BASE = Path(__file__).resolve().parent
MODOS = ("manual", "automatico")


def configuracion(modo):
    return tomllib.loads((BASE / f"{modo}.config.toml").read_text(encoding="utf-8"))


def variantes_validas():
    a, b = (configuracion(m) for m in MODOS)
    if a.pop("approvals_reviewer") != "user" or b.pop("approvals_reviewer") != "auto_review":
        raise ValueError("Los revisores no corresponden a la comparación.")
    if a != b:
        raise ValueError("Las variantes difieren en algo más que el revisor.")


def preparar(lab):
    # Debe ser una carpeta nueva, fuera de temporales y sin datos personales.
    lab.mkdir(parents=True, exist_ok=False)
    for modo in MODOS:
        proyecto = lab / modo / "proyecto"
        proyecto.mkdir(parents=True)
        (lab / modo / "entregas").mkdir()
        for name in ("evaluar.py", "casos.json", "prompt.txt"):
            shutil.copyfile(BASE / name, proyecto / name)
    print("Laboratorio preparado. No se inició Codex ni se modificó config.toml.")


def hojas(tabla, prefijo=""):
    for clave, valor in tabla.items():
        nombre = f"{prefijo}.{clave}" if prefijo else clave
        if isinstance(valor, dict):
            yield from hojas(valor, nombre)
        elif isinstance(valor, bool):
            yield nombre, str(valor).lower()
        elif isinstance(valor, str):
            yield nombre, json.dumps(valor)
        else:
            raise ValueError(f"Tipo de configuración no admitido: {nombre}")


def comando(lab, modo, modelo):
    proyecto = lab / modo / "proyecto"
    if not proyecto.is_dir() or not (proyecto.parent / "entregas").is_dir():
        raise ValueError("Falta preparar el laboratorio.")
    for name in ("evaluar.py", "casos.json", "prompt.txt"):
        if (proyecto / name).read_bytes() != (BASE / name).read_bytes():
            raise ValueError(f"{name} no coincide con la versión actual. Conserva este laboratorio y prepara uno nuevo.")
    if (proyecto / "informe.json").exists() or (proyecto.parent / "entregas/informe.json").exists():
        raise ValueError("Ya hay evidencia de una ejecución. Preparar otro laboratorio.")
    cmd = ["codex", "--no-daemon", "--no-alt-screen", "--strict-config",
           "--cd", str(proyecto), "--model", modelo]
    for clave, valor in hojas(configuracion(modo)):
        cmd.extend(["--config", f"{clave}={valor}"])
    cmd.append((BASE / "prompt.txt").read_text(encoding="utf-8"))
    return cmd


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="accion", required=True)
    s = sub.add_parser("preparar")
    s.add_argument("--lab", type=Path, required=True)
    s = sub.add_parser("iniciar")
    s.add_argument("--lab", type=Path, required=True)
    s.add_argument("--modo", choices=MODOS, required=True)
    s.add_argument("--modelo", required=True, help="El mismo modelo disponible en ambos modos")
    s.add_argument("--mostrar", action="store_true", help="Mostrar sin abrir una sesión")
    args = p.parse_args()
    try:
        variantes_validas()
        lab = args.lab.expanduser().resolve()
        if args.accion == "preparar":
            preparar(lab)
        else:
            cmd = comando(lab, args.modo, args.modelo)
            if args.mostrar:
                print(shlex.join(cmd))
            else:
                if not sys.stdin.isatty() or not sys.stdout.isatty():
                    raise ValueError("Abrir desde una terminal interactiva para observar los permisos.")
                if not shutil.which("codex"):
                    raise ValueError("Codex CLI no está en PATH.")
                raise SystemExit(subprocess.run(cmd, cwd=lab / args.modo / "proyecto").returncode)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {type(exc).__name__}: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
