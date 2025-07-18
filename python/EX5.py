
cursos = {
    "CS101": {
        "nombre": "Programación I",
        "profesor": "Dra. Soto",
        "inscritos": 3,
        "estudiantes": ["Ana", "Luis", "Pedro"],
        "estado": "abierto"
    },
    "CS102": {
        "nombre": "Estructuras de Datos",
        "profesor": "Sr. Gómez",
        "inscritos": 2,
        "estudiantes": ["Camila", "Esteban"],
        "estado": "cerrado"
    }
}

def generar_id_curso(cursos):
    numero = len(cursos) + 1
    return f"CS{str(numero).zfill(3)}"  # Ejemplo: CS001, CS002, ...

def agregar_curso():
    ramo = input("Ingrese el nombre del ramo: ")
    profesor = input("Ingrese el nombre del profesor del ramo: ")
    while True:
        try:
            inscritos = int(input("Ingrese cupos del ramo: "))
            if inscritos >= 1:
                break
        except(ValueError):
            print("Debes ingresar un valor mayor o igual 1")
    estudiantes = []
    estado = input("Ingrese el estado del ramo (Abierto-Cerrado)").lower()
    if estado in ["abierto","cerrado"]:
        nuevo = {"nombre": ramo,
                "profesor" : profesor,
                "inscritos": inscritos,
                "estudiantes": estudiantes,
                "estado": estado}
        ID = generar_id_curso(cursos)
        cursos.update({ID:nuevo})
    else:
        print("Valor ingresado incorrecto")

def inscribir_estudiante():
    nombre = input("ingrese su nombre para la inscripcion: ")
    for clave,valor in cursos.items():
        pass
    if nombre in valor["nombre"]:
        print("Ya se encuentra ese alumno")
    else:
        if valor["estado"]=="Cerrado":
            print("Grupo Lleno")
        else:
            valor["estudiantes"].append(nombre)

def mostrar_estudiantes():
    for clave,valor in cursos.items():
        print(f"\nCurso {clave} - {valor['nombre']}")
        print(f"Profesor: {valor['profesor']}")
        print(f"Inscritos: {len(valor['estudiantes'])}/{valor['inscritos']}")
        print("Estudiantes:", ", ".join(valor["estudiantes"]) if valor["estudiantes"] else "Ninguno")
        print(f"Estado: {valor['estado'].capitalize()}")

def cerrar_curso():
    Cursos_actuales = []
    for curso in cursos:
        Cursos_actuales.append(curso)
    print(f"Cursos Actuales: {Cursos_actuales}")
    ID = input("Ingrese el id del curso: ")
    for clave,valor in cursos.items():
        if cursos[ID]:
            if valor["estado"]=="cerrado":
                print("Ese curso ya está cerrado")
            else:
                valor["estado"]="cerrado"
                print(f"El curso {clave} ha sido cerrado exitosamente.")
        else:
            print("no se encuentra el ID del curso en la base de datos")

while True:
    print("Base de Datos Diego Portales")
    print("1. Agregar curso")
    print("2. Inscribir_estudiante")
    print("3. Mostrar Estudiantes")
    print("4. Cerrar Curso")
    print("5. Salir")
    opc = input("Ingrese alguna opcion: ")
    if opc == "1":
        agregar_curso()
    elif opc == "2":
        inscribir_estudiante()
    elif opc == "3":
        mostrar_estudiantes()
    elif opc == "4":
        cerrar_curso()
    elif opc == "5":
        break
    else:
        print("Opcion ingresada incorrecta")

