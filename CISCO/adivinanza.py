secret_number = 777

while True:
    print(
    """
    +================================+
    | ¡Bienvenido a mi juego, muggle!|
    | Introduce un número entero     |
    | y adivina qué número he        |
    | elegido para ti.               |
    |¿Cuál es el número secreto?     |
    +================================+
    """)
    num = int(input("Ingrese un numero: "))
    if num == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

while True:
    print("Estoy atrapado dentro de un bucle.")

