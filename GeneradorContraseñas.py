import tkinter as tk
import string
import random
import pyperclip

class Generador():
    
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Generador contraseñas")
        self.ventana.geometry("300x200")
        self.ventana.resizable(0,0)

        self.longitud = tk.IntVar()
        self.longitud.set("")
        self.contrasena = tk.StringVar()

        lbl_mensaje = tk.Label(self.ventana,text="Longitud de la contraseña",font=("Arial",12,"bold"))
        lbl_mensaje.pack(pady=10)

        txt_longitud = tk.Entry(self.ventana,textvariable=self.longitud,font=("Arial",11))
        txt_longitud.pack()
        txt_longitud.focus()

        lbl_generada2 = tk.Label(self.ventana,text="Contraseña generada",font=("Arial",12,"bold"))
        lbl_generada2.pack(pady=10)

        lbl_generada = tk.Label(self.ventana,textvariable=self.contrasena,font=("Arial",11))
        lbl_generada.pack()

        btn_generar = tk.Button(self.ventana,text="Generar",command=self.generar_contrasena,font=("Arial",12,"bold"))
        btn_generar.pack(padx=30,side="left")

        btn_copiar = tk.Button(self.ventana,text="Copiar",command=self.copiar_contrasena,font=("Arial",12,"bold"))
        btn_copiar.pack(padx=30,side="right")
     
    def generar_contrasena(self):
        longi = int(self.longitud.get())
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contra = ''.join(random.choice(caracteres) for i in range(longi))
        self.contrasena.set(contra)

    def copiar_contrasena(self):
        pyperclip.copy(self.contrasena.get())       

ventana = tk.Tk()
aplicacion = Generador(ventana)
ventana.mainloop()
