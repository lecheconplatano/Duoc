import pandas as pd

vehiculos = {
    "ABCD12": ["Toyota", "Corolla", 2020, "Sedán"],
    "EFGH34": ["Hyundai", "Tucson", 2022, "SUV"],
    "IJKL56": ["Chevrolet", "Spark", 2019, "Hatchback"],
    "MNOP78": ["Kia", "Rio", 2021, "Sedán"],
    "QRST90": ["Ford", "Escape", 2020, "SUV"],
    "UVWX11": ["Nissan", "Versa", 2018, "Sedán"],
    "YZAB22": ["Honda", "Civic", 2023, "Sedán"],
    "CDEF33": ["Mazda", "CX-5", 2022, "SUV"],
    "GHIJ44": ["Peugeot", "208", 2021, "Hatchback"],
    "KLMN55": ["Volkswagen", "Golf", 2020, "Hatchback"]
}

# Convertir a DataFrame correctamente
df = pd.DataFrame.from_dict(vehiculos, orient="index", columns=["Marca", "Modelo", "Año", "Tipo"])
df.index.name = "Patente"

print(df[df["Año"] < 2020])
