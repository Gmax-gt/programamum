import pandas as pd

# Cargar datos
archivo_entrada = "C:\Users\santex\Downloads\cargar - Hoja 1.csv"
archivo_salida = "C:\Users\santex\Downloads\Libro1.xlsx - 05-07 (1).csv"

# Leer el archivo CSV de entrada
df = pd.read_csv(archivo_entrada)

# Aquí se pueden agregar transformaciones o manipulaciones de datos necesarias
# Por ejemplo, podríamos imprimir las primeras filas del dataframe para verificar su contenido
print("Datos cargados:")
print(df.head())

# Exportar los datos procesados a un nuevo archivo CSV
df.to_csv(archivo_salida, index=False)

print(f"Datos exportados a {archivo_salida}")