#DICCIONARIO DE LISTAS
datos = {
    "nombres": ["Ana", "Luis", "Pedro"],
    "edades": [25, 30, 20]
}
print(datos["nombres"])


#LISTA DE DICCIONARIOS
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
 ]
print(personas[0])
print(personas[0]["nombre"])
print(personas[0]["edad"])

#DICCIONARIO DE DICCIONARIOS
usuarios = {
    "001": {"nombre": "Ana", "pais": "Chile"},
    "002": {"nombre": "Luis", "pais": "Argentina"}
 }
print(usuarios["001"]["nombre"])
print(usuarios["001"]["pais"])