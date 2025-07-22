def is_prime(num):
    if num <= 1:
        return False  # no es primo si es 0, 1 o negativo
    for i in range(2, num):  # probar desde 2 hasta num-1
        if num % i == 0:
            return False  # si es divisible, no es primo
    return True  # si nadie lo dividió, es primo

# Usamos la función
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")


