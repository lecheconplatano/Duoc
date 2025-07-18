import customtkinter as ctk

# Configuración del tema
ctk.set_appearance_mode("Dark")  # "Light", "Dark", o "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

# Crear ventana principal
ventana = ctk.CTk()
ventana.title("Analisis Aplicacion")
ventana.geometry("400x600")  # ancho x alto

# Función que se ejecuta al presionar el botón
def saludar():
    nombre = entrada.get()  # Obtener texto ingresado
    etiqueta_resultado.configure(text=f"¡Hola, {nombre}!")  # Mostrar saludo

# Etiqueta con la pregunta
etiqueta = ctk.CTkLabel(ventana, text="¿Cómo te llamas?")
etiqueta.pack(pady=10)

# Entrada de texto
entrada = ctk.CTkEntry(ventana, placeholder_text="Escribe tu nombre aquí")
entrada.pack(pady=10)

# Botón
boton = ctk.CTkButton(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = ctk.CTkLabel(ventana, text="")
etiqueta_resultado.pack(pady=10)


# Mostrar ventana
ventana.mainloop()
