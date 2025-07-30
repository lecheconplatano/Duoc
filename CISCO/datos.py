personas = [
    {"id": 1, "nombre": "Ana", "edad": 23, "ciudad": "Santiago"},
    {"id": 2, "nombre": "Luis", "edad": 31, "ciudad": "Valparaíso"},
    {"id": 3, "nombre": "María", "edad": 27, "ciudad": "Santiago"},
    {"id": 4, "nombre": "Carlos", "edad": 35, "ciudad": "Concepción"},
    {"id": 5, "nombre": "Javiera", "edad": 19, "ciudad": "La Serena"},
    {"id": 6, "nombre": "Pedro", "edad": 40, "ciudad": "Santiago"},
    {"id": 7, "nombre": "Sofía", "edad": 28, "ciudad": "Valdivia"},
    {"id": 8, "nombre": "Tomás", "edad": 22, "ciudad": "Valparaíso"},
    {"id": 9, "nombre": "Camila", "edad": 33, "ciudad": "Santiago"},
    {"id": 10, "nombre": "Diego", "edad": 25, "ciudad": "Puerto Montt"},
]

def ciudad(city):
    for persona in personas:
        if persona["ciudad"]==city:
            print(persona["nombre"])

def edad(age):
    for persona in personas:
        if persona["edad"] > age:
            print(persona["nombre"])   

def personas_rango():
    edades = []
    for persona in personas:
        edades.append(persona["edad"])
    edades.sort()
    encontrados = False
    for persona in personas:
        if persona["edad"] == edades[0]:
            encontrados = True
            print(f"Esta es la persona con menos edad {persona["nombre"]} con {persona["edad"]} años")
        elif persona["edad"] == edades[-1]:
            encontrados = True
            print(f"Esta es la persona con mas edad {persona["nombre"]} con {persona["edad"]} años")
    if not encontrados:
        print("No se ha encontrado informacion")

def personas_por_ciudad():
    ciudades = {}
    for persona in personas:
        if persona["ciudad"] not in ciudades:
            ciudades[persona["ciudad"]]=0
    for persona in personas:
        for ciudad in ciudades:
            if persona["ciudad"]==ciudad:
                ciudades[persona["ciudad"]]+=1
    print(ciudades)

def busqueda(name):
    encontrados = False
    for persona in personas:
        if name in persona["nombre"]:
            encontrados = True
            print(f"Edad {persona["edad"]}")
            print(f"Ciudad {persona["ciudad"]}")
    if not encontrados:
        print("No se ha encontrado esa persona en la base de datos")

while True:
    print("Menu de opciones Ciudadanía")
    print("1. Busqueda de persona por ciudad")
    print("2. Búsqueda de persona por edad")
    print("3. Edad mas alta y baja")
    print("4. Cantidad de personas por ciudad")
    print("5. Buscar persona por nombre")
    print("6. Salir")
    opc = input("Ingrese alguna opcion: ")
    if opc == "1":
        city = input("Ingrese la ciudad de busqueda: ").capitalize()
        ciudad(city)
    elif opc == "2":
        age = int(input("Ingrese edad en adelante para la búsqueda: "))
        edad(age)
    elif opc == "3":
        personas_rango()
    elif opc == "4":
        personas_por_ciudad()
    elif opc == "5":
        name = input("Ingrese el nombre de la persona a buscar: ")
        busqueda(name)
    elif opc == "6":
        print("Gracias por probar nuestro servicio")
        break
    else:
        print("Opción ingresada incorrecta")