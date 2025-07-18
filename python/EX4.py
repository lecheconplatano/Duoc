# Crea un programa que permita gestionar estudiantes usando un diccionario de listas con las claves 
# "nombres", "edades" y "notas".
estudiantes = {}

def agregar():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    nota = int(input("Ingrese el promedio del estudiante: "))
    estudiantes[nombre]=[edad,nota]

def mostrar():
    for nombre,info in estudiantes.items():
        print(f"Nombre : {nombre} Edad :{info[0]} Nota :{info[1]}")

def eliminar():
    nombre_eliminar = input("Ingrese el nombre del alumno a eliminar: ")
    if nombre_eliminar in estudiantes:
        del estudiantes[nombre_eliminar]
    else:
        print("No se encuentra el estudiante")

def calcular():
    notas = []
    for nombre,info in estudiantes.items():
        nota=info[1]
        notas.append(nota)
    cont = len(notas)
    promedio = sum(notas)/cont
    print(f"El promedio de notas es de {promedio}")

while True:
    print("1. Agregar un estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Eliminar un estudiante por nombre")
    print("4. Calcular el promedio de notas")
    print("5. Salir")
    opc = input("Ingrese alguna opcion: ")
    if opc == "1":
        agregar()
    elif opc == "2":
        mostrar()
    elif opc == "3":
        eliminar()
    elif opc == "4":
        calcular()
    elif opc == "5":
        print("Gracias por visitar nuestro programa")
        exit()
    else:
        print("Opcion ingresada incorrecta")
        

