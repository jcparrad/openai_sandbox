"""Comprueba archivos reales contra la referencia del caso sintetico."""
import argparse
import csv
import json
from decimal import Decimal
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    expected = json.loads(Path(__file__).with_name("resultado_esperado.json").read_text(encoding="utf-8"))
    try:
        observed = json.loads((args.output_dir / "resumen.json").read_text(encoding="utf-8"))
        if observed != expected:
            raise ValueError("El JSON no coincide con la referencia.")
        with (args.output_dir / "totales_por_area.csv").open(encoding="utf-8", newline="") as source:
            reader = csv.DictReader(source)
            if reader.fieldnames != ["area", "total"]:
                raise ValueError("Cabecera CSV incorrecta.")
            rows = list(reader)
        if len(rows) != len(expected["por_area"]):
            raise ValueError("Cantidad de areas incorrecta.")
        groups = {row["area"]: Decimal(row["total"]) for row in rows}
        reference = {area: Decimal(str(total)) for area, total in expected["por_area"].items()}
        if groups != reference:
            raise ValueError("Las agrupaciones del CSV no coinciden.")
    except (OSError, ValueError, KeyError, ArithmeticError) as exc:
        parser.exit(1, f"Verificacion fallida: {exc}\n")
    print("PASS: JSON y CSV coinciden con la referencia; total 700, 6 filas y promedio 116.6667.")


if __name__ == "__main__":
    main()
