import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_top_categories(df: pd.DataFrame, column: str, top_n: int = 10, palette: str = "viridis") -> None:
    """
    Genera un grafico de barras con las categorias mas frecuentes de una columna especifica.

    Args:
        df (DataFrame): DataFrame que contiene los datos.
        column (str): Nombre de la columna categorica a analizar.
        top_n (int, opcional): Numero de categorias mas frecuentes a mostrar. 
                               Por defecto es 10.
        palette (str, opcional): Paleta de colores para el grafico. 
                                 Por defecto es 'viridis'.

    Returns:
        None: Muestra el grafico en pantalla.
    """
    plt.figure(figsize=(10,6))
    top_categories = df[column].value_counts().head(top_n).index
    sns.countplot(
        y=column,
        data=df[df[column].isin(top_categories)],
        hue=column,
        order=top_categories,
        palette=palette,
        legend=False
    )

    plt.title(f'Top {top_n} categorías más frecuentes en "{column}"', fontsize=14)
    plt.xlabel('Cantidad de registros')
    plt.ylabel('Categoría')

    plt.tight_layout()
    plt.show()

def plot_category_values(values: pd.Series, title="Top categorías",
                         xlabel="Valor", ylabel="Categoría",
                         palette="viridis") -> None:
    df_plot = values.reset_index()
    df_plot.columns = ["Categoria", "Valor"]

    plt.figure(figsize=(10,6))
    ax = sns.barplot(
        x="Valor",
        y="Categoria",
        hue="Categoria",
        data=df_plot,
        palette=palette,
        legend=False
    )

    plt.title(title, fontsize=14)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()