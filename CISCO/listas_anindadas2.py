""" OBJETIVO DEL NIVEL 5 (Aplicación real con comprensión de listas y estructuras)
Diccionarios
zip()
enumerate()
Generación de estructuras como tuplas, dicts o listas filtradas
Combinación de datos múltiples (muy útil en la vida real) 
"""

# 1. Compresión de Diccionarios
edades = {"Ana": 20, "Luis": 25, "Carlos": 17}
mayores = {k: v for k, v in edades.items() if v >= 18}


