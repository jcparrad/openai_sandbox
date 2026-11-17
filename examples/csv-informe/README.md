# Caso de referencia: CSV a informe

Datos sintéticos para explicar la misma tarea en dos entornos. Proceden del
proyecto original de Knowledge Sharing. Los scripts y la referencia se conservan
sin cambios; su cálculo local está documentado como prueba previa, no como una
ejecución de Agents API.

- Entrada: [importes.csv](importes.csv), seis filas por área.
- Salidas: `resumen.json` y `totales_por_area.csv`.
- Referencia: [resultado_esperado.json](resultado_esperado.json), total 700, promedio 116,6667, Operaciones 200, Soporte 280 y Ventas 220.
- [Verificador](verificar_resultados.py): comprueba los archivos guardados contra la referencia fija.

## Reproducir el cálculo local

Desde la raíz, con Python estándar y una carpeta de salida nueva:

```bash
python3 examples/csv-informe/resumir_importes.py --input examples/csv-informe/importes.csv --output-dir evidence/csv-01
python3 examples/csv-informe/verificar_resultados.py --output-dir evidence/csv-01
```

El generador puede escribir sobre resultados existentes: usar un directorio
nuevo. El verificador espera exactamente los datos originales. Cambiar el CSV
requiere definir y revisar otra referencia.

Estos comandos no crean un sandbox, no conectan Agents API y no miden aislamiento.
Las dos futuras pruebas se harán con estos mismos datos y criterio de verificación.
