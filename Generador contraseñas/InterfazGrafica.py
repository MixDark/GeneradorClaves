import tkinter as tk
from tkinter import messagebox
from GeneradorContraseñas import PasswordManager

class Generador:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Generador contraseñas")
        self.ventana.resizable(0, 0)
        self.ancho = 300
        self.alto = 200
        self.ventana_x = ventana.winfo_screenwidth() // 2 - self.ancho // 2
        self.ventana_y = ventana.winfo_screenheight() // 2 - self.alto // 2
        posicion = f"{self.ancho}x{self.alto}+{self.ventana_x}+{self.ventana_y}"
        self.ventana.geometry(posicion)

        self.longitud = tk.IntVar()
        self.contrasena = tk.StringVar()

        lbl_mensaje = tk.Label(self.ventana, text="Longitud de la contraseña", font=("Arial", 12, "bold"))
        lbl_mensaje.pack(pady=10)

        # Configurar la entrada con validación
        vcmd = self.ventana.register(self.validate_entry)
        self.txt_longitud = tk.Entry(self.ventana, textvariable=self.longitud, font=("Arial", 11), validate="key", validatecommand=(vcmd, '%P'))
        self.txt_longitud.pack()
        self.txt_longitud.focus()

        lbl_generada2 = tk.Label(self.ventana, text="Contraseña generada", font=("Arial", 12, "bold"))
        lbl_generada2.pack(pady=10)

        lbl_generada = tk.Label(self.ventana, textvariable=self.contrasena, font=("Arial", 11))
        lbl_generada.pack()

        btn_generar = tk.Button(self.ventana, text="Generar", command=self.generar_contrasena, font=("Arial", 12, "bold"))
        btn_generar.pack(padx=30, side="left")

        btn_copiar = tk.Button(self.ventana, text="Copiar", command=self.copiar_contrasena, font=("Arial", 12, "bold"))
        btn_copiar.pack(padx=30, side="right")

        self.manager = PasswordManager()

    def validate_entry(self, new_value):
        return new_value == "" or new_value.isdigit()

    def generar_contrasena(self):
        if self.txt_longitud.get() == "":
            messagebox.showwarning("Entrada vacía", "Ingresa un número para la longitud de la contraseña.")
            self.txt_longitud.focus()
            return

        try:
            longi = self.longitud.get()
            if longi <= 0:
                raise ValueError("La longitud debe ser mayor que cero.")
            contra = self.manager.generate_password(longi)
            self.contrasena.set(contra)
        except ValueError as e:
            messagebox.showwarning("Entrada no válida", str(e))
            self.txt_longitud.focus()
            self.txt_longitud.select_range(0, tk.END)

    def copiar_contrasena(self):
        self.manager.copy_password()

if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = Generador(ventana)
    ventana.mainloop()