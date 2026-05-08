import pandas as pd

def eliminar_duplicados(df):
    return df.drop_duplicates()

def manejar_valores_nulos(df):
    return df.fillna("Sin dato")

def normalizar_columna(df, columna):
    df[columna] = (df[columna] - df[columna].min()) / (df[columna].max() - df[columna].min())
    return df

def codificar_categoricas(df):
    return pd.get_dummies(df)

print("Funciones de preprocesamiento creadas correctamente.")