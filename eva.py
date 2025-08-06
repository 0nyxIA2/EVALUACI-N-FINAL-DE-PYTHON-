import tkinter as tk
from tkinter import messagebox

# -------- Datos de usuarios (en memoria) --------
usuarios = {
    "luis": "1234",
    "gabiriel": "1234",
    "kevin": "123"
}

# -------- Preguntas y respuestas --------
preguntas = [
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Tierra", "Saturno", "Júpiter", "Marte"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué estrella es el centro del sistema solar?",
        "opciones": ["Proxima Centauri", "La Luna", "El Sol", "Sirio"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cuál es la galaxia en la que se encuentra el sistema solar?",
        "opciones": ["Andrómeda", "Vía Láctea", "Orión", "Centauro"],
        "correcta": 1
    },
    {
        "pregunta": "¿En qué año llegó el hombre a la Luna?",
        "opciones": ["1969", "1959", "1980", "1972"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuál es el planeta más cercano al Sol?",
        "opciones": ["Venus", "Mercurio", "Marte", "Júpiter"],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué planeta es conocido como el 'planeta rojo'?",
        "opciones": ["Júpiter", "Saturno", "Marte", "Neptuno"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cómo se llama el telescopio espacial lanzado en 1990?",
        "opciones": ["Hubble", "James Webb", "Kepler", "Voyager"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué planeta tiene los anillos más notorios?",
        "opciones": ["Júpiter", "Urano", "Saturno", "Neptuno"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cuál es el satélite natural de la Tierra?",
        "opciones": ["Europa", "La Luna", "Titán", "Fobos"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cómo se llama el conjunto de estrellas que forman una figura en el cielo?",
        "opciones": ["Nebulosa", "Galaxia", "Constelación", "Asteroide"],
        "correcta": 2
    }
]

# -------- Variables globales --------
usuario_actual = ""
puntaje = 0
pregunta_actual = 0

# -------- Pantalla de bienvenida --------
def mostrar_bienvenida():
    limpiar_ventana()
    bienvenida = tk.Label(ventana, text=" Bienvenido a la Trivia Interactiva ", font=("Poppins", 16), fg="blue")
    bienvenida.pack(pady=30)
    tk.Button(ventana, text="Comenzar", command=mostrar_login, bg="lightblue", font=("Poppins", 12)).pack(pady=10)

# -------- Login --------
def mostrar_login():
    limpiar_ventana()
    tk.Label(ventana, text="Iniciar sesión", font=("Poppins", 14), fg="blue").pack(pady=10)
    tk.Label(ventana, text="Usuario:").pack()
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack()
    tk.Label(ventana, text="Contraseña:").pack()
    entry_contra = tk.Entry(ventana, show="*")
    entry_contra.pack()

    def intentar_login():
        usuario = entry_usuario.get()
        contra = entry_contra.get()
        if usuario in usuarios and usuarios[usuario] == contra:
            global usuario_actual, puntaje, pregunta_actual
            usuario_actual = usuario
            puntaje = 0
            pregunta_actual = 0
            messagebox.showinfo("Login exitoso", f"¡Hola {usuario_actual}!")
            mostrar_pregunta()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(ventana, text="Ingresar", command=intentar_login, bg="lightgreen").pack(pady=10)
    tk.Button(ventana, text="Volver", command=mostrar_bienvenida).pack()

# -------- Preguntas --------
def mostrar_pregunta():
    limpiar_ventana()
    global pregunta_actual
    if pregunta_actual < len(preguntas):
        pregunta = preguntas[pregunta_actual]
        tk.Label(ventana, text=f"Pregunta {pregunta_actual+1}:", font=("poppins", 12, "bold"), fg="navy").pack(pady=10)
        tk.Label(ventana, text=pregunta["pregunta"], font=("poppins", 12)).pack(pady=5)

        opcion_var = tk.IntVar(value=-1)

        for idx, opcion in enumerate(pregunta["opciones"]):
            tk.Radiobutton(ventana, text=opcion, variable=opcion_var, value=idx, font=("Poppins", 11)).pack(anchor="w")

        def responder():
            global puntaje, pregunta_actual
            seleccion = opcion_var.get()
            if seleccion == -1:
                messagebox.showwarning("Sin respuesta", "Por favor, selecciona una opción")
                return
            if seleccion == pregunta["correcta"]:
                puntaje += 1
                messagebox.showinfo("Correcto", "¡Respuesta correcta! ")
            else:
                messagebox.showinfo("Incorrecto", f"La opción correcta era: {pregunta['opciones'][pregunta['correcta']]}")
            pregunta_actual += 1
            mostrar_pregunta()

        tk.Button(ventana, text="Responder", command=responder, bg="yellow").pack(pady=10)
    else:
        mostrar_resultado()

# -------- Resultado --------
def mostrar_resultado():
    limpiar_ventana()
    tk.Label(ventana, text="Trivia finalizada ", font=("Arial", 14), fg="green").pack(pady=15)
    tk.Label(ventana, text=f"Puntaje obtenido: {puntaje} / {len(preguntas)}", font=("poppins", 12)).pack(pady=10)
    if puntaje == len(preguntas):
        mensaje = f"¡{usuario_actual}, eres un GENIO! "
    elif puntaje >= len(preguntas)//2:
        mensaje = f"¡Buen intento, {usuario_actual}! Sigue practicando. "
    else:
        mensaje = f"{usuario_actual}, puedes mejorar. ¡No te rindas! "
    tk.Label(ventana, text=mensaje, font=("Arial", 12, "italic"), fg="purple").pack(pady=10)
    tk.Button(ventana, text="Volver a jugar", command=mostrar_bienvenida, bg="lightblue").pack(pady=5)
    tk.Button(ventana, text="Salir", command=ventana.quit, bg="red", fg="white").pack()

# -------- Limpiar ventana --------
def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

# -------- Ventana principal --------
ventana = tk.Tk()
ventana.title("Trivia Interactiva - By Copilot")
ventana.geometry("450x350")
ventana.resizable(False, False)
ventana.config(bg="#F9F6F2")

# -------- Inicio --------
mostrar_bienvenida()
ventana.mainloop()