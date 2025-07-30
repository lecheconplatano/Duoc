import pandas as pd 

# Leer el archivo
df = pd.read_csv("C:/Users/ariel/Downloads/empleados_grande.csv")

# 1. Total de filas y columnas
num_total_column_filas = df.shape
print("Total filas y columnas:", num_total_column_filas)

# 2. Nombre de las columnas
columnas = df.columns
print("Columnas:", columnas)

# 3. Trabajadores del departamento Ventas
trabajadores_ventas = df[df["Departamento"] == "Ventas"]
print("\nEmpleados en Ventas:")
print(trabajadores_ventas)

# 4. Cantidad de empleados por departamento
contador_empleado_x_dep = df["Departamento"].value_counts()
print("\nCantidad de empleados por departamento:")
print(contador_empleado_x_dep)

# 5. Sueldo promedio general
sueldo_prom = df["Salario"].mean()
print(f"\nSueldo promedio general: ${round(sueldo_prom)}")

# 6. Empleados con sueldo mayor al promedio
print("\nEmpleados con sueldo mayor al promedio:")
print(df[df["Salario"] > sueldo_prom])

# 7. Sueldo más alto y más bajo
sueldo_alto = df["Salario"].max()
sueldo_bajo = df["Salario"].min()
print(f"\nSueldo más alto: ${sueldo_alto}")
print(f"Sueldo más bajo: ${sueldo_bajo}")
