# Las clases tienen adentro:
# Atributos y métodos
# variables y funciones 

class Clase():
    #bloque de codigo 
    pass

# Python está hecho con clases y objetos
saludo = "hola"
print(type(saludo))

mayusculas = saludo.upper()
print(type(mayusculas))

# Identidad de los objetos (id)
print(id(saludo))
print(id(mayusculas))

# Los objetos tienen:
# Estado : Sería la interacción con los atributos
# osea con las variables
# Comportamiento : Sería la alineacion con los metodos
# osea con las funciones

# Declaracion de clase
class NombreClase():
    pass

# Objeto creado a partir de clase
objeto = NombreClase()