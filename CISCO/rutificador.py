# 1. Tomar el rut sin puntos ni guión. Ejemplo: 27.962.409-2  
# 2. Separar el dígito verificador del rut.  
# 3. Reordenar los números de Derecha a Izquierda. Ejemplo: 9 0 4 2 6 2 9 7  
# 4. Multiplicar cada número por serie 2, 3, 4, 5, 6, 7  
# 5. Sumar todos los resultados. Ejemplo: 163  
# 6. Dividir el resultado por 11 y obtener el resto sin decimales.  
#     Ejemplo: 163 / 11 = 14,8181818182... El resultado sería 14.  
# 7. Multiplicar valor de paso 6 por 11. Ejemplo: 14 * 11 = 154  
# 8. Restar valor de paso 7 a valor de paso 5. Ejemplo: 163 - 154 = 9  
# 9. Restar resultado de paso 8 a 11. Ejemplo: 11 - 9 = 2  

rut = "22.169.412-0"
new_rut = rut.replace(".","").replace("-","")
print(f"El rut limpio es {new_rut}")
digito = new_rut[-1]
print(f"EL digito verificador es {digito}")
reordenado = int(new_rut)
reordenado = list(reordenado)
print(f"El reordenado es {reordenado}")

