ventas = [
    {"cliente": "Ana", "producto": "Leche", "precio": 1200, "categoria": "Lácteos"},
    {"cliente": "Luis", "producto": "Pan", "precio": 1000, "categoria": "Panadería"},
    {"cliente": "Ana", "producto": "Queso", "precio": 2500, "categoria": "Lácteos"},
    {"cliente": "Pedro", "producto": "Jugo", "precio": 1800, "categoria": "Bebidas"},
    {"cliente": "Luis", "producto": "Leche", "precio": 1200, "categoria": "Lácteos"},
    {"cliente": "Pedro", "producto": "Pan", "precio": 1000, "categoria": "Panadería"},
    {"cliente": "Ana", "producto": "Jugo", "precio": 1800, "categoria": "Bebidas"},
    {"cliente": "Luis", "producto": "Queso", "precio": 2500, "categoria": "Lácteos"},
    {"cliente": "Ana", "producto": "Pan", "precio": 1000, "categoria": "Panadería"},
]

"""
 Parte 1: Productos más vendidos
Queremos saber cuántas veces se vendió cada producto. Ejemplo de salida:
{
    "Leche": 2,
    "Pan": 3,
    "Queso": 2,
    "Jugo": 2
}
"""

"""
 Parte 2: Agrupar ventas por categoría
Ejemplo esperado:
{
    "Lácteos": [
        {"cliente": "Ana", "producto": "Leche", ...},
        {"cliente": "Ana", "producto": "Queso", ...},
        ...
    ],
    "Panadería": [...],
    "Bebidas": [...]
}
"""

def mas_vendidos():
    conteo = {}
    for venta in ventas:
        producto = venta["producto"]
        if producto in conteo:
            conteo[producto]+=1
        else:
            conteo[producto]=1
    print("Productos mas vendidos")
    for pro,val in conteo.items():
        print(f"{pro} con {val} ventas")

def ventas_categoria():
    categorias = {}
    for v in ventas:
        categoria = v["categoria"]
        if categoria not in categorias:
            categorias[categoria]=[]
        categorias[categoria].append(v)
    print(categorias)

ventas_categoria()