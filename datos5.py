estudiantes = [
    {"nombre":"ariel", "rut": "221694120", "carrera": "informatica", "notas": []},
    ]

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    rut = input("Ingrese el rut del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
    notas = []
    estudiante = {"nombre":nombre, "rut":rut, "carrera": carrera, "notas": notas}
    estudiantes.append(estudiante)
    print("Estudiante agregado con EXITO!!")
    print(estudiantes)

def agregar_nota(estudiante):
    for estudiante in estudiantes:
        if estudiante not in estudiantes:
            print("No se encontro el estudiante en nuestro listado")
        else:
            try:
                nota = float(input("Ingrese la nota a agregar: "))
                estudiante["notas"].append(nota)
            except ValueError:
                print("Debes ingresar una nota correcta")

def prom_estudiante(est):
    for estudiante in estudiantes:
        if est == estudiante["nombre"]:
            try:
                if len(estudiante["notas"]) == 0:
                    print("No hay notas regisreadas")
                else:
                    prom = sum(estudiante["notas"])/len(estudiante["notas"])
                    print(f"EL promedio del estudiante {estudiante["nombre"]} es de {prom}")
            except ValueError:
                print("No hay notas registradas")
def mostrar_aprobados():
    aprobados = []
    for estudiante in estudiantes:
        prom = sum(estudiante["notas"])/len(estudiante["notas"])
        if prom > 4.0:
            aprobados.append(estudiante["nombre"])
    print(aprobados)
while True:
    print("""    1. Agregar estudiante
    2. Agregar nota a un estudiante
    3. Ver promedio de un estudiante
    4. Mostrar todos los estudiantes aprobados (promedio ≥ 4.0)
    5. Salir""")
    opc = input("Ingrese alguna opción: ")
    if opc == "1":
        agregar_estudiante()
    elif opc == "2":
        agregar_nota("ariel")
    elif opc == "3":
        est = input("Ingrese el nombre del estudiante: ")
        prom_estudiante(est)
