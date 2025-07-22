numeros = [3, 7, 1, 9, 4]
# Tu tarea: usar un for para sumar todos los elementos
suma = 0
for n in numeros:
    suma +=n
print(f"La suma de los numeros es {suma }")


numeros = [3, 7, 1, 9, 4, 10, 2, 6]
# Tu tarea: usar un for para contar cuántos números son mayores a 5

cont = 0
for n in numeros:
    if n > 5:
        cont+=1
print(f"Los numeros mayores a 5 son {cont}")


numeros = [12, 3, 21, 5, 7, 30, 2]
# Tu tarea: usar un for para encontrar el número más grande
numeros.sort()
num_max = numeros[-1]
print(num_max)


nombres = ["Ana", "Luis", "Carlos", "Sofía"]
# Tu tarea: usar un for para crear una nueva lista invertida
new = []
for nom in nombres:
    new.insert(0,nom)
print(new) #Invertidos


numeros = [2, 4, 5, 6, 7, 8, 9, 11, 13]
primos = []

for n in numeros:
    if n < 2:
        continue  # descartamos 0 y 1, que no son primos
    es_primo = True
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(n)

print(f"Los primos son: {primos}")


numeros = [2, 5, 8, 11, 14, 17, 20]
# Tarea: sumar solo los números pares de la lista

pares = []
for n in numeros:
    if n % 2== 0:
        pares.append(n)
pares = sum(pares)
print(pares)


palabras = ["sol", "montaña", "mar", "computadora", "flor", "inteligencia"]
# Tarea: contar cuántas palabras tienen más de 5 letras
cont = 0
for palabra in palabras:
    if len(palabra) > 5:
        cont +=1
print(f"Hay {cont} palabras que superan las 5 letras")


numeros = [4, -2, 7, -9, 0, 3, -1, 5]
# Tarea: crear dos listas: una con los positivos, otra con los negativos
positivos = []
negativos = []
for n in numeros:
    if n >= 0:
        positivos.append(n)
    else:
        negativos.append(n)
print(f"Los positivos son estos {positivos}")
print(f"Los negativos son estos {negativos}")



numeros = [1, 2, 3, 4, 5]
# Tarea: crear una nueva lista con cada número elevado al cuadrado
elevados = []
for n in numeros:
    elevados.append(n**2)
print(f"La lista elevada queda así {elevados}")



palabras = ["casa", "carro", "camino", "perro", "cielo"]
# Tarea: contar cuántas veces aparece la letra "c" (considerando todas las palabras)
cont = 0
for palabra in palabras:
    for letra in palabra:
        if letra == "c":
            cont +=1
print(f"La cantidad de veces que aparece 'c' es {cont}")



numeros = [2, 3, 4, 3, 2, 7, 8, 7, 9]
# Tu tarea: crear una lista sin números repetidos
no_repetidos = []
for n in numeros:
    if n not in no_repetidos:
        no_repetidos.append(n)
    else:
        continue
print("Esta es la nueva lista sin números repetidos")
print(no_repetidos)


palabras = ["perro", "gato", "elefante", "jirafa"]
# Tu tarea: crear una lista con palabras en mayúsculas
palabras_mayusculas = []
for palabra in palabras:
    palabras_mayusculas.append(palabra.upper())
print("La lista con palabras a mayusculas es")
print(palabras_mayusculas)


numeros = [10, 23, 45, 23, 67]
valor = 23
cont = 0
# Tu tarea: encontrar el índice del primer 23
encontrados = False
for i in range(len(numeros)):
    if numeros[i] == valor:
        print(f"El valor {valor} está en el indice {i}")
        encontrados = True
        break
if not encontrados:
    print("Valor no encontrado")



palabras = ["sol", "mar", "pez", "lago", "cielo"]
# Tu tarea: filtrar las palabras con “a”
filtro = []
for palabra in palabras:
    if "a" in palabra:
        filtro.append(palabra)
print(f"Palabras encontradas {filtro}")



numeros = [5, -3, 9, 0, -1, 4]
positivos = []
# Tu tarea: calcular el promedio solo de los positivos
for n in numeros:
    if n >= 0:
        positivos.append(n)

if len(positivos) > 0:
    prom = sum(positivos)/len(positivos)
    print(f"El promedio de los postivos es {prom}")
else:
    print("No hay números positivos para calcular un promedio")
