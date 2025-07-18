# lista de ventas boletas
ventas = [
    {"nro_boleta": 2001, "fecha": "22/04/2020", "cliente": "Camila Soto", "total": 0},
    {"nro_boleta": 2002, "fecha": "09/05/2022", "cliente": "Esteban Ríos", "total": 0},
    {"nro_boleta": 2003, "fecha": "22/05/2020", "cliente": "Daniela Herrera", "total": 0},
    {"nro_boleta": 2004, "fecha": "24/10/2024", "cliente": "Felipe Contreras", "total": 0},
    {"nro_boleta": 2005, "fecha": "24/07/2020", "cliente": "Valentina Campos", "total": 0},
    {"nro_boleta": 2006, "fecha": "21/04/2020", "cliente": "Javiera Morales", "total": 0},
    {"nro_boleta": 2007, "fecha": "19/07/2021", "cliente": "Carlos Silva", "total": 0},
    {"nro_boleta": 2008, "fecha": "22/03/2025", "cliente": "Francisca Reyes", "total": 0},
    {"nro_boleta": 2009, "fecha": "14/07/2025", "cliente": "Ignacio Ruiz", "total": 0},
    {"nro_boleta": 2010, "fecha": "31/08/2022", "cliente": "Laura Tapia", "total": 0},
]

# detalle de productos vendidos
detalle_ventas = [
    {"nro_boleta": 2001, "producto": "Harina", "cantidad": 1, "precio_unitario": 1200},
    {"nro_boleta": 2001, "producto": "Leche", "cantidad": 2, "precio_unitario": 1100},
    {"nro_boleta": 2001, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},

    {"nro_boleta": 2002, "producto": "Pan", "cantidad": 3, "precio_unitario": 800},
    {"nro_boleta": 2002, "producto": "Mantequilla", "cantidad": 1, "precio_unitario": 1800},

    {"nro_boleta": 2003, "producto": "Arroz", "cantidad": 2, "precio_unitario": 1800},
    {"nro_boleta": 2003, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},

    {"nro_boleta": 2004, "producto": "Fideos", "cantidad": 3, "precio_unitario": 900},
    {"nro_boleta": 2004, "producto": "Salsa", "cantidad": 2, "precio_unitario": 1300},

    {"nro_boleta": 2005, "producto": "Aceite", "cantidad": 1, "precio_unitario": 3200},
    {"nro_boleta": 2005, "producto": "Jugo", "cantidad": 2, "precio_unitario": 1400},

    {"nro_boleta": 2006, "producto": "Pan", "cantidad": 1, "precio_unitario": 800},
    {"nro_boleta": 2006, "producto": "Sal", "cantidad": 1, "precio_unitario": 600},
    {"nro_boleta": 2006, "producto": "Azúcar", "cantidad": 2, "precio_unitario": 1200},

    {"nro_boleta": 2007, "producto": "Leche", "cantidad": 2, "precio_unitario": 1100},
    {"nro_boleta": 2007, "producto": "Café", "cantidad": 1, "precio_unitario": 2500},

    {"nro_boleta": 2008, "producto": "Galletas", "cantidad": 2, "precio_unitario": 1600},
    {"nro_boleta": 2008, "producto": "Jugo", "cantidad": 1, "precio_unitario": 1400},

    {"nro_boleta": 2009, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},
    {"nro_boleta": 2009, "producto": "Mantequilla", "cantidad": 1, "precio_unitario": 1800},
    {"nro_boleta": 2009, "producto": "Pan", "cantidad": 2, "precio_unitario": 800},

    {"nro_boleta": 2010, "producto": "Café", "cantidad": 1, "precio_unitario": 2500},
    {"nro_boleta": 2010, "producto": "Leche", "cantidad": 1, "precio_unitario": 1100},
]
# Funciones
def total_boleta():
    for venta in ventas: # Recorre cada numero de boleta para ser evaluado en los detalles de venta
        nro = venta["nro_boleta"] # Es el numero de boleta
        total = 0
        for detalle in detalle_ventas: # recorremos el numero de boleta en cada detalle de venta para actualizar los valores correspondientes
            if detalle["nro_boleta"] == nro: 
                subtotal = detalle["cantidad"] * detalle["precio_unitario"] #subtotal de cada boleta con venta correspondiente
                total += subtotal
        venta["total"] = total  # Actualiza el total en la boleta
    print("Detalles actualizados exitosamente")

def cliente():
    cliente = input("Ingrese el nombre del cliente: ")
    info = []
    for venta in ventas:
        if venta["cliente"] == cliente:
            num = venta["nro_boleta"]
            for detalle in detalle_ventas:
                if detalle["nro_boleta"]==num:
                    info.append(detalle["producto"])
    print(f"Productos Comprados por {cliente}")
    print(f"Productos : {info}")

def boleta_fecha(fecha):
    for venta in ventas:
        if venta["fecha"] == fecha:
            print("======================")
            print("----DATOS CLIENTE----")
            print("======================")
            print(f"Nombre {venta["cliente"]}")
            print(f"boleta {venta["nro_boleta"]}")
            for detalle in detalle_ventas:
                if detalle["nro_boleta"] == venta["nro_boleta"]:
                    print(f"Productos {detalle["producto"]} || Cantidad {detalle["cantidad"]} || Precio unitario {detalle["precio_unitario"]}")

def listar_masvendidos():
    productos = []
    for detalle in detalle_ventas:
        producto = detalle["producto"]
        productos.append(producto)
    print(productos)


#Menu Principal
while True:
    print("============================")
    print("Menu Supermercado DUMBO")
    print("============================")
    print("1. Calcular el total de cada boleta a partir del detalle de productos.")
    print("2. Mostrar los productos comprados por un cliente específico.")
    print("3. Obtener la boleta con el total más alto y más bajo.")
    print("4. Filtrar las compras por fecha específica.")
    print("5. Listar los productos más vendidos en general.")
    print("6. Salir")
    opc = input("Ingrese opcion: ")
    if opc == "1":
        total_boleta()
    elif opc == "2":
        cliente()
    elif opc == "3":
        print("opc3")
    elif opc == "4":
        fecha = input("Ingrese la fecha con formato: ")
        boleta_fecha(fecha)
    elif opc == "5":
        listar_masvendidos()
    elif opc == "6":
        print("Gracias por preferirnos")
        break
    else:
        print("Opcion ingresada incorrecta")