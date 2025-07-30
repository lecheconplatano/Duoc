empleados = [
    {"id": 1, "nombre": "Ana", "cargo": "Gerente", "sueldo": 1800000, "años_experiencia": 8},
    {"id": 2, "nombre": "Luis", "cargo": "Analista", "sueldo": 1200000, "años_experiencia": 4},
    {"id": 3, "nombre": "María", "cargo": "Desarrollador", "sueldo": 1500000, "años_experiencia": 6},
    {"id": 4, "nombre": "Carlos", "cargo": "Desarrollador", "sueldo": 1400000, "años_experiencia": 5},
    {"id": 5, "nombre": "Javiera", "cargo": "Analista", "sueldo": 1100000, "años_experiencia": 3},
    {"id": 6, "nombre": "Tomás", "cargo": "Desarrollador", "sueldo": 1600000, "años_experiencia": 7},
    {"id": 7, "nombre": "Camila", "cargo": "Gerente", "sueldo": 1900000, "años_experiencia": 9}
]
# buscar_empleado(nombre): Muestra el sueldo y cargo de un empleado si se encuentra por nombre.
# promedio_sueldo(cargo): Calcula y muestra el sueldo promedio de todos los empleados con ese cargo.
# empleado_mas_experto(): Muestra el nombre del empleado con más años de experiencia.
# listar_cargos(): Muestra cuántos empleados hay por cada tipo de cargo (ej: “Gerente: 2”, etc.).

def buscar_empleado(nombre):
    for empleado in empleados:
        if nombre in empleado["nombre"]:
            print(f"Sueldo ${empleado["sueldo"]} || Cargo {empleado["cargo"]}")

def promedio_sueldo(cargo):
    total = 0
    cont = 0
    for empleado in empleados:
        if empleado["cargo"]==cargo:
            cont +=1
            total += empleado["sueldo"]
    prom = total/cont
    print(f"El promedio salarial del cargo {cargo} es de ${round(prom)}")

def empleado_mas_experto():
    mas_experto = empleados[0]
    for empleado in empleados[1:]:
        if empleado["años_experiencia"] > mas_experto["años_experiencia"]:
            mas_experto = empleado
    print(f"El empleado con mas años de experiencia es {mas_experto["nombre"]}")

def listar_cargos():
    cargos = {}
    for empleado in empleados:
        if empleado["cargo"] not in cargos:
            cargos[empleado["cargo"]]=1
        else:
            cargos[empleado["cargo"]]+=1
    print(cargos)

while True:
    print("Bienvenido al sistema de la empresa")
    print("1. Cargar saldo y cargo por busqueda de nombre")
    print("2. Sueldo promedio de los empleados de la empresa")
    print("3. Nombre de empleado con más años de experiencia")
    print("4. Listar empleados por cargo")
    print("5. Salir")
    opc = input("ingrese alguna opcion: ")
    if opc == "1":
        nombre = input("ingrese el nombre de busqueda: ").capitalize()
        buscar_empleado(nombre)
    elif opc == "2":
        cargos = ["Desarrollador","Analista","Gerente"]
        print(cargos)
        cargo = input("Ingrese el cargo a buscar: ").capitalize()
        promedio_sueldo(cargo)
    elif opc == "3":
        empleado_mas_experto()
    elif opc == "4":
        listar_cargos()
    elif opc == "5":
        print("Te esperamos devuelta")
        break
    else:
        print("Opcion ingresada incorrecta")