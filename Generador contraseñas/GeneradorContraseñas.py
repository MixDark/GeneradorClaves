import string
import random
import pyperclip

class PasswordManager:
    def __init__(self):
        self.password = ""

    def generate_password(self, length):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.choice(caracteres) for _ in range(length))
        return self.password

    def copy_password(self):
        pyperclip.copy(self.password)