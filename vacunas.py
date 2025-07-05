# Crea un programa que permita registrar vacunas aplicadas a mascotas.
# Cada mascota tiene un nombre, especie (perro o gato)
# y un registro de vacunas que es un diccionario donde la clave es el nombre de la vacuna y el valor es la fecha en que se aplicó.
mascotas = {}

def agregar_mascota(mascotas, nombre, especie):
    if nombre in mascotas:
        print("La mascota ya se encuentra registrada")
    else:
        mascotas[nombre]={
            "especie" : especie.lower(),
            "vacunas" : {}
        }
        print(f"{nombre} ha sido registrada como un {especie}")

def registrar_vacuna(mascotas, nombre, vacuna, fecha):
    if nombre in mascotas:
        mascotas[nombre]["vacunas"][vacuna] = fecha
        print(f"vacuna {vacuna} registrada para {nombre} el {fecha}")
    else:
        print("mascota no encontrada")

def mostrar_mascotas(mascotas):
    if not mascotas:
        print("No se encuentran mascotas registradas")
    else:
        for nombre,datos in mascotas.items():
            print(f"nombre : {nombre}")
            for vacuna,fecha in datos["vacunas"].items():
                print(f"nombre : {nombre} || vacuna {vacuna}")



while True:
    print("1. Agregar mascota")
    print("2. Registrar vacuna")
    print("3. Mostrar mascotas")
    print("4. Salir")
    opc = input("ingrese alguna opcion: ")
    if opc == "1":
        nombre = input("ingrese el nombre: ")
        especie = input("Ingrese la especie: ")
        agregar_mascota(mascotas,nombre,especie)
    elif opc == "2":
        nombre = input("Ingrese el nombre de la mascota a buscar: ")
        vacuna = input("Ingrese el nombre de la vacuna: ")
        fecha = input("Ingrese la fecha de vacunacion: ")
        registrar_vacuna(mascotas, nombre, vacuna, fecha)
    elif opc == "3":
        mostrar_mascotas(mascotas)
    elif opc == "4":
        print("Gracias por visitar nuestra veterinaria")
        break