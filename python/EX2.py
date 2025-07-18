# Crea un programa en Python para registrar información básica de estudiantes. 
# Los datos se guardarán en un diccionario donde la clave será el número de identificación del
# estudiante (un número entero) y el valor será una lista con el nombre y la edad del estudiante

estudiantes = {
    101: ["Ana López", 18],
    102: ["Juan Pérez", 19],
    103: ["María García", 20]
}
def registro():
    estudiante = {}
    ID = int(input("Numero de identificacion: "))
    if ID in estudiantes:
        print("Ya existe un estudiante con este ID")
        return
    else:
        nombre = input("Ingrese Nombre: ")
        edad = int(input("Ingrese Edad"))
        estudiante[ID]=[nombre,edad]
        estudiantes.update(estudiante)
        

def informacion():
    ID = int(input("Ingrese ID de estudiante: "))
    if ID in estudiantes:
        estudiante = (estudiantes[ID])
        print(f"nombre: {estudiante[0]} || edad: {estudiante[1]}")
    else:
        print("Estudiante no encontrado")

def eliminar():
    ID = int(input("Numero de identificacion: "))
    if ID in estudiantes:
        del estudiantes[ID]
        
while True: 
    print("=== Menú Principal ===")
    print("1. Registrar estudiante")
    print("2. Ver información de estudiante")
    print("3. Eliminar estudiante")
    print("4. Salir")

    opcion = input("Ingrese opcion: ")
    if opcion == "1":
        registro()
    elif opcion == "2":
        informacion()
    elif opcion == "3":
        eliminar()
    elif opcion == "4":
        print("¡Programa de estudiantes finalizado!")
        break
