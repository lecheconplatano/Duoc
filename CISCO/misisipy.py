# Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)

# Escribe una función print con el mensaje final.

# Salida Esperada

# 1 Mississippi
# 2 Mississippi
# 3 Mississippi
# 4 Mississippi
# 5 Mississippi
# Lista o no, aquí vengo!

# Solución

import time

for i in range(1,6):
    print(f"{i} Mississippi")
    time.sleep(1)
print("Lista o no, aquí vengo!")

