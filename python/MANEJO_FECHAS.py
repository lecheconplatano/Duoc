from datetime import datetime

# Lista de diccionarios
#ESTE NO LO HICE...
nacimientos = []

def registrar_bebe():
    nombre = input("Nombre del bebé: ")
    madre = input("Nombre de la madre: ")
    hospital = input("Nombre del hospital: ")
    fecha_str = input("Fecha de nacimiento (dd/mm/aaaa): ")

    try:
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        print("❌ Fecha inválida. Usa el formato dd/mm/aaaa.")
        return

    bebe = {
        "nombre": nombre,
        "madre": madre,
        "fecha_nacimiento": fecha,
        "hospital": hospital
    }

    nacimientos.append(bebe)
    print("✅ Registro exitoso.")

def mostrar_nacimientos():
    if not nacimientos:
        print("No hay nacimientos registrados.")
        return

    for bebe in nacimientos:
        fecha_formateada = bebe["fecha_nacimiento"].strftime("%d/%m/%Y")
        print(f"\n👶 {bebe['nombre']} | Madre: {bebe['madre']} | Fecha: {fecha_formateada} | Hospital: {bebe['hospital']}")

def buscar_por_fecha():
    fecha_str = input("Ingrese una fecha para buscar nacimientos (dd/mm/aaaa): ")
    try:
        fecha_buscada = datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        print("❌ Fecha inválida.")
        return

    encontrados = [b for b in nacimientos if b["fecha_nacimiento"].date() == fecha_buscada.date()]

    if encontrados:
        print(f"\n👶 Bebés nacidos el {fecha_str}:")
        for bebe in encontrados:
            print(f"- {bebe['nombre']} (Madre: {bebe['madre']}, Hospital: {bebe['hospital']})")
    else:
        print("No se encontraron nacimientos para esa fecha.")

# Menú
while True:
    print("\n🍼 Registro de Nacimientos")
    print("1. Registrar bebé")
    print("2. Mostrar todos los nacimientos")
    print("3. Buscar nacimientos por fecha")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_bebe()
    elif opcion == "2":
        mostrar_nacimientos()
    elif opcion == "3":
        buscar_por_fecha()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")
