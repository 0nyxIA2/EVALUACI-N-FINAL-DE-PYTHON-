from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

def nuevo():
    nueva = Toplevel(ventana)
    nueva.title("Nueva Ventana")
    nueva.geometry("250x100")
    Label(nueva, text="¡Ventana nueva abierta!").pack(pady=20)

def salir():
    if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
        ventana.destroy()

def mostrar_info():
    messagebox.showinfo("Acerca de", "Este es un proyecto de formulario y menú en Tkinter.")

def limpiar_datos():
    entrada_nombre.delete(0, END)
    generoradio.set("")
    lista_carrera.set("")

def mostrar_datos():
    nombre = entrada_nombre.get()
    genero = generoradio.get()
    carrera = lista_carrera.get()
    if not nombre.strip() or not carrera.strip() or not genero:
        messagebox.showwarning("Faltan datos", "Por favor, completa todos los datos.")
        return
    mensaje = f"Nombre: {nombre}\nGénero: {genero}\nCarrera: {carrera}"
    messagebox.showinfo("Datos del estudiante", mensaje)
    if carrera == "Ing. en Sistemas":
        messagebox.showinfo("¡Excelente elección!", "¡Has elegido la mejor carrera!")
    else:
        messagebox.showinfo("¡Mala elección!", "¡Deberías de cambiar de carrera!")

ventana = Tk()
ventana.title("Proyecto Estudiante con Menú")
ventana.geometry("400x300")

barra_menu = Menu(ventana)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=mostrar_info)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
ventana.config(menu=barra_menu)

Label(ventana, text="Nombre").place(x=30, y=30)
entrada_nombre = Entry(ventana, width=30)
entrada_nombre.place(x=90, y=30)

Label(ventana, text="Género").place(x=30, y=60)
generoradio = StringVar()
generor1 = Radiobutton(ventana, text="Femenino", variable=generoradio, value="Femenino")
generor1.place(x=90, y=60)
generor2 = Radiobutton(ventana, text="Masculino", variable=generoradio, value="Masculino")
generor2.place(x=180, y=60)

Label(ventana, text="Carrera").place(x=30, y=90)
lista_carrera = Combobox(ventana, values=["Ing. en Sistemas", "Ing. Civil", "Ing. Eléctrica", "Ing. Mecánica", "Arquitectura"])
lista_carrera.place(x=100, y=90)

Button(ventana, text="Mostrar", command=mostrar_datos).place(x=80, y=130)
Button(ventana, text="Limpiar", command=limpiar_datos).place(x=150, y=130)
Button(ventana, text="Salir", command=salir).place(x=220, y=130)

ventana.mainloop()