import pandas as pd

# columnas con pocos valores distintos -> las cargo como category para usar menos memoria
COLUMNAS_CATEGORICAS = [
    "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
    "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod", "Churn",
]


def leer_datos(ruta):
    tipos = {col: "category" for col in COLUMNAS_CATEGORICAS}
    tipos["SeniorCitizen"] = "int8"
    tipos["tenure"] = "int16"
    tipos["MonthlyCharges"] = "float32"
    # TotalCharges la leo como texto porque trae valores vacios (" "), la arreglo en la limpieza

    df = pd.read_csv(ruta, dtype=tipos)
    print(f"Datos leidos: {df.shape[0]} filas y {df.shape[1]} columnas")
    return df
