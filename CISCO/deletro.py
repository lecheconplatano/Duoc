


# LAB el Feo Devorador de Vocales
user_word = input("Ingrese la palabra: ")
user_word = user_word.upper()

vocales = ["A","E","I","O","U"]
for i in user_word:
    if i in vocales:
        continue
    else:
        print(i)


i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
        