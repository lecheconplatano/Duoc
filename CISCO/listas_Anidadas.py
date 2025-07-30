# Crea una nueva lista con todos los números en una sola lista.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista1 = [num for fila in matriz for num in fila]
print(lista1)

# Cuadrados de cada número en matriz
# Con la misma matriz de arriba, crea una nueva lista con los cuadrados de todos los números.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista2 = [num ** 2 for fila in matriz for num in fila]
print(lista2)

# Filtrar números pares de la matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Crea una lista con solo los números pares dentro de esa matriz.
lista3 = [(num, "par") if num%2 == 0 else (num, "impar") for fila in matriz for num in fila]
print(lista3)

# Extraer primeras letras
# Crea una lista con la primera letra de cada palabra.
palabras = [["auto", "casa"], ["piano", "mesa"], ["zapato", "cielo"]]
lista4 = [palabra[0] for sublista in palabras for palabra in sublista]
print(lista4)

# 📊 Contar palabras con más de 4 letras
# De la misma lista palabras, crea una lista con solo las palabras que tienen más de 4 letras.
palabras = [["auto", "casa"], ["piano", "mesa"], ["zapato", "cielo"]]
lista5 = [(palabra, len(palabra)) for sublista in palabras for palabra in sublista if len(palabra) > 4]
print(lista5)
