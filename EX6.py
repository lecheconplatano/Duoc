vehiculos = {
    "VH001": {
        "marca": "Toyota",
        "modelo": "Corolla",
        "año": 2018,
        "patente": "ABCD-12",
        "propietario": ["Juan Pérez", "12.345.678-9", "Santiago"]
    },
    "VH002": {
        "marca": "Ford",
        "modelo": "Focus",
        "año": 2020,
        "patente": "XYZ-987",
        "propietario": ["María López", "11.222.333-4", "Valparaíso"]
    }
}

def agregar():
    marca = input("Ingrese la marca de su vehículo: ")
    modelo = input("Ingrese el modelo de su vehículo: ")
    año = int(input("Ingrese el año de su vehículo (entre 1980 y 2025): "))
    if año >=1980 and año <=2025:
        patente = input("Ingrese su patente (4 letras y 2 digitos): ")
        letras = patente[:4]
        digitos = patente[4:]
        if len(patente)==6 and letras.isalpha() and digitos.isdigit():
            print("Patente correcta")
            nombre_propietario = input("Ingrese el nombre del propietario: ")
            rut = input("Ingrese el rut del propietario: ")
            ciudad = input("Ingrese la ciudad del propietario: ")
            vehiculo = {
                "marca":marca,
                "modelo":modelo,
                "año":año,
                "patente":patente,
                "propietario":[nombre_propietario,rut,ciudad]
            }
            ID = input("ID del vehiculo: ")
            vehiculos.update({ID:vehiculo})
        else:
            print("Patente incorrecta, ingrese 4 letras y 2 digitos")
            return
    else:
        print("Año del vehículo fuera del rango")
        return
    
def mostrar():
    for id,valor in vehiculos.items():
        print(f"El {id} : {valor["propietario"]}")        

def buscar_patente():
    patente = input("ingrese la patente que desea buscar: ")
    for clave,valor in vehiculos.items():
        if patente in valor["patente"]:
            print(valor["propietario"])
            break
    else:
        print("Patente no encontrada en la base de datos")

def listar_ciudad():
    ciudad = input("ingrese la ciudad a buscar: ")
    encontrados = False
    for clave,valor in vehiculos.items():
        if ciudad == valor["propietario"][2]:
            encontrados = True
            print(f"ID: {clave}, Marca: {valor['marca']}, Modelo: {valor['modelo']}, Año: {valor['año']}, Patente: {valor['patente']}, Propietario: {valor['propietario'][0]}")
    if encontrados == False:        
        print("no se encontro la ciudad en la base de datos")

def listar_año():
    while True:
        try:
            año = int(input("Ingrese el año del vehículo: "))
            break
        except(ValueError):
            print("Ingresa un valor numérico")
    encontrado = False
    for clave,valor in vehiculos.items():
        if año == valor["año"]:
            print(f"ID: {clave}, Marca: {valor['marca']}, Modelo: {valor['modelo']}, Año: {valor['año']}, Patente: {valor['patente']}, Propietario: {valor['propietario'][0]}")
            encontrado = True
    if encontrado == False:
        print("No se ha encontrado un auto de ese año")

def salir():
    print("Gracias por visitarnos")
    exit()

def menu():
    print("1. Agregar vehículo")
    print("2. Buscar vehículo por patente")
    print("3. Listar todos los vehículos de una ciudad específica")
    print("4. Listar vehículos por año")
    print("5. Mostrar todos los vehículos registrados")
    print("6. Salir del programa")

while True:
    menu()
    opc = input("Ingrese opcion: ")
    if opc == "1":
        agregar()
    elif opc == "2":
        buscar_patente()
    elif opc == "3":
        listar_ciudad()
    elif opc == "4":
        listar_año()
    elif opc == "5":
        mostrar()
    elif opc == "6":
        salir()
    else:
        print("opcion seleccionada incorrecta")