import tkinter
import string
import random
import pyperclip
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.title("Generador")
ventana.geometry("250x160")
ventana.resizable(0,0)

caracteres = list(string.ascii_letters + string.digits + "!#@&%$()/+*-")
longitud = tkinter.IntVar()

def generar():
    random.shuffle(caracteres)

    password = []
    for i in range(longitud.get()):
        password.append(random.choice(caracteres))

    random.shuffle(password)

    lblGenerada.configure(text="Contraseña: "+"".join(password))
    pyperclip.copy("".join(password))
    messagebox.showinfo(message="Contraseña copiada al portapeles", title="Generador") 

lblMensaje = tkinter.Label(ventana,text="Longitud de la contraseña")
lblMensaje.pack(pady=10)

txtLongitud = tkinter.Entry(ventana,textvariable=longitud).pack()

btnGenerar = tkinter.Button(ventana,text="Generar",command=generar).pack(pady=15)
lblGenerada = tkinter.Label(ventana,text="Contraseña: ")
lblGenerada.pack()

ventana.mainloop()