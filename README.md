# Starbucks Analysis

Proyecto de análisis de datos de Starbucks utilizando Python y Jupyter Notebook.  
Incluye exploración de datos, limpieza y visualizaciones con Pandas, NumPy, Seaborn y Matplotlib.

## Acerca del conjunto de datos
El dataset simula transacciones de Starbucks (100.000), incluyendo información sobre canal de pedido, tamaño del carrito, membresía en recompensas, tiempos de cumplimiento y gasto total.  
Se utiliza para explorar patrones de consumo y entrenar modelos predictivos orientados a entender los factores que impulsan el gasto.

# Conclusión del proyecto

Este trabajo integra un **EDA completo**, preparación de datos y un **modelo de Random Forest** que predice el gasto total con gran precisión (R²=0.97, RMSE=1.02).  
Se aplicaron técnicas de **limpieza, encoding, train/test split, evaluación y análisis de importancia de variables**, demostrando dominio de **Python, pandas, scikit-learn y visualización con Seaborn/Matplotlib**.  
Los resultados confirman que el **tamaño del carrito**, el **canal Mobile App** y las **personalizaciones** son los principales impulsores del gasto, ofreciendo insights estratégicos para fidelización y optimización de canales.  
Un proyecto sólido de **data analysis + machine learning**, documentado de forma clara y profesional para portfolio.

## Tecnologías utilizadas
- Python  
- Jupyter Notebook  
- pandas, NumPy  
- scikit-learn  
- Seaborn, Matplotlib

## Resultados clave
- Modelo Random Forest con R²=0.97 y RMSE=1.02  
- Identificación de variables más influyentes: tamaño del carrito, canal Mobile App y personalizaciones  
- Insights estratégicos para fidelización y optimización de canales

## Instalación
Clonar el repositorio y crear un entorno virtual:
```bash
git clone https://github.com/AgustinRodr/starbucks_analysis.git
cd starbucks_analysis
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt