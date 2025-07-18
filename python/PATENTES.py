datos_vehiculos = {}

def ingresar():
    vehiculos = ["Auto", "Moto", "Camion"]
    patente = input("Ingrese la patente: ").upper()
    tipo = input("Ingrese el tipo de vehiculo: ").capitalize()
    while True:
        try:
            año = int(input("Ingrese el año de fabricacion: "))
            break
        except(ValueError):
            print("Debes elegir año entre 2007 y 2025")
    letras = patente[:4]
    digitos = patente[4:]
    if len(patente)==6 and letras.isalpha() and digitos.isdigit():
        if patente not in datos_vehiculos:
            print("Patente valida")
            if tipo in vehiculos:
                print("Vehículo válido")
                if año >=2007 and año <=2025:
                    print("Año de fabricacion correcta")
                    datos_vehiculos[patente]=[tipo,año]
                    print(datos_vehiculos)
                else:
                    print("Año de fabricacion incorrecta")
            else:
                print("Informacion no deseada")
        else:
            print("Patente ya se encuentra registrada")
    else:
        print("Patente Incorrecta")

def buscar():
    patente = input("ingrese patente para buscar en la base de datos: ").upper()
    letras = patente[:4]
    digitos = patente[4:]
    if len(patente)==6 and letras.isalpha() and digitos.isdigit():
        if patente in datos_vehiculos:
            print(f"DATOS OBTENIDOS: Vehículo | año fabricacion = {datos_vehiculos[patente]}")

def eliminar():
    patente = input("ingrese patente para buscar en la base de datos: ").upper()
    letras = patente[:4]
    digitos = patente[4:]
    if len(patente)==6 and letras.isalpha() and digitos.isdigit():
        if patente in datos_vehiculos:
            del datos_vehiculos[patente]
            print("¡Vehículo eliminado!")
        else:
            print("No se pudo eliminar el vehículo")

def mostrar():
    print(f"DATOS OBTENIDOS: Vehículo | año fabricacion = {datos_vehiculos}")

def cantidad_total():
    lista_vehiculos = []
    for vehiculo in datos_vehiculos:
        lista_vehiculos.append(vehiculo)
    contador = len(lista_vehiculos)
    print(f"El total de vehiculos inscritos fue de {contador}")

while True:
    print("===== MENU =====")
    print("1. Ingresar vehículo") 
    print("2. Buscar vehículo") 
    print("3. Eliminar vehículo") 
    print("4. Mostrar Vehículos")
    print("5. Salir")
    opc = input("Ingrese alguna opcion: ")
    if opc == "1":
        ingresar()
    elif opc == "2":
        buscar()
    elif opc == "3":
        eliminar()
    elif opc == "4":
        mostrar()
    elif opc == "5":
        cantidad_total()
    else:
        print("Opcion invalida")
