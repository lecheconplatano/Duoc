#hola
#waton
peliculas = [
    {"titulo": "Matrix", "stock": 50, "vendidas": 0},
    {"titulo": "El Padrino", "stock": 40, "vendidas": 0},
    {"titulo": "Interestelar", "stock": 60, "vendidas": 0}
]

def mostrar_peliculas():
    print("\nPelículas en cartelera:")
    for i, p in enumerate(peliculas):
        print(f"{i+1}. {p['titulo']} - Stock: {p['stock']} - Vendidas: {p['vendidas']}")

def vender_entradas():
    mostrar_peliculas()
    eleccion = int(input("\nSelecciona la película (número): ")) - 1

    if 0 <= eleccion < len(peliculas):
        cantidad = int(input("¿Cuántas entradas quieres comprar?: "))
        if cantidad <= peliculas[eleccion]["stock"]:
            peliculas[eleccion]["stock"] -= cantidad
            peliculas[eleccion]["vendidas"] += cantidad
            print("✅ Venta realizada con éxito.")
        else:
            print("❌ No hay suficientes entradas disponibles.")
    else:
        print("❌ Película no válida.")

def mostrar_reporte():
    print("\n📊 Reporte de ventas:")
    for p in peliculas:
        print(f"{p['titulo']} - Vendidas: {p['vendidas']} - Restantes: {p['stock']}")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar películas")
    print("2. Vender entradas")
    print("3. Mostrar reporte")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_peliculas()
    elif opcion == "2":
        vender_entradas()
    elif opcion == "3":
        mostrar_reporte()
    elif opcion == "4":
        print("👋 Cerrando el sistema.")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
