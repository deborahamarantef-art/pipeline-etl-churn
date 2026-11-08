# Pipeline ETL - Churn de clientes Telco

Pre-entrega de Data Science II. Es un pipeline que lee el dataset de churn de clientes de una empresa de telecomunicaciones, lo limpia y lo guarda en Parquet para usarlo despues en el modelo.

Dataset: Telco Customer Churn (IBM) - https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## Estructura

```
main.py              -> ejecuta el pipeline
src/extract.py       -> lectura del CSV
src/transform.py     -> limpieza
src/load.py          -> guardado en Parquet
data/raw/            -> aca va el CSV original (no se sube, esta en el .gitignore)
data/processed/      -> resultado del pipeline
```

## Como ejecutarlo

1. Instalar las librerias:

```
pip install -r requirements.txt
```

2. Descargar el CSV de Kaggle y guardarlo como `data/raw/telco_churn.csv`

3. Ejecutar:

```
python main.py
```

## Etapas del pipeline

**1. Extraccion (`src/extract.py`)**

Lee el CSV con `pd.read_csv` indicando los tipos de cada columna. Las columnas de texto con pocos valores (Yes/No, tipo de contrato, etc.) se cargan como `category` y los numeros como `int8`, `int16` o `float32` en vez de los tipos por defecto. Con esto el dataframe pasa de ocupar 1.95 MB a 0.39 MB en memoria.

**2. Transformacion (`src/transform.py`)**

- Normaliza los nombres de columnas a snake_case (por ejemplo `MonthlyCharges` -> `monthly_charges`).
- Elimina filas duplicadas y clientes repetidos por `customer_id` (en este dataset no hay, pero queda el control).
- `total_charges` viene como texto y tiene 11 valores vacios. Son clientes con `tenure` = 0, es decir que recien entraron y todavia no pagaron nada, por eso se completan con 0 en lugar de borrarlos o usar el promedio.
- Pasa `churn` de Yes/No a 1/0.

**3. Carga (`src/load.py`)**

Guarda el resultado en `data/processed/telco_churn_limpio.parquet`.

Uso Parquet porque:
- guarda los tipos de datos, entonces al leerlo no hay que volver a convertir nada (en el CSV `total_charges` venia como texto)
- es un formato por columnas y comprimido, ocupa menos (185 KB contra 950 KB del CSV)
- se lee mas rapido y se pueden leer solo las columnas que se necesitan, lo que sirve cuando se entrena un modelo con muchos datos

## Resultado

7043 filas y 21 columnas, sin nulos.
