"""Caso de referencia local; no llama a OpenAI ni crea un sandbox."""
import argparse
import csv
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


def numeric(value):
    return int(value) if value == value.to_integral_value() else float(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        totals = {}
        count = 0
        with args.input.open(encoding="utf-8", newline="") as source:
            reader = csv.DictReader(source)
            if reader.fieldnames != ["id", "area", "importe"]:
                raise ValueError("Se esperan las columnas id,area,importe.")
            for row in reader:
                if None in row or any(value is None for value in row.values()):
                    raise ValueError("Fila incompleta o con columnas adicionales.")
                area = row["area"].strip()
                if not row["id"].strip() or not area:
                    raise ValueError("Cada fila necesita id y area.")
                amount = Decimal(row["importe"])
                if not amount.is_finite():
                    raise ValueError("El importe debe ser un numero finito.")
                totals[area] = totals.get(area, Decimal(0)) + amount
                count += 1
        if count == 0:
            raise ValueError("El CSV no contiene filas de datos.")
        total = sum(totals.values(), Decimal(0))
        average = (total / count).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
        result = {
            "filas": count,
            "total": numeric(total),
            "promedio": numeric(average),
            "por_area": {area: numeric(value) for area, value in sorted(totals.items())},
        }
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir / "resumen.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        with (args.output_dir / "totales_por_area.csv").open(
            "w", encoding="utf-8", newline=""
        ) as destination:
            writer = csv.writer(destination)
            writer.writerow(["area", "total"])
            writer.writerows((area, format(value, "f")) for area, value in sorted(totals.items()))
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
    except (OSError, ValueError, InvalidOperation) as exc:
        parser.exit(2, f"No se pudo generar el reporte: {exc}\n")


if __name__ == "__main__":
    main()
