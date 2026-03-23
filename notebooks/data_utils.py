import pandas as pd
from visualizaciones import plot_category_values

def select_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Devuelve un DataFrame filtrado con las columnas especificadas.
    Args:
        df (DataFrame): DataFrame original.
        columns (list): Lista de nombres de columnas a conservar.

    Returns:
        DataFrame: Nuevo DataFrame con solo las columnas seleccionadas.
    """
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise KeyError(f"Las siguientes columnas no existen en el DataFrame: {missing}")
    return df[columns]

from visualizaciones import plot_category_values

def missing_data_report(df: pd.DataFrame, sort: bool = True, threshold: float = 0.0, plot: bool = False) -> pd.Series:
    """
    Calcula el porcentaje de datos faltantes por columna en un DataFrame.
    Opcionalmente grafica los resultados. Si no hay faltantes, muestra un mensaje claro.
    """
    missing = df.isnull().mean() * 100
    if threshold > 0:
        missing = missing[missing > threshold]
    if sort:
        missing = missing.sort_values(ascending=False)

    if missing.empty:
        print(" No se encontraron columnas con datos faltantes.")
    else:
        print(" Porcentaje de datos faltantes por columna:")
        print(missing)
        if plot:
            plot_category_values(
                missing,
                title="Porcentaje de datos faltantes por columna",
                xlabel="Porcentaje (%)",
                ylabel="Columnas",
                palette="magma"
            )

    return missing

def detect_outliers_iqr(df: pd.DataFrame, column: str, factor: float = 1.5) -> pd.DataFrame:
    """
    Detecta outliers en una columna numérica usando el método IQR.

    Args:
        df (DataFrame): DataFrame que contiene los datos.
        column (str): Nombre de la columna numérica a analizar.
        factor (float, opcional): Multiplicador del IQR para definir los límites. 
                                  Por defecto es 1.5.

    Returns:
        DataFrame: Subconjunto del DataFrame con los outliers detectados.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    outliers = df[
        (df[column] < (Q1 - factor * IQR)) |
        (df[column] > (Q3 + factor * IQR))
    ]
    return outliers

