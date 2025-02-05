import random
import string
import pyperclip

class PasswordManager:
    def __init__(self):
        self.last_password = ""

    def generate_password(self, length, options):
        # Crear el conjunto de caracteres basado en las opciones seleccionadas
        chars = ''
        if options['mayusculas']:
            chars += string.ascii_uppercase
        if options['minusculas']:
            chars += string.ascii_lowercase
        if options['numeros']:
            chars += string.digits
        if options['especiales']:
            chars += "!@#$%^&*"

        if not chars:
            raise ValueError("Debe seleccionar al menos un tipo de carácter")

        # Generar la contraseña
        self.last_password = ''.join(random.choice(chars) for _ in range(length))
        return self.last_password

    def copy_password(self):
        if self.last_password:
            pyperclip.copy(self.last_password)
