import re
import pandas as pd


def normalizar_columnas(df):
    # paso los nombres a snake_case: "MonthlyCharges" -> "monthly_charges"
    nuevas = []
    for col in df.columns:
        col = col.replace("ID", "Id")
        col = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", col)
        nuevas.append(col.lower())
    df.columns = nuevas
    return df


def limpiar_datos(df):
    df = df.copy()
    df = normalizar_columnas(df)

    # duplicados
    filas_antes = len(df)
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset="customer_id")
    print(f"Duplicados eliminados: {filas_antes - len(df)}")

    # nulos: total_charges viene como texto y tiene espacios vacios
    df["total_charges"] = pd.to_numeric(df["total_charges"], errors="coerce").astype("float32")
    nulos = df["total_charges"].isna().sum()
    print(f"Nulos en total_charges: {nulos}")

    # son clientes con tenure = 0, o sea que todavia no pagaron ningun mes.
    # por eso los completo con 0 en vez de borrarlos o usar la media
    df["total_charges"] = df["total_charges"].fillna(0)

    # si quedara algun nulo en otra columna, borro esas filas
    df = df.dropna()

    # paso el target a 0/1 para usar en el modelo despues
    df["churn"] = (df["churn"] == "Yes").astype("int8")

    print(f"Datos limpios: {df.shape[0]} filas")
    return df
