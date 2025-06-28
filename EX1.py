libros = {
    "Cien años de soledad": "Gabriel García Márquez",
    "Don Quijote de la Mancha": "Miguel de Cervantes",
    "1984": "George Orwell"
 }

# Desarrolla un programa en Python que te permita gestionar una pequeña colección de libros. 
# Los datos de los libros se almacenarán en un diccionario donde la clave será el título del libro y el
# valor será el nombre del autor

def agregar():
    titulo = input("Ingrese Titulo: ")
    for libro,autor in libros.items():
        if titulo in libro:
            print("Este libro ya está en la colección")
            return
    autor = input("Ingrese el autor del libro: ")
    nuevo_libro = {
        titulo : autor
    }
    libros.update(nuevo_libro)
    print("libro agregado con exito")

def buscar():
    titulo = input("ingrese titulo del libro a buscar")
    for libro in libros.items():
        if titulo in libro:
            print(libro)
        else:
            print("Libros no encontrado")

def mostrar():
    for libro,autor in libros.items():
        print(f"Libro: {libro} | Autor: {autor}")

    
while True:
    print("MENU")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Mostrar libros")
    print("4. Salir")

    opc = input("Ingrese Opcion.")
    if opc ==  "1":
        agregar()
    elif opc == "2":
        buscar()
    elif opc == "3":
        mostrar()
    elif opc == "4":
        print("¡Hasta luego!")
        break