numeros = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Tarea: sumar todos los números en todas las sublistas}
suma_total = 0
for sublista in numeros:
    for numero in sublista:
        suma_total +=numero
print(f"La suma total es {suma_total}")


oraciones = ["El cielo es azul","Me gusta programar en Python","Hola"]
# Tarea: para cada oración, mostrar cuántas palabras tiene
# Salida esperada:
# → 'El cielo es azul' → 4 palabras
# → 'Me gusta programar en Python' → 5 palabras
# → 'Hola' → 1 palabra
for oracion in oraciones:
    total = 0
    oracion = oracion.split(" ")
    for palabra in oracion:
        total += 1
    print(f"Por oracion {oracion} hay -> {total} palabras")



estudiantes = [
    {"nombre": "Ana", "nota": 6.0},
    {"nombre": "Luis", "nota": 4.3},
    {"nombre": "Javiera", "nota": 5.5},
    {"nombre": "Tomás", "nota": 3.8}
]
# Tarea: mostrar solo los estudiantes con nota mayor o igual a 5.0
# Salida esperada:
# → Ana: 6.0
# → Javiera: 5.5
for estudiante in estudiantes:
    if estudiante["nota"] >= 5.0:
        print(f"{estudiante["nombre"]} {estudiante["nota"]}")


# Tarea: contar cuántas veces aparece cada letra, sin repetir
# Salida esperada: {'p': 1, 'r': 3, 'o': 2, 'g': 1, 'a': 2, 'm': 1, 'd': 1}
palabra = "programador"
conteo = {}

for letra in palabra:
    if letra in conteo:
        conteo[letra] += 1
    else:
        conteo[letra] = 1

print(conteo)


productos = [
    {"codigo": "A123", "nombre": "Mouse", "precio": 15000},
    {"codigo": "B456", "nombre": "Teclado", "precio": 22000},
    {"codigo": "C789", "nombre": "Pantalla", "precio": 80000}
]
# Tarea: buscar un producto ingresando su código y mostrar su nombre y precio
# Si no se encuentra, mostrar "Producto no encontrado"
codigo = input("ingresa su codigo: ").upper()
encontrados = False
for producto in productos:
    if producto["codigo"]==codigo:
        encontrados = True
        break
if encontrados:
    print(f"Codigo {producto["codigo"]}")
    print(f"Nombre {producto["nombre"]}")
    print(f"Precio {producto["precio"]}")
else:
    print("No se encontro el código")
