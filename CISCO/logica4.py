
# # Tarea: para cada fila, dejar solo los números que no se repiten.
# # Resultado esperado:
# # [[1, 3], [5, 6], [8]]

# matriz = [
#     [1, 2, 2, 3],
#     [4, 4, 5, 6],
#     [7, 7, 7, 8]
# ]

# resultado = []

# for fila in matriz:
#     fila_nueva = []
#     for num in fila:
#         if fila.count(num) == 1:
#             fila_nueva.append(num)
#     resultado.append(fila_nueva)

# print(resultado)

# palabras = ["sol", "luz", "perro", "gato", "mesa", "murciélago"]
# no_repetidas = []
# # Dada una lista de palabras, queremos quedarnos solo con las palabras que no tienen letras repetidas.
# for palabra in palabras:
#     repetidas = False
#     for letra in palabra:
#         if palabra.count(letra) >1:
#             repetidas = True
#             break
#     if not repetidas:
#         no_repetidas.append(palabra)

# print(no_repetidas)



matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# Sumar los bordes de una matriz
for i in range(len(matriz)):
    print(i)
