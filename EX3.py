# agregar_estudiante() → pide todos los datos por consola y los agrega al diccionario.
# buscar_por_ciudad() → solicita una ciudad y muestra todos los estudiantes que vivan allí.
# mostrar_todos() → muestra todos los estudiantes registrados.

estudiantes = {
    "ST001": {
        "nombre": "Carlos Ruiz",
        "edad": 22,
        "carrera": "Ingeniería",
        "ciudad": "Santiago"
    },
    "ST002": {
        "nombre": "Ana Torres",
        "edad": 20,
        "carrera": "Medicina",
        "ciudad": "Valparaíso"
    }
}
def generar_id(estudiantes):
    numero = len(estudiantes) + 1
    return f"ST{str(numero).zfill(3)}"  # Ej: ST001, ST002, etc.
    
def menu():
    print("Universidad Prehistoria Chile")
    print("1.- Agregar estudiante")
    print("2.- Buscar por ciudad")
    print("3.- Mostrar todos")
    print("4.- Salir")

def agregar_estudiante():
    nombre = input("ingrese el nombre del estudiante: ").capitalize()
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad >= 18:
                break
        except(ValueError):
            print("Debes ingresar un valor numerico mayor a 18")
    carrera = input("ingrese la carrera del estudiante: ").capitalize()
    ciudad = input("ingrese la ciudad del estudiante: ").capitalize()
    estudiante ={
        "nombre" : nombre,
        "edad" : edad,
        "carrera" : carrera,
        "ciudad" : ciudad
        }
    ID = generar_id(estudiantes)
    estudiantes.update({ID:estudiante})
    print("Estudiante agregado con éxito...")

def buscar_por_ciudad():
    ciudad = input("Filtro por ciudad: ")
    for clave,valor in estudiantes.items():
        if ciudad == valor["ciudad"]:
            print(f"nombre:{valor["nombre"]}; edad:{valor["edad"]}; carrera: {valor["carrera"]}; ciudad: {valor["ciudad"]}")

def listado():
    i = 1
    for clave,valor in estudiantes.items():
        print(f"Estudiante {i}; nombre:{valor["nombre"]}; edad:{valor["edad"]}; carrera: {valor["carrera"]}; ciudad: {valor["ciudad"]}")
        i+=1


while True:
    menu()
    opcion = input("Ingrese alguna opcion: ")
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        buscar_por_ciudad()
    elif opcion == "3":
        listado()
    else:
        print("Opcion ingresada incorrecta")
