numeros = [4, 5, 6, 4, 7, 5, 8, 9, 4, 8]
# Tarea: Crear una nueva lista con los números que aparecen solo una vez.
# Salida esperada: [6, 7, 9]
no_repetidos = []
for n in numeros:
    if numeros.count(n) == 1:
        no_repetidos.append(n)

print("Los numeros no repetidos son")
print(no_repetidos)


numeros = [2, 3, 4]
multiplicacion = 1
# Dada una lista de números, calcular el producto (multiplicación) de todos sus elementos.
# Resultado esperado: 2 * 3 * 4 = 24
for n in numeros:
    multiplicacion *= n
print(multiplicacion)

palabra = "murciélago"
# Dada una palabra, contar cuántas veces aparece cada letra sin usar count().
# Resultado esperado: {'m':1, 'u':1, 'r':1, ...}
anidados = {}
for letra in palabra:
    if letra in anidados:
        anidados[letra] +=1
    else:
        anidados[letra]=1
print(anidados)


datos = [3, 5, 3, 2, 4, 5, 1]
# Dada una lista, eliminar los elementos repetidos pero conservando el orden en el que aparecieron por primera vez.
# Resultado esperado: [3, 5, 2, 4, 1]
repetidos = {}
for dato in datos:
    if dato not in repetidos:
        repetidos[dato]=1
    else:
        repetidos[dato]+=1
rep_ordenados = []
for rep in repetidos:
    rep_ordenados.append(rep)
print(rep_ordenados)



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Mostrar todos los elementos fila por fila")
for row in matrix:
    print(row)

print("Mostrar todos los elementos de la matriz elemento a elemento en la columna")
for row in matrix:
    for element in row:
        print(element)

print("Mostrar todos los elementos de una matriz en formato matriz")
for row in matrix:
    for element in row:
        print(element)