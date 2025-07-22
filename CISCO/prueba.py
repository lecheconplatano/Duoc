# Funcion con un nombre
def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)

introduction("Jorge")


# Funcion de direccion
def address(street, city, postal_code):
    print("Tu dirección es:", street,"St.,", city, postal_code)

s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")
address(s, c, p_c)

def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")

# Funcion con lista 
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))




