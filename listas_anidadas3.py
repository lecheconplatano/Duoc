productos = [
    {"codigo": "A101", "nombre": "Teclado", "precio": 10000, "categoria": "Periféricos"},
    {"codigo": "A102", "nombre": "Mouse", "precio": 5000, "categoria": "Periféricos"},
    {"codigo": "B201", "nombre": "SSD", "precio": 25000, "categoria": "Almacenamiento"},
    {"codigo": "C301", "nombre": "Monitor", "precio": 80000, "categoria": "Pantallas"},
]

# Filtrar productos por precio mayor a 10.000
caros = [p for p in productos if p["precio"] > 10000]

# Obtener solo los nombres
nombres = [p["nombre"] for p in productos]

#  Crear un diccionario con código como clave
dicc_productos = {p["codigo"]: p for p in productos}

# Conjuntos (set) con categorías únicas
categorias = {p["categoria"] for p in productos}

# print(dicc_productos)
print(categorias)