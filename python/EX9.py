estudiantes = []

def agregar(nom,edad,nota):
    estudiante = {"nombre":nom,"edad":edad,"nota":nota}
    estudiantes.append(estudiante)

def analisis():
    aprobados = 0
    for estudiante in estudiantes:
        if estudiante["nota"] >= 4.0:
            aprobados += 1
    return aprobados

def resumen_estadistico():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    total_notas = 0
    nota_max = -1
    nota_min = 8
    destacado = 0
    mejor_estudiante = ""
    peor_estudiante = ""

    for est in estudiantes:
        nota = est["nota"]
        total_notas += nota

        if nota > nota_max:
            nota_max = nota
            mejor_estudiante = est["nombre"]

        if nota < nota_min:
            nota_min = nota
            peor_estudiante = est["nombre"]

        if nota >= 6.0:
            destacado += 1

    promedio = total_notas / len(estudiantes)

    print("\n----- Resumen Estadístico -----")
    print(f"Promedio general de notas: {promedio:.2f}")
    print(f"Mejor estudiante: {mejor_estudiante} con nota {nota_max}")
    print(f"Peor estudiante: {peor_estudiante} con nota {nota_min}")
    print(f"Estudiantes destacados (nota ≥ 6.0): {destacado}")
    print("--------------------------------")

        

while True:
    print("Bienvenido al ingreso de estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Contar aprobados")
    print("4. Salir")
    print("5. Resumen Estadístico")
    opc = input("Ingrese alguna opcion: ")
    if opc == "1":
        nom = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        nota = float(input("Ingrese la nota final: "))
        agregar(nom,edad,nota)
    elif opc == "2":
        for estudiante in estudiantes:
            print(f"Nombre:{estudiante["nombre"]} || Edad:{estudiante["edad"]} || Nota:{estudiante["nota"]}")
    elif opc == "3":
        aprobados = analisis()
        print(f"Cantidad de aprobados: {aprobados}")
    elif opc == "4":
        print("Gracias por preferirnos")
        break
    elif opc == "5":
        resumen_estadistico()
    else:
        print("Opcion ingresada incorrecta")