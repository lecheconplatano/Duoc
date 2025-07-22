# Lista de numeros sin repetir
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for num in my_list:
    if num not in new_list:
        new_list.append(num)
my_list = new_list
print("La lista con elementos únicos:")
print(my_list)

# Determinar el cuadrado por cada elemento
squares = [x ** 2 for x in range(10)]
print(squares)

# Lista donde cada elemento se multiplica por dos
twos = [2 ** i for i in range(8)]
print(twos)

# Lista de impares 
odds = [x for x in squares if x % 2 != 0 ]  
print(odds)

# Tablero de ajedez
board = []

EMPTY = "."
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
print(board)

# Resultado esperado
"""
[['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.']] 
"""

# Temperaturas experimento

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)

# 3 Edificios con 15 pisos cada uno y 20 habitaciones para cada piso
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# Reservar una habitacion 
rooms[1][9][13] = True # reserva la habitacion 14 del en el piso 16 del edificio 2
rooms[0][4][1] = False # reserva la habitacion 2 del en el piso 5 del edificio 1

# Verificar vacantes en el tercer edificio en el piso 15 y si hay vacantes se aumenta el contador 
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1


#  Almacenar el cuadrado de los numeros del 1 al 4 con un rango del 1-5
cubed = [num ** 3 for num in range(5)]
print(cubed)  # output: [0, 1, 8, 27, 64]


# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)'


# Cubo - un arreglo tridimensional (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'










