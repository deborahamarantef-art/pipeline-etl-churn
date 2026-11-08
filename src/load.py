def guardar_parquet(df, ruta):
    df.to_parquet(ruta, index=False)
    print(f"Archivo guardado en {ruta}")
