class Jugador():
    # Atributos del jugador
    edad = None

    #Metodo
    def permitir_acceso(self):
        print("puedes entrar.")
    def denegar_Acceso(self):
        print("No puedes entrar.")
    def comprobar_edad(self):
        if self.edad < 18:
            self.denegar_Acceso()
        else:
            self.permitir_acceso()

# Objeto creados a partir de la clase (Instanciar)
jugador1 = Jugador()
jugador2 = Jugador()

jugador1.edad = 15
jugador2.edad = 60

jugador1.comprobar_edad()
jugador2.comprobar_edad()
