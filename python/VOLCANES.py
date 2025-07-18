volcanes = {
    "Villarrica": ["Chile", 2847, 2020],
    "Llaima": ["Chile", 3125, 2009],
    "Osorno": ["Chile", 2652, 1835],
    "Calbuco": ["Chile", 2015, 2015],
    "Nevados de Chillán": ["Chile", 3212, 2022]
}

def registro():
    nombre = input("ingrese nombre: ").capitalize()
    pais = input("ingrese pais: ").capitalize()
    altura = int(input("Altura en metros"))
    erupcion = int(input("Año de última erupción"))
    volcanes[nombre] = [pais,altura,erupcion]

def buscar():
    nombre = input("ingrese nombre: ")
    if nombre in volcanes:
        print(volcanes[nombre])
    else:
        print("Volcán no encontrado")

def actualizar():
    nombre = input("ingrese nombre: ")
    if nombre in volcanes:
        pais = input("Ingrese su nuevo pais: ")
        altura = int(input("Ingrese su nueva altura en metros: "))
        erupcion = int(input("ingrese nuevo año de última erupción"))
        volcan = volcanes[nombre]
        volcan[0] = pais
        volcan[1] = altura
        volcan[2] = erupcion
    else:
        print("No se puede actualizar. Volcán no encontrado")

def eliminar():
    nombre = input("ingrese nombre del volcan a eliminar: ").capitalize()
    if nombre in volcanes:
        del volcanes[nombre]
        print("Volcán eliminado con éxito")
    else:
        print("No se pudo eliminar. Volcán no encontrado")

def mostrar():
    lista_volcanes = []
    for volcan in volcanes:
        lista_volcanes.append(volcan)
        lista_volcanes.sort
    print("Lista de volcanes")
    print(lista_volcanes)
    if lista_volcanes == []:
        print("No hay volcanes registrados")

def salir():
    lista_volcanes = []
    for volcan in volcanes:
        lista_volcanes.append(volcan)
    volcanes_registrados = len(lista_volcanes)
    print("Hasta luego compañero")
    print(f"cantidad total de volcanes registrados {volcanes_registrados}")
    exit()


while True:
    print("1. Registrar volcán")
    print("2. Buscar volcán")
    print("3. Actualizar volcán")
    print("4. Eliminar volcán")
    print("5. Mostrar todos los volcanes")
    print("6. Salir")
    opc = input("Ingrese opcion: ")
    if opc == "1":
        registro()
    elif opc == "2":
        buscar()
    elif opc == "3":
        actualizar()
    elif opc == "4":
        eliminar()
    elif opc == "5":
        mostrar()
    elif opc == "6":
        salir()
    else:
        print("Opcion ingresada incorrecta")