# ============================
# 🎵 ACTIVIDAD 2 – GESTOR DE PLAYLIST MUSICAL
# ============================


# Crea un programa que permita administrar una *LISTA* de canciones.
# Cada canción debe ser representada mediante un *DICCIONARIO* que contenga:
# - 'titulo' (str): nombre de la canción
# - 'artista' (str): nombre del artista o banda
# - 'genero' (str): género musical (pop, rock, reggaetón, etc.)
# - 'duracion' (float): duración en minutos

# CRAER AQUI LA LISTA DE CANCIONES
playlist = [
    {
    "titulo":"Wonder",
    "artista": "oasis",
    "genero" : "rock",
    "duracion" : 4.2
    },
    {
    "titulo":"Slide",
    "artista": "oasis",
    "genero" : "rock",
    "duracion" : 4.2    
    },
    {
    "titulo":"Like a Rolling Stone",
    "artista": "Bob Dylan",
    "genero" : "rock",
    "duracion" : 7.1        
    }
]

# ============================
# Función 1: Ver todas las canciones
# ============================
def ver_canciones():
    i = 1
    for cancion in playlist:
        print(f"{i}.- {cancion["titulo"]}")
        i+=1
# ============================
# Función 2: Buscar canciones por artista
# ============================
def buscar_por_artista():
    resultados = []
    artista = input("ingrese el nombre del artista: ").lower()
    for c in playlist:
        if artista == c["artista"]:
            resultados.append(c)
    if resultados:
        print("canciones encontradas")
        for cancion in resultados:
            print(f"canciones encontradas: {cancion["titulo"]} || genero {cancion["genero"]}")
    else:
        print("Canciones no encontradas")

# ============================
# Función 3: Agregar una nueva canción
# ============================
def agregar_cancion():
    titulo = input("ingrese el nombre de la cancion: ")
    artista = input("ingrese el nombre del artista: ")
    genero = input("ingrese el genero de la cancion: ")
    duracion = float(input("ingrese la duracion de la cancion"))
    nueva_cancion ={
        "titulo" : titulo,
        "artista": artista,
        "genero" : genero,
        "duracion" : duracion
    }
    playlist.append(nueva_cancion)
    print("Cancion Agregada con Éxito a la Playlist")
    

# ============================
# Función 4: Ver canciones por género
# ============================
def ver_por_genero(genero):
    resultados = []
    for c in playlist:
        if genero.lower() == c["genero"]:
            resultados.append(c)
    if resultados:
        print(f"canciones del genero {genero}")
        for c in resultados:
            print(f"{c["titulo"]} | {c["artista"]} | {c["duracion"]}")
    else:
        print("No se encontraron coincidencias")
            

# ============================
# Bucle principal del menú
# ============================
while True:
    print("\n🎧 Menú Playlist Personal 🎧")
    print("1. Ver todas las canciones")
    print("2. Buscar canciones por artista")
    print("3. Agregar una nueva canción")
    print("4. Ver canciones por género")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        ver_canciones()
    elif opcion == "2":
        buscar_por_artista()
    elif opcion == "3":
        agregar_cancion()
    elif opcion == "4":
        genero = input("ingrese genero de la cancion: ")
        ver_por_genero(genero)
    elif opcion == "5":
        print("Gracias por usar el gestor de playlist. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
