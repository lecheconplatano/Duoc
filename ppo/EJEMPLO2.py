class Vehiculo():
    #Atributos
    color = None
    longitud_metros = None
    ruedas = 4

    #Metodos
    def arrancar(self):
        print("Incia arranque del motor")
    def detener(self):
        print("Se detiene el motor")

#Instaciar dos objetos del vehículo
objeto_Vehiculo_1 = Vehiculo()
objeto_Vehiculo_2 = Vehiculo()

#Direcciones de memoria donde se almacenan los objetos
print(objeto_Vehiculo_1)
print(objeto_Vehiculo_2)

# Ver atributos de un objeto
print(objeto_Vehiculo_1.ruedas) 
print(objeto_Vehiculo_1.color)

# Reasignar atributo a un objeto
objeto_Vehiculo_1.ruedas = 6
objeto_Vehiculo_1.color = "Negro"