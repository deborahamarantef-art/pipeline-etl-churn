from src.extract import leer_datos
from src.transform import limpiar_datos
from src.load import guardar_parquet

RUTA_ENTRADA = "data/raw/telco_churn.csv"
RUTA_SALIDA = "data/processed/telco_churn_limpio.parquet"


def main():
    print("1. Extraccion")
    df = leer_datos(RUTA_ENTRADA)

    print("2. Transformacion")
    df = limpiar_datos(df)

    print("3. Carga")
    guardar_parquet(df, RUTA_SALIDA)


if __name__ == "__main__":
    main()
