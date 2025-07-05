# 🛒 Ejercicio Práctico: Sistema de Ventas de Librería "Lectura Viva"
# La librería Lectura Viva desea implementar un sistema para gestionar sus ventas, utilizando dos listas de diccionarios:
# Lista boletas, donde cada diccionario representa una boleta emitida.
# Lista detalle_ventas, donde cada diccionario contiene los productos comprados en una boleta específica.




# 📋 Datos Iniciales
# Lista de boletas:
# python
# Copiar
# Editar
boletas = [
    {"numero": 2001, "fecha": "01/07/2025", "cliente": "Isabel Allende", "total": 0},
    {"numero": 2002, "fecha": "02/07/2025", "cliente": "Pablo Neruda", "total": 0},
]


# Lista de detalle de ventas:
# python
# Copiar
# Editar
detalle_ventas = [
    {"numero_boleta": 2001, "producto": "Libro: Cien años de soledad", "cantidad": 1, "precio_unitario": 12000},
    {"numero_boleta": 2001, "producto": "Cuaderno universitario", "cantidad": 2, "precio_unitario": 2500},
    {"numero_boleta": 2002, "producto": "Lápices de colores", "cantidad": 1, "precio_unitario": 3500},
]

def ventas_añoymes():
    mes = input("Ingrese el mes de busqueda: ")
    año = input("Ingrese el año de busqueda: ")
    for boleta in boletas:
        fecha = boleta["fecha"]
        if mes == fecha[3:5] and año == fecha[6:]:
            print(boleta)
        else:
            print("Fecha ingresada invalida")


while True:
    print("===========================================")
    print("Sistema de Ventas de Librería Lectura Viva")
    print("===========================================")
    print("1. Mostrar el total vendido en un mes y año específico (ingresados por el usuario)")
    print("2. Mostrar la información de una boleta (incluyendo los productos comprados)")
    print("3. Agregar uno o más productos a una boleta existente.")
    print("4. Actualizar el total de todas las boletas con base en los productos.")
    print("5. Salir del programa.")
    opc = input("ingrese alguna opcion: ")
    if opc == "1":
        ventas_añoymes()
