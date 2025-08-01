import pandas as pd

boletas = {
    "numero": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "fecha": [
        "01/07/2025", "01/07/2025", "02/07/2025", "02/07/2025", "03/07/2025",
        "03/07/2025", "04/07/2025", "04/07/2025", "05/07/2025", "05/07/2025"
    ],
    "cliente": ["Juan Pérez", "María López", "Carlos Díaz", "Ana Muñoz", "Pedro Rojas",
        "Laura Torres", "Miguel Vera", "Camila Soto", "Daniel Pino", "Sofía León"],
}

df = pd.DataFrame(boletas)

productos_por_boleta = {
    1001: [
        {"nombre": "Arroz", "cantidad": 2, "precio_unitario": 1500},
        {"nombre": "Leche", "cantidad": 3, "precio_unitario": 1000}
    ],
    1002: [
        {"nombre": "Pan", "cantidad": 4, "precio_unitario": 800},
        {"nombre": "Huevos", "cantidad": 1, "precio_unitario": 1200}
    ],
    1003: [
        {"nombre": "Azúcar", "cantidad": 1, "precio_unitario": 1100},
        {"nombre": "Café", "cantidad": 2, "precio_unitario": 2200},
        {"nombre": "Té", "cantidad": 1, "precio_unitario": 500}
    ],
    1004: [
        {"nombre": "Jugo", "cantidad": 2, "precio_unitario": 1200},
        {"nombre": "Agua", "cantidad": 2, "precio_unitario": 1100}
    ],
    1005: [
        {"nombre": "Aceite", "cantidad": 1, "precio_unitario": 2900},
        {"nombre": "Fideos", "cantidad": 3, "precio_unitario": 900}
    ],
    1006: [
        {"nombre": "Leche", "cantidad": 4, "precio_unitario": 1000},
        {"nombre": "Pan", "cantidad": 5, "precio_unitario": 800}
    ],
    1007: [
        {"nombre": "Yogur", "cantidad": 3, "precio_unitario": 850},
        {"nombre": "Cereal", "cantidad": 2, "precio_unitario": 2200}
    ],
    1008: [
        {"nombre": "Detergente", "cantidad": 1, "precio_unitario": 3200},
        {"nombre": "Esponja", "cantidad": 2, "precio_unitario": 800}
    ],
    1009: [
        {"nombre": "Carne", "cantidad": 2, "precio_unitario": 5000},
        {"nombre": "Papas", "cantidad": 4, "precio_unitario": 1000}
    ],
    1010: [
        {"nombre": "Galletas", "cantidad": 3, "precio_unitario": 900},
        {"nombre": "Jugo", "cantidad": 2, "precio_unitario": 1200}
    ]
}

#Menu Principal
while True:
    print("============================")
    print("Menu Supermercado DUMBO")
    print("============================")
    print("1. Ver todas las boletas registradas")
    print("2. Buscar boleta por número")
    print("3. Filtrar boletas por fecha")
    print("4. Agregar una nueva boleta")
    print("5. Calcular el total de una boleta")
    print("6. Salir del programa")
    opc = input("Ingrese opcion: ")
    if opc == "1":
        totales = []
        for numero in boletas["numero"]:
            productos = productos_por_boleta[numero]
            total_boleta = sum(p["cantidad"] * p["precio_unitario"] for p in productos)
            totales.append(total_boleta)
        boletas["total"] = totales

    df = pd.DataFrame(boletas)
    print(df.head())
