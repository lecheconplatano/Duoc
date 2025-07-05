# biblioteca = {
#     "1984": {"autor": "George Orwell", "año": 1949, "copias": 2},
#     "El Principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "copias": 1}
# }

# agregar_libro(biblioteca, titulo, autor, año, copias): agrega un nuevo libro al diccionario.
# prestar_libro(biblioteca, titulo): si hay copias, resta una y muestra un mensaje de éxito.
# mostrar_biblioteca(biblioteca): muestra todos los libros con sus datos.

biblioteca = {}

def agregar_libro(biblioteca, titulo, autor, año, copias):
    if titulo in biblioteca:
        print("Ya se encuentra ese libro")
    else:
        libro = {
            titulo: {
            "autor": autor,
            "año": año,
            "copias": copias
                    }
                }
        biblioteca.update(libro)
        print(biblioteca)

def prestar_libro(biblioteca, titulo):
    if titulo in biblioteca:
        if biblioteca[titulo]["copias"] > 0:
            biblioteca[titulo]["copias"] -= 1
            print(f"Has prestado el libro '{titulo}'.")
        else:
            print("No tenemos mas stock del libro")
    else:
        print("Libro no encontrado en la biblioteca")

def mostrar_biblioteca(biblioteca):
    print(biblioteca)

    

while True:
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. mostrar biblioteca")
    print("4. Salir")
    opc = input("ingrese alguna opcion: ")
    if opc == "1":
        titulo = input("Ingrese titulo del libro: ")
        autor = input("Ingrese autor del libro: ")
        año = int(input("Ingrese año del libro: "))
        copias = int(input("Ingrese copias del libro: "))
        agregar_libro(biblioteca, titulo, autor, año, copias)
    elif opc == "2":
        titulo = input("ingrese el titulo del libro: ")
        prestar_libro(biblioteca, titulo)
    elif opc == "3":
        mostrar_biblioteca(biblioteca)
    elif opc == "4":
        print("Gracias por ingresar a nuestra libreria")
        break
