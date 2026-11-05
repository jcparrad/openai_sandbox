"""Carga de trabajo sintética: evaluar, verificar y exportar sin sobrescribir."""
import argparse
import hashlib
import json
from pathlib import Path


def casos():
    return json.loads(Path(__file__).with_name("casos.json").read_text(encoding="utf-8"))


def ejecutar(operacion, entrada):
    if operacion == "sumar":
        return sum(entrada)
    if operacion == "contar_palabras":
        return len(entrada.split())
    if operacion == "mayusculas":
        return entrada.upper()
    raise ValueError(f"Operación desconocida: {operacion}")


def generar():
    resultados = []
    for caso in casos():
        valor = ejecutar(caso["operacion"], caso["entrada"])
        resultados.append({"id": caso["id"], "resultado": valor,
                           "correcto": valor == caso["esperado"]})
    return {"version": 1, "total": len(resultados),
            "correctos": sum(r["correcto"] for r in resultados),
            "resultados": resultados}


def verificar(path):
    # Referencia independiente: no invocar ejecutar() ni generar().
    referencia = casos()
    esperado = {"version": 1, "total": len(referencia), "correctos": len(referencia),
                "resultados": [{"id": c["id"], "resultado": c["esperado"],
                                "correcto": True} for c in referencia]}
    if json.loads(path.read_text(encoding="utf-8")) != esperado:
        raise ValueError("El informe no coincide con la referencia fija.")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="accion", required=True)
    p = sub.add_parser("evaluar")
    p.add_argument("--output", type=Path, required=True)
    p = sub.add_parser("verificar")
    p.add_argument("--input", type=Path, required=True)
    p = sub.add_parser("exportar")
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--dest", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.accion == "evaluar":
            # El directorio debe existir; 'x' impide reemplazar evidencia previa.
            with args.output.open("x", encoding="utf-8") as f:
                json.dump(generar(), f, ensure_ascii=False, indent=2)
                f.write("\n")
            digest = verificar(args.output)
        elif args.accion == "verificar":
            digest = verificar(args.input)
        else:
            digest = verificar(args.input)
            contenido = args.input.read_bytes()
            with args.dest.open("xb") as f:
                f.write(contenido)
            if verificar(args.dest) != digest:
                raise ValueError("La copia no coincide byte a byte con el informe.")
        print(f"PASS: 6/6 casos; SHA-256 {digest}")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"FAIL: {type(exc).__name__}: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
