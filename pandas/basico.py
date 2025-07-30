import pandas as pd # importamos la librería pandas con un alias como pd

# Leer archivo CSV excel con un dataframe como base
df = pd.read_csv("C:/Users/ariel/Downloads/empleados.csv")

# Filtrar por un sueldo mayor a 1.500.000
sueldo_alto = df[df["sueldo"]>1500000]
print(sueldo_alto)

# Filtrar por columna
df["cargo"]

# Filtrar con mas de una columna
df[["sueldo","nombre"]]

# Sueldo promedio
conteo = df["sueldo"].mean()
print(conteo)