ventas = [
    {"id": 1, "cliente": "Juan Pérez", "producto": "Notebook", "categoria": "Tecnología", "precio": 750000, "cantidad": 1},
    {"id": 2, "cliente": "Ana Torres", "producto": "Mouse", "categoria": "Tecnología", "precio": 25000, "cantidad": 2},
    {"id": 3, "cliente": "Luis Soto", "producto": "Lámpara", "categoria": "Iluminación", "precio": 22000, "cantidad": 3},
    {"id": 4, "cliente": "María López", "producto": "Silla Gamer", "categoria": "Muebles", "precio": 190000, "cantidad": 1},
    {"id": 5, "cliente": "Tomás Díaz", "producto": "Teclado", "categoria": "Tecnología", "precio": 30000, "cantidad": 2},
    {"id": 6, "cliente": "Camila Rojas", "producto": "Escritorio", "categoria": "Muebles", "precio": 135000, "cantidad": 1},
    {"id": 7, "cliente": "Javiera Ríos", "producto": "Monitor", "categoria": "Tecnología", "precio": 180000, "cantidad": 2},
    {"id": 8, "cliente": "Carlos Sáez", "producto": "Notebook", "categoria": "Tecnología", "precio": 750000, "cantidad": 1},
    {"id": 9, "cliente": "Fernanda Herrera", "producto": "Mouse", "categoria": "Tecnología", "precio": 25000, "cantidad": 1},
    {"id": 10, "cliente": "Ignacio Pino", "producto": "Lámpara", "categoria": "Iluminación", "precio": 22000, "cantidad": 4},
    {"id": 11, "cliente": "Sofía Mena", "producto": "Silla Gamer", "categoria": "Muebles", "precio": 190000, "cantidad": 1},
    {"id": 12, "cliente": "Gabriel Álvarez", "producto": "Teclado", "categoria": "Tecnología", "precio": 30000, "cantidad": 3},
    {"id": 13, "cliente": "Valentina Figueroa", "producto": "Escritorio", "categoria": "Muebles", "precio": 135000, "cantidad": 1},
    {"id": 14, "cliente": "Nicolás Peña", "producto": "Monitor", "categoria": "Tecnología", "precio": 180000, "cantidad": 1},
    {"id": 15, "cliente": "Paula Núñez", "producto": "Notebook", "categoria": "Tecnología", "precio": 750000, "cantidad": 1}
]

# total_ventas_cliente(nombre)
# → Muestra el total gastado por un cliente en todas sus compras.

# producto_mas_vendido()
# → Muestra qué producto se vendió más veces (sumando las cantidades).

# ventas_por_categoria()
# → Muestra cuántas unidades se vendieron por cada categoría.

# venta_mayor()
# → Muestra los datos de la venta de mayor valor (precio * cantidad).

# buscar_producto(nombre)
# → Muestra todas las ventas de ese producto.

# menu interactivo con opciones para probar lo anterior.

def total_ventas_cliente(nombre):
    total = 0
    for v in ventas:
        if v["cliente"].capitalize()==nombre:
            total = v["precio"]*v["cantidad"]
    print(f"El total gastado por el cliente {nombre} tiene un valor de ${total}")

def producto_mas_vendido():
    productos = {}
    for v in ventas:
        if v["producto"] not in productos:
            productos[v["producto"]]=v["cantidad"]
        else:
            productos[v["producto"]]+=v["cantidad"]

    producto_max = None
    max = 0
    for producto,cantidad in productos.items():
        if cantidad > max:
            max = cantidad
            producto_max = producto
    print(f"El producto mas vendido fue {producto_max} con {max} ventas")

def ventas_por_categoria():
    categorias = {}
    for v in ventas:
        if v["categoria"] not in categorias:
            categorias[v["categoria"]]=v["cantidad"]
        else:
            categorias[v["categoria"]]+=v["cantidad"]
    for categoria,ventas_t in categorias.items():
        print(f"La categoría {categoria} tiene {ventas_t} ventas")

def venta_mayor():
    v_mayor = ventas[0]["precio"] * ventas[0]["cantidad"]
    for v in ventas[1:]:
        valor = v["precio"] * v["cantidad"]
        if v_mayor < valor:
            v_mayor = valor
    print(f"La venta mayor fue de ${valor}")

def buscar_producto(nombre):
    ventas_totales = 0
    for v in ventas:
        if nombre == v["producto"].capitalize():
            ventas_totales += v["cantidad"]
    print(f"La cantidad todal de ventas de {nombre} fue de {ventas_totales} ventas")


while True:
    print("Bienvenido al servicio de ventas")
    print("1. Total gastado por cliente")
    print("2. Producto que más se vendió")
    print("3. Ventas por categoría")
    print("4. Venta de mayor valor")
    print("5. Ver venta de un producto")
    print("6. Salir")
    opc = input("Ingrese alguna opción: ")
    if opc == "1":
        nombre = input("Ingrese el nombre del cliente: ").capitalize()
        total_ventas_cliente(nombre)
    elif opc == "2":
        producto_mas_vendido()
    elif opc == "3":
        ventas_por_categoria()
    elif opc == "4":
        venta_mayor()
    elif opc == "5":
        nombre = input("Ingrese el nombre de producto: ").capitalize()
        buscar_producto(nombre)
    elif opc == "6":
        print("Programa finalizado...")
        break
    else:
        print("opción ingresada incorrecta")