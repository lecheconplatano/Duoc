boletas = [
   {"numero": 1001, "fecha": "15/03/2025", "cliente": "Juan Pérez", "total": 0},
   {"numero": 1002, "fecha": "22/11/2025", "cliente": "María López", "total": 0},
   {"numero": 1003, "fecha": "08/05/2025", "cliente": "Carlos Soto", "total": 0},
   {"numero": 1004, "fecha": "30/09/2025", "cliente": "Ana Torres", "total": 0},
   {"numero": 1005, "fecha": "17/02/2025", "cliente": "Pedro Rojas", "total": 0}, 
   {"numero": 1006, "fecha": "04/12/2025", "cliente": "Laura Díaz", "total": 0},
   {"numero": 1007, "fecha": "11/08/2025", "cliente": "Felipe Gutiérrez", "total": 0},
   {"numero": 1008, "fecha": "25/06/2025", "cliente": "Sofía Morales", "total": 0},
   {"numero": 1009, "fecha": "19/04/2025", "cliente": "Andrés Bravo", "total": 0},
   {"numero": 1010, "fecha": "07/10/2025", "cliente": "Gabriela Méndez", "total": 0},
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

Productos=['Leche', 'Pan', 'Huevos', 'Arroz', 'Fideos', 'Aceite', 'Azúcar', 'Café', 'Sal', 'Jugo']

def imprimir_boleta(bol):
    print("========================")
    print(f"Numero {bol["numero"]}")
    print(f"Fecha {bol["fecha"]}")
    print(f"Cliente {bol["cliente"]}")
    print(f"Total {bol["total"]}")
    print("========================")

def info_boleta(numero):
    for bol in boletas:
        if bol["numero"] == numero:
            imprimir_boleta(bol)

def busqueda_fecha(dia,mes):
    encontrados = False
    for bol in boletas:
        fecha = bol["fecha"].split("/")
        if dia == fecha[0] and mes == fecha[1]:
                encontrados=True
                print("=================")
                print("Fecha encontrada")
                print("=================")
                print(bol["numero"])
                print(bol["fecha"])
                print(bol["cliente"])
                print(bol["total"])
    if not encontrados:
        print("Fecha no encontrada")

def agregar_producto(numero,producto,cantidad,precio_unitario):
    # {"numero_boleta": 1001, "producto": "Leche", "cantidad": 2, "precio_unitario": 1200}
    if producto in Productos and cantidad > 0 and precio_unitario > 0:
        detalle_compra = {
            "numero_boleta":numero,
            "producto":producto,
            "cantidad":cantidad,
            "precio_unitario":precio_unitario
        }            
        detalle.append(detalle_compra)
    else:
        print("Producto no encotrado en la lista oficial, o datos mal ingresados")

def actualizar_boleta():
    total = 0
    for boleta in boletas:
        for info in detalle:
            if boleta["numero"] == info["numero_boleta"]:
                subtotal = info["cantidad"] * info["precio_unitario"]
                total+=subtotal
                boleta["total"]=total
def salir():
    print("Gracias por preferirnos")
    exit()

while True:
    print("===================================")
    print("MENÚ PRINCIPAL SUPERMERCADO DUMBO")
    print("===================================")
    print("1. Total vendido en un mes y año en particular.") 
    print("2. Información de una boleta específica, incluyendo su detalle.") 
    print("3. Agregar uno o más productos a una boleta.") 
    print("4. Actualizar el total de todas las boletas.")
    print("5. Salir.")
    opc = input("ingrese alguna opcion: ")
    if opc == "1":
        dia = input("ingrese el dia a buscar: ").zfill(2)
        mes = input("ingrese el mes a buscar: ").zfill(2)
        busqueda_fecha(dia,mes)
    elif opc == "2":
        numero = int(input("ingrese el num para buscar la boleta: "))
        info_boleta(numero)
    elif opc == "3":
        numero = int(input("Ingrese un numero: "))
        producto = input("Ingrese un el tipo de producto: ")
        cantidad = int(input("Ingrese una cantidad: "))
        precio_unitario = int(input("Ingrese el precio unitario: "))
        agregar_producto(numero,producto,cantidad,precio_unitario)
    elif opc == "4":
        actualizar_boleta()
        print("Las boletas han sido actualizadas")
    elif opc == "5":
        salir()
    else:
        print("Opcion ingresada incorrecta")
