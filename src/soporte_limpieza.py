import pandas as pd
import numpy as np


def convertir_columnas_datetime(df, columnas, formato="%Y-%m-%d"):
    """
    Convierte las columnas especificadas a tipo datetime.

    Args:
        df (pd.DataFrame): DataFrame con los datos.
        columnas (list): Lista de nombres de columnas a convertir.
        formato (str, opcional): Formato de la fecha a usar. Por defecto, "%Y-%m-%d".

    Returns:
        pd.DataFrame: DataFrame con las columnas convertidas.
    """
    for col in columnas:
        # Intenta convertir la columna a datetime
        df[col] = pd.to_datetime(df[col], format=formato, errors="coerce")
        
        # Calcula la cantidad de valores no convertidos
        total_valores = len(df[col])
        no_convertidos = df[col].isna().sum()
        
        if no_convertidos > 0:
            print(f"Advertencia: En la columna '{col}' se han asignado NaT en {no_convertidos} de {total_valores} registros ({(no_convertidos/total_valores)*100} %).")

    return df