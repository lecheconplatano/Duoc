mascotas = []

def ingresar():
    tipo_mascota = ["Perro","Gato","Ave"]
    mascota = input("ingrese el nombre de la mascota: ")
    tipo = input("Ingrese el tipo de mascota: ").capitalize()
    if tipo not in tipo_mascota:
        print("Mascota no aceptada")
    else:   
        edad = int(input("Ingrese la edad de su mascota: "))
    nueva_mascota = {
        "Nombre de la mascota" : mascota,
        "Tipo de mascota" : tipo,
        "Edad" : edad
    }
    mascotas.append(nueva_mascota)

def buscar():
    nombre = input("ingrese el nombre de la mascota: ")
    for mascota in mascotas:
        if nombre in mascota["Nombre de la mascota"]:
            print(f"Mascota encontrada en la base de datos")
            print(f"Tipo de mascota {mascota["Tipo de mascota"]}")
            print(f"Edad {mascota["Edad"]} años")
        else:
            print("la mascota no se encuentra")

def eliminar():
    nombre = input("ingrese el nombre de la mascota: ")
    for mascota in mascotas:
        if nombre in mascota["Nombre de la mascota"]:
            mascotas.remove(mascota)  
            print("¡Mascota eliminada!")  
        else:
            print("No se pudo eliminar la mascota")

while True:
    print("=====================")
    print("TIENDA DE MASCOTAS")
    print("=====================")
    print("1. Ingresar mascota") 
    print("2. Buscar mascota") 
    print("3. Eliminar mascota") 
    print("4. Salir")
    opc = input("ingrese alguna opcion: ")
    if opc == "1":
        ingresar()
    elif opc == "2":
        buscar()
    elif opc == "3":
        eliminar()
    elif opc == "4":
        print("gracias por visitar nuestra tienda de animalitos")
        total_mascotas = len(mascotas)
        print(f"Cantidad total de mascotas registradas : {total_mascotas}")
        exit()
