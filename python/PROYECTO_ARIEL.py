from datetime import datetime

# Sistema de Gestión de Boletas de Supermercado
boletas = []

def agregarboleta(num,fecha,cliente,producto,precio):
    boleta = {"numero":num,"fecha":fecha,"cliente":cliente,"productos":[{"producto":producto,"precio_unitario":precio}]}
    boletas.append(boleta)

def mostrar_boletas():
    print("==================")
    print("-----Boletas-----")
    for b in boletas:
        print(f"Numero de boleta {b['numero']}")
        print(f"fecha {b["fecha"]}")
        print(f"cliente {b["cliente"]}")
        for prod in b["productos"]:
            print(f"productos {prod["producto"]}")
            print(f"precio unitario {prod["precio_unitario"]}")
            print("==================")

def busqueda(cliente):
    for b in boletas:
        if cliente == b["cliente"]:
            print(f"ID BOLETA {b["numero"]}")
            print(f"FECHA {b["fecha"]}")
            for p in b["productos"]:
                print(f"PRODUCTO {p["producto"]}")
                print(f"PRECIO ${p["precio_unitario"]}")

def salir():
    print("Gracias por preferirnos")
    exit()

def rango_fecha():
    f1 = input("ingrese el rango inferior (fecha)")
    f2 = input("Ingrese el rango superior (fecha)")
    try:
        fecha1 = datetime.strptime(f1,"%d-%m-%Y").date()
        fecha2 = datetime.strptime(f2,"%d-%m-%Y").date()
        print("Buscando entre boletas")
        for b in boletas:
            if fecha1 <= b["fecha"] <= fecha2:
                print(b["numero"])
    except ValueError:
        print("Fecha inválida. Debe tener formato dd/mm/yyyy y ser real.")

def boleta_cara():
    for b in boletas:
        mom = 0
        for p in b["productos"]:
            if p["precio_unitario"] >= mom:
                mom = b["precio_unitario"]
            else:
                p["precio_unitario"]
    print(f"la boleta con mayor valor es con {mom}")

while True:
    print("Bienvenido al sistema de gestión de boletas de supermercado.")
    print("1. Agregar Boleta")
    print("2. Mostrar Boletas Registradas")
    print("3. Buscar Boletas Por Cliente")
    print("4. Buscar Boletas Por Rango De Fecha")
    print("6. Salir")
    opc = input("Ingrese una opción: ")
    if opc == "1":
        try:
            num = int(input("Ingrese el num de boleta: "))
            if num > 1 and num not in boletas:
                fech_str = input("Ingrese la fecha: ")
                try:
                    fecha = datetime.strptime(fech_str, '%d-%m-%Y').date()
                    cliente = input("Ingrese su nombre: ")
                    producto = input("Ingrese el nombre del producto: ")
                    try:
                        precio = int(input("Ingrese el precio del producto: "))
                        if precio > 1:
                            agregarboleta(num,fecha,cliente,producto,precio)
                    except ValueError:
                        print("Ingrese un precio entero mayor a 1")
                except ValueError:
                    print("Fecha inválida. Debe tener formato dd/mm/yyyy y ser real.")
        except ValueError:
            print("Debes ingresar un valor entero positivo")
    elif opc == "2":
        mostrar_boletas()
    elif opc == "3":
        cliente = input("ingrese el nombre del cliente a buscar: ")
        busqueda(cliente)
    elif opc == "4":
        rango_fecha()
    elif opc == "5":
        boleta_cara()
    elif opc == "6":
        salir()
