# Crea una lista con los números del 1 al 10.
lista = [i for i in range(1,11)]
print(lista)


# Crea una lista con los cuadrados de los números del 1 al 10: [1, 4, 9, ...]
lista2 = [i**2 for i in range(1,11)]
print(lista2)

# Crea una lista con los números pares entre 1 y 20.
lista3 = [i for i in range(1,21) if i % 2 == 0]
print(lista3)

# Palabras en mayúsculas
# Dada esta lista 
palabras = ["perro", "gato", "loro", "pez"]
lista4 = [palabra.upper() for palabra in palabras]
print(lista4)

# Filtrar nombres largos
# Dada esta lista:
nombres = ["Ana", "Bernardo", "Luis", "María", "Cristóbal"]
lista5 = [len(nombre) for nombre in nombres if len(nombre) > 5]
print(lista5)

# Filtrar números múltiplos de 3
# De los números del 1 al 50, guarda solo los múltiplos de 3.
lista6 = [3 * i for i in range(1,51) if 3*i <50]
print(lista6)

# Palabras que terminan en "o"
# Dada esta lista:
palabras = ["auto", "casa", "piano", "mesa", "zapato"]
lista7 = [palabra for palabra in palabras if palabra[-1] == "o"]
print(lista7)

# De los números del 1 al 10, genera una lista que diga "par" o "impar" según corresponda.
lista8 = ["par" if i%2==0 else "impar" for i in range(1,11)]
print(lista8)


# Genera una lista que diga "adulto" si la edad es 18 o más, "menor" si es menor.
edades = [15, 22, 17, 30, 10]
lista9 = ["adulto" if edad >= 18 else "menor" for edad in edades]
print(lista9)

#Genera una nueva lista con los precios con IVA (19%) incluido.
precios = [1000, 2500, 3800]
lista10 = [1.19 * precio for precio in precios]
print(lista10)


#Crea una lista que diga "aprobado" si la nota es mayor o igual a 4.0, "reprobado" si es menor.
notas = [3.5, 4.9, 5.3, 6.1, 3.9]
lista11 = [(nota,"aprobado") if nota >= 4.0 else (nota,"reprobado") for nota in notas]
print(lista11)





