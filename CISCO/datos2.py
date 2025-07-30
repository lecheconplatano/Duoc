productos = [
    {"id": 1, "nombre": "Notebook", "categoria": "Tecnología", "precio": 750000, "stock": 12},
    {"id": 2, "nombre": "Silla Gamer", "categoria": "Muebles", "precio": 190000, "stock": 5},
    {"id": 3, "nombre": "Mouse", "categoria": "Tecnología", "precio": 25000, "stock": 30},
    {"id": 4, "nombre": "Escritorio", "categoria": "Muebles", "precio": 135000, "stock": 7},
    {"id": 5, "nombre": "Lámpara", "categoria": "Iluminación", "precio": 22000, "stock": 15},
    {"id": 6, "nombre": "Monitor", "categoria": "Tecnología", "precio": 180000, "stock": 10},
    {"id": 7, "nombre": "Teclado", "categoria": "Tecnología", "precio": 30000, "stock": 25},
]

def mostrar_stock():
    print("Estos son los productos que tiene menos de 10 en stock")
    for producto in productos:
        if producto["stock"] < 10:
            print(producto["nombre"])

def producto_mas_caro():
    lista_precios = []
    for producto in productos:
        lista_precios.append(producto["precio"])
    lista_precios.sort()
    for producto in productos:
        if producto["precio"]==lista_precios[-1]:
            print(f"Nombre: {producto["nombre"]}")
            print(f"Precio: {producto["precio"]}")

def stock_total_Tecnología():
    stock_t = 0
    for p in productos:
        if p["categoria"]=="Tecnología":
            stock_t += p["stock"]
    print(f"El stock total de la categoría tecnología es {stock_t}") 

def productos_entre():
    new_list = []
    for p in productos:
        if p["precio"] > 20000 and p["precio"] < 100000:
            new_list.append(p)
    print(new_list)


def busqueda(name):
    encontrados = False
    for p in productos:
        if name == p["nombre"]:
            encontrados = True
            print(f"EL precio es{p["precio"]}")
            print(f"El Stock es {p["stock"]}")
    if not encontrados:
        print("No se ha encontrado el producto")


while True:
    print("Menu de opciones TIENDA")
    print("1. Mostrar productos con menos de 10 de stock")
    print("2. Mostrar producto mas caro")
    print("3. Stock total de la categoría tecnología")
    print("4. Productos con precio entre $20.000 y $100.000")
    print("5. Buscar producto por nombre")
    print("6. Salir")
    opc = input("Ingrese alguna opcion: ")
    if opc == "1":
        mostrar_stock()
    elif opc == "2":
        producto_mas_caro()
    elif opc == "3":
        stock_total_Tecnología()
    elif opc == "4":
        productos_entre()
    elif opc == "5":
        name = input("Ingrese el nombre a buscar: ").capitalize()
        busqueda(name)
    else:
        print("Opcion ingresada incorrecta")