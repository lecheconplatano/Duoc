# El taller mecánico DUOMECÁNICO realiza mantenciones a vehículos de distinto tipo, registrando la información en dos diccionarios: vehiculos y mantenciones. Además de una lista de marcas.
# Diccionario de Vehículos
# Clave: Patente. Formada por 4 letras y 2 dígitos (ej. "ABCD12").
# Valor: Una lista con: marca, modelo, año de fabricación y tipo de vehículo.

mantenciones = {
10: {"patente": "ABCD12", "costo_total": 180000, "repuestos": ["Filtro de aceite", "Aceite", "Bujías"], "fecha": "05/01/2025"},
20: {"patente": "EFGH34", "costo_total": 250000, "repuestos": ["Pastillas de freno", "Aceite", "Filtro aire"], "fecha": "12/01/2025"},
30: {"patente": "IJKL56", "costo_total": 160000, "repuestos": ["Aceite", "Batería"], "fecha": "25/01/2025"},
40: {"patente": "MNOP78", "costo_total": 195000, "repuestos": ["Filtro de aceite", "Aceite", "Correa distribución"], "fecha": "04/02/2025"},
50: {"patente": "QRST90", "costo_total": 220000, "repuestos": ["Amortiguadores", "Filtro aire"], "fecha": "18/02/2025"},
60: {"patente": "UVWX11", "costo_total": 175000, "repuestos": ["Bujías", "Aceite", "Filtro de combustible"], "fecha": "01/03/2025"},
70: {"patente": "YZAB22", "costo_total": 280000, "repuestos": ["Pastillas de freno", "Aceite", "Radiador"], "fecha": "11/03/2025"},
80: {"patente": "CDEF33", "costo_total": 240000, "repuestos": ["Aceite", "Filtro aceite", "Filtro aire"], "fecha": "20/03/2025"},
90: {"patente": "GHIJ44", "costo_total": 170000, "repuestos": ["Aceite", "Bujías"], "fecha": "02/04/2025"},
100: {"patente": "KLMN55", "costo_total": 200000, "repuestos": ["Correa distribución", "Aceite", "Filtro aceite"], "fecha": "14/04/2025"},
110: {"patente": "ABCD12", "costo_total": 150000, "repuestos": ["Aceite", "Filtro aire"], "fecha": "29/04/2025"},
120: {"patente": "EFGH34", "costo_total": 230000, "repuestos": ["Aceite", "Radiador"], "fecha": "05/05/2025"},
130: {"patente": "IJKL56", "costo_total": 165000, "repuestos": ["Filtro aceite"], "fecha": "19/05/2025"},
140: {"patente": "YZAB22", "costo_total": 190000, "repuestos": [], "fecha": "01/06/2025"},
150: {"patente": "CDEF33", "costo_total": 210000, "repuestos": ["Bujías", "Aceite"], "fecha": "10/06/2025"},
160: {"patente": "EFGH34", "costo_total": 245000, "repuestos": ["Aceite", "Bujías", "Filtro aceite"], "fecha": "22/06/2025"},
170: {"patente": "GHIJ44", "costo_total": 180000, "repuestos": [], "fecha": "29/06/2025"},
180: {"patente": "ABCD12", "costo_total": 155000, "repuestos": ["Aceite", "Filtro combustible"], "fecha": "30/06/2025"},
190: {"patente": "MNOP78", "costo_total": 190000, "repuestos": ["Aceite", "Filtro aceite", "Filtro aire"], "fecha": "28/06/2025"},
200: {"patente": "UVWX11", "costo_total": 170000, "repuestos": ["Correa distribución", "Aceite"], "fecha": "27/06/2025"}
}

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

marcas=['Mazda', 'Chevrolet', 'Ford', 'Hyundai', 'Peugeot', 'Nissan', 'Kia', 'Volkswagen', 'Honda', 'Toyota']

#funciones
def info_veh(patente):      
    if patente not in vehiculos:
        print("Pantente no encontrada en el listado")
    else:
        print(f"Informacion de la patente {patente}")
        print(vehiculos[patente])

# 200: {"patente": "UVWX11", "costo_total": 170000, "repuestos": ["Correa distribución", "Aceite"], "fecha": "27/06/2025"}
def veh_man(patente):
    print(f"---Mantenciones Vehículo {patente}---")
    total = 0
    for id,datos in mantenciones.items():
        if patente in datos["patente"]:
            repuestos = datos["repuestos"]
            subtotal = datos["costo_total"]
            print(f"ID:{id} {repuestos} || ${subtotal}")
            total = total+subtotal
    print(f"Total final ${total}")

def total_repuestos():
    total = []
    for datos in mantenciones.values():
        repuestos = (datos["repuestos"])
        for repuesto in repuestos:
            total.append(repuesto)
    print("=======================")
    print(f"Total de repuestos {len(total)}")
    print("=======================")

def agregar_veh(patente,marca,modelo,año,tipo):
    if marca in marcas:
        if patente in vehiculos:
            print("Ya se encuentra usada esa patente")
        else:
            vehiculo={patente:[marca,modelo,año,tipo]}
            vehiculos.update(vehiculo)
            print(vehiculos)
    else:
        print("Ese modelo no esta en el listado")

# Programa principal
opc = "0"
while opc != "5":
    print("\n--- Menú principal taller mecánico ---")
    print("====================================")
    print("1. Total en $ de todas las mantenciones de un vehículo específico")
    print("2. Información de un vehículo específico y sus mantenciones")
    print("3. Cantidad total de repuestos X utilizados")
    print("4. Ingresar un vehículo nuevo (no se puede repetir la patente).")
    print("5. Salir")
    opc = input("Ingrese la opción: ")

    if opc == "1":
        patente = input("Ingrese la patente (ej, ABCD12): ").upper()
        veh_man(patente)
    elif opc == "2":
        patente = input("Ingrese la patente (ej, ABCD12): ").upper()
        info_veh(patente)
    elif opc == "3":
        total_repuestos()
    elif opc == "4":
        patente = input("Ingrese la patente (ej, ABCD12): ").upper()
        marca = input("ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        año = int(input("ingrese el año de fab: "))
        tipo = input("ingrese el tipo: ")
        agregar_veh(patente,marca,modelo,año,tipo)
    elif opc == "5":
        print("Gracias por visitarnos")