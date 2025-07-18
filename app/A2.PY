import customtkinter as ctk

# Configuración inicial
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

estudiantes = []

def agregar_estudiante():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    nota = entry_nota.get()

    if not nombre or not edad or not nota:
        salida_textbox.delete("0.0", ctk.END)
        salida_textbox.insert(ctk.END, "⚠️ Faltan datos por ingresar.\n")
        return

    try:
        edad = int(edad)
        nota = float(nota)
    except ValueError:
        salida_textbox.delete("0.0", ctk.END)
        salida_textbox.insert(ctk.END, "❌ Edad o nota inválida.\n")
        return

    estudiante = {"nombre": nombre, "edad": edad, "nota": nota}
    estudiantes.append(estudiante)

    salida_textbox.delete("0.0", ctk.END)
    salida_textbox.insert(ctk.END, f"✅ Estudiante '{nombre}' agregado correctamente.\n")

    entry_nombre.delete(0, ctk.END)
    entry_edad.delete(0, ctk.END)
    entry_nota.delete(0, ctk.END)

def mostrar_estudiantes():
    salida_textbox.delete("0.0", ctk.END)
    if not estudiantes:
        salida_textbox.insert(ctk.END, "📭 No hay estudiantes registrados.\n")
        return

    salida_textbox.insert(ctk.END, "📋 Lista de Estudiantes:\n\n")
    for idx, est in enumerate(estudiantes, 1):
        salida_textbox.insert(
            ctk.END,
            f"{idx}. {est['nombre']} | Edad: {est['edad']} | Nota: {est['nota']}\n"
        )

def contar_aprobados():
    aprobados = sum(1 for est in estudiantes if est["nota"] >= 4.0)
    salida_textbox.delete("0.0", ctk.END)
    salida_textbox.insert(ctk.END, f"🎓 Cantidad de aprobados: {aprobados}\n")

def resumen_estadistico():
    salida_textbox.delete("0.0", ctk.END)
    if not estudiantes:
        salida_textbox.insert(ctk.END, "📭 No hay estudiantes registrados.\n")
        return

    total = sum(est["nota"] for est in estudiantes)
    promedio = total / len(estudiantes)
    mejor = max(estudiantes, key=lambda e: e["nota"])
    peor = min(estudiantes, key=lambda e: e["nota"])
    destacados = sum(1 for e in estudiantes if e["nota"] >= 6.0)

    salida_textbox.insert(ctk.END, "📊 Resumen Estadístico:\n\n")
    salida_textbox.insert(ctk.END, f"📈 Promedio general: {promedio:.2f}\n")
    salida_textbox.insert(ctk.END, f"🏅 Mejor estudiante: {mejor['nombre']} ({mejor['nota']})\n")
    salida_textbox.insert(ctk.END, f"📉 Peor estudiante: {peor['nombre']} ({peor['nota']})\n")
    salida_textbox.insert(ctk.END, f"🌟 Destacados (nota ≥ 6.0): {destacados}\n")

# Ventana principal
ventana = ctk.CTk()
ventana.title("Gestor de Estudiantes")
ventana.geometry("600x650")
ventana.resizable(False, False)

# Título
titulo = ctk.CTkLabel(
    ventana,
    text="📘 Gestión de Estudiantes",
    font=ctk.CTkFont(size=24, weight="bold")
)
titulo.pack(pady=12)

# Frame de ingreso
frame_ingreso = ctk.CTkFrame(ventana)
frame_ingreso.pack(pady=10, padx=20, fill="x")

entry_nombre = ctk.CTkEntry(frame_ingreso, placeholder_text="Nombre del estudiante")
entry_nombre.pack(pady=5, padx=10, fill="x")

entry_edad = ctk.CTkEntry(frame_ingreso, placeholder_text="Edad")
entry_edad.pack(pady=5, padx=10, fill="x")

entry_nota = ctk.CTkEntry(frame_ingreso, placeholder_text="Nota final")
entry_nota.pack(pady=5, padx=10, fill="x")

btn_agregar = ctk.CTkButton(frame_ingreso, text="➕ Agregar Estudiante", command=agregar_estudiante)
btn_agregar.pack(pady=10)

# Frame de acciones
frame_botones = ctk.CTkFrame(ventana)
frame_botones.pack(pady=10, padx=20, fill="x")

btn_mostrar = ctk.CTkButton(frame_botones, text="📋 Mostrar Estudiantes", command=mostrar_estudiantes)
btn_mostrar.pack(pady=5, padx=10, fill="x")

btn_aprobados = ctk.CTkButton(frame_botones, text="🎓 Contar Aprobados", command=contar_aprobados)
btn_aprobados.pack(pady=5, padx=10, fill="x")

btn_resumen = ctk.CTkButton(frame_botones, text="📊 Ver Resumen Estadístico", command=resumen_estadistico)
btn_resumen.pack(pady=5, padx=10, fill="x")

# Salida visual
salida_textbox = ctk.CTkTextbox(ventana, width=550, height=250, corner_radius=10)
salida_textbox.pack(pady=20)

# Iniciar aplicación
ventana.mainloop()
