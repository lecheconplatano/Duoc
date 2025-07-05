boletas = [
   {"numero": 1001, "fecha": "01/07/2025", "cliente": "Juan Pérez", "total": 0},
   {"numero": 1002, "fecha": "02/07/2025", "cliente": "María López", "total": 0},
   {"numero": 1003, "fecha": "03/07/2025", "cliente": "Carlos Soto", "total": 0},
   {"numero": 1004, "fecha": "04/07/2025", "cliente": "Ana Torres", "total": 0},
   {"numero": 1005, "fecha": "05/07/2025", "cliente": "Pedro Rojas", "total": 0}, 
   {"numero": 1006, "fecha": "06/07/2025", "cliente": "Laura Díaz", "total": 0},
   {"numero": 1007, "fecha": "07/07/2025", "cliente": "Felipe Gutiérrez", "total": 0},
   {"numero": 1008, "fecha": "08/07/2025", "cliente": "Sofía Morales", "total": 0},
   {"numero": 1009, "fecha": "09/07/2025", "cliente": "Andrés Bravo", "total": 0},
   {"numero": 1010, "fecha": "10/07/2025", "cliente": "Gabriela Méndez", "total": 0},
]


detalle = [
# Boleta 1001
{"numero_boleta": 1001, "producto": "Leche", "cantidad": 2, "precio_unitario": 1200},
{"numero_boleta": 1001, "producto": "Pan", "cantidad": 1, "precio_unitario": 1500},
{"numero_boleta": 1001, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},

# Boleta 1002
{"numero_boleta": 1002, "producto": "Arroz", "cantidad": 1, "precio_unitario": 1800},
{"numero_boleta": 1002, "producto": "Fideos", "cantidad": 2, "precio_unitario": 900},

# Boleta 1003
{"numero_boleta": 1003, "producto": "Aceite", "cantidad": 1, "precio_unitario": 3000},
{"numero_boleta": 1003, "producto": "Azúcar", "cantidad": 1, "precio_unitario": 1500},
{"numero_boleta": 1003, "producto": "Café", "cantidad": 1, "precio_unitario": 2500},

# Boleta 1004
{"numero_boleta": 1004, "producto": "Pan", "cantidad": 2, "precio_unitario": 1500},
{"numero_boleta": 1004, "producto": "Sal", "cantidad": 1, "precio_unitario": 800},

# Boleta 1005
{"numero_boleta": 1005, "producto": "Jugo", "cantidad": 2, "precio_unitario": 1200},
{"numero_boleta": 1005, "producto": "Leche", "cantidad": 1, "precio_unitario": 1200},
{"numero_boleta": 1005, "producto": "Arroz", "cantidad": 1, "precio_unitario": 1800},

# Boleta 1006
{"numero_boleta": 1006, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},
{"numero_boleta": 1006, "producto": "Café", "cantidad": 1, "precio_unitario": 2500},

# Boleta 1007
{"numero_boleta": 1007, "producto": "Azúcar", "cantidad": 1, "precio_unitario": 1500},
{"numero_boleta": 1007, "producto": "Fideos", "cantidad": 2, "precio_unitario": 900},

# Boleta 1008
{"numero_boleta": 1008, "producto": "Pan", "cantidad": 1, "precio_unitario": 1500},
{"numero_boleta": 1008, "producto": "Sal", "cantidad": 1, "precio_unitario": 800},
{"numero_boleta": 1008, "producto": "Aceite", "cantidad": 1, "precio_unitario": 3000},
{"numero_boleta": 1008, "producto": "Jugo", "cantidad": 1, "precio_unitario": 1200},

# Boleta 1009
{"numero_boleta": 1009, "producto": "Leche", "cantidad": 2, "precio_unitario": 1200},
{"numero_boleta": 1009, "producto": "Huevos", "cantidad": 1, "precio_unitario": 2500},
{"numero_boleta": 1009, "producto": "Arroz", "cantidad": 1, "precio_unitario": 1800},

# Boleta 1010
{"numero_boleta": 1010, "producto": "Fideos", "cantidad": 2, "precio_unitario": 900},
{"numero_boleta": 1010, "producto": "Café", "cantidad": 1, "precio_unitario": 2500},
]

def agregar_producto(num_boleta, producto, cantidad, precio_unitario):   
    listado = ['Leche', 'Pan', 'Huevos', 'Arroz', 'Fideos', 'Aceite', 'Azúcar', 'Café', 'Sal', 'Jugo']
    existe = False
    for boleta in boletas:
        if boleta["numero"] == num_boleta:
            existe = True
            break

    if existe == True:
        if producto in listado and cantidad > 0:
            detalle.append({
                "numero_boleta": num_boleta,
                "producto": producto,
                "cantidad": cantidad,
                "precio_unitario": precio_unitario
            })
            print("Producto agregado correctamente.")
        else:
            print("Información ingresada incorrecta.")
    else:
        print("No se encuentra esa boleta en el registro.")


def total_mes():
    mes = input("Ingrese el mes de busqueda: ")
    año = input("Ingrese el año de busqueda: ")
    total = 0
    for boleta in boletas:
        fecha = boleta["fecha"]
        if mes == fecha[3:5] and año == fecha[6:]:
            total += boleta["total"]
    print(f"Total vendido en {mes}/{año}: ${total}")

def mostrar_boleta():
    busqueda = int(input("Ingrese el número de boleta: "))
    encontrado = False
    for boleta in boletas:
        if boleta["numero"] == busqueda:
            encontrado = True
            print("==========================")
            print(f"Boleta N° {boleta['numero']}")
            print("==========================")
            print(f"Fecha: {boleta['fecha']}")
            print(f"Cliente: {boleta['cliente']}")
            print("==========================")
            print("Detalles de Compra del cliente")
            print("==========================")
            
            total = 0
            for item in detalle:
                if item["numero_boleta"] == busqueda:
                    subtotal = item["cantidad"] * item["precio_unitario"]
                    total += subtotal
                    print(f"{item['producto']} | Cantidad: {item['cantidad']} | Precio: ${item['precio_unitario']} | Subtotal: ${subtotal}")
            print(f"Total: ${total}")
            break
    if encontrado == False:
        print("No se ha encontrado la boleta.")

def actualizar_valores():
    for boleta in boletas:
        total = 0
        for item in detalle:
            if item["numero_boleta"] == boleta["numero"]:
                total += item["cantidad"] * item["precio_unitario"]
    print("Los valores han sido actualizados de forma correcta")

while True:
    print("MENÚ PRINCIPAL SUPERMERCADO DUMBO")
    print("====================================")
    print("1. Total vendido en un mes y año en particular.")
    print("2. Información de una boleta específica, incluyendo su detalle.")
    print("3. Agregar uno o más productos a una boleta.")
    print("4. Actualizar el total de todas las boletas.")
    print("5. Salir.")

    opc = input("ingrese alguna opcion: ")
    if opc == "1":
        total_mes()
    elif opc == "2":
        mostrar_boleta()
    elif opc == "3":
        num_boleta = int(input("Ingrese el número de boleta: "))
        producto = input("Ingrese el tipo de producto: ").capitalize()
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio_unitario = int(input("Ingrese el precio unitario del producto: "))
        agregar_producto(num_boleta, producto, cantidad, precio_unitario)

    elif opc == "4":
        actualizar_valores()
    elif opc == "5":
        print("Gracias por visitar Jumbo")
        break
        
