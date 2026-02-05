import random
import string
import pyperclip
import math
import json
from datetime import datetime

class PasswordManager:
    def __init__(self):
        self.last_password = ""
        self.password_history = []
        self.special_chars_presets = {
            'basico': '!@#$%^&*',
            'expandido': '!@#$%^&*()_+-=[]{}|;:,.<>?',
            'strict': '!@#$%'
        }

    def generate_password(self, length, options, exclude_ambiguous=False):
        """Genera una contraseña con las opciones especificadas"""
        chars = ''
        
        if options['mayusculas']:
            chars += string.ascii_uppercase
        if options['minusculas']:
            chars += string.ascii_lowercase
        if options['numeros']:
            chars += string.digits
        if options['especiales']:
            special_set = options.get('special_chars', self.special_chars_presets['basico'])
            chars += special_set

        if exclude_ambiguous:
            # Remover caracteres ambiguos: 0, O, l, 1, |, I
            ambiguous = '0Ol1|I'
            chars = ''.join(c for c in chars if c not in ambiguous)

        if not chars:
            raise ValueError("Debe seleccionar al menos un tipo de carácter")

        # Generar la contraseña
        password = ''.join(random.choice(chars) for _ in range(length))
        self.last_password = password
        
        # Guardar en historial
        self.password_history.append({
            'password': password,
            'timestamp': datetime.now().isoformat(),
            'length': length,
            'options': options
        })
        
        return password

    def generate_multiple(self, count, length, options, exclude_ambiguous=False):
        """Genera múltiples contraseñas"""
        passwords = []
        for _ in range(count):
            password = self.generate_password(length, options, exclude_ambiguous)
            passwords.append(password)
        return passwords

    def analyze_strength(self, password):
        """Analiza la fortaleza de una contraseña"""
        strength = {
            'score': 0,
            'level': 'Muy débil',
            'entropy': 0,
            'criteria': {
                'longitud': len(password) >= 12,
                'mayusculas': any(c.isupper() for c in password),
                'minusculas': any(c.islower() for c in password),
                'numeros': any(c.isdigit() for c in password),
                'especiales': any(not c.isalnum() for c in password)
            }
        }
        
        # Calcular puntuación
        if len(password) >= 8:
            strength['score'] += 20
        if len(password) >= 12:
            strength['score'] += 20
        if len(password) >= 16:
            strength['score'] += 10
            
        if strength['criteria']['mayusculas']:
            strength['score'] += 15
        if strength['criteria']['minusculas']:
            strength['score'] += 15
        if strength['criteria']['numeros']:
            strength['score'] += 15
        if strength['criteria']['especiales']:
            strength['score'] += 15
        
        # Calcular entropía
        charset_size = self._calculate_charset_size(password)
        strength['entropy'] = len(password) * math.log2(charset_size) if charset_size > 0 else 0
        
        # Determinar nivel
        if strength['score'] >= 80:
            strength['level'] = 'Muy fuerte'
            strength['color'] = '#4caf50'  # Verde
        elif strength['score'] >= 60:
            strength['level'] = 'Fuerte'
            strength['color'] = '#8bc34a'  # Verde claro
        elif strength['score'] >= 40:
            strength['level'] = 'Media'
            strength['color'] = '#ff9800'  # Naranja
        elif strength['score'] >= 20:
            strength['level'] = 'Débil'
            strength['color'] = '#f44336'  # Rojo
        else:
            strength['level'] = 'Muy débil'
            strength['color'] = '#d32f2f'  # Rojo oscuro
            
        return strength

    def _calculate_charset_size(self, password):
        """Calcula el tamaño del charset usado en la contraseña"""
        size = 0
        if any(c.isupper() for c in password):
            size += 26
        if any(c.islower() for c in password):
            size += 26
        if any(c.isdigit() for c in password):
            size += 10
        if any(not c.isalnum() for c in password):
            size += 32
        return size

    def estimate_crack_time(self, password, guesses_per_second=1e9):
        """Estima el tiempo para romper la contraseña"""
        strength = self.analyze_strength(password)
        charset_size = self._calculate_charset_size(password)
        
        # Número promedio de intentos = (charset_size ^ length) / 2
        total_combinations = (charset_size ** len(password)) / 2
        seconds_to_crack = total_combinations / guesses_per_second
        
        # Convertir a formato legible
        if seconds_to_crack < 1:
            return "< 1 segundo"
        elif seconds_to_crack < 60:
            return f"{int(seconds_to_crack)} segundos"
        elif seconds_to_crack < 3600:
            return f"{int(seconds_to_crack / 60)} minutos"
        elif seconds_to_crack < 86400:
            return f"{int(seconds_to_crack / 3600)} horas"
        elif seconds_to_crack < 31536000:
            return f"{int(seconds_to_crack / 86400)} días"
        else:
            return f"{int(seconds_to_crack / 31536000)} años"

    def get_presets(self):
        """Retorna los presets de contraseñas"""
        return {
            'debil': {
                'mayusculas': False,
                'minusculas': True,
                'numeros': False,
                'especiales': False,
                'length': 8
            },
            'media': {
                'mayusculas': True,
                'minusculas': True,
                'numeros': True,
                'especiales': False,
                'length': 12
            },
            'fuerte': {
                'mayusculas': True,
                'minusculas': True,
                'numeros': True,
                'especiales': True,
                'length': 16
            }
        }

    def copy_password(self):
        if self.last_password:
            pyperclip.copy(self.last_password)
            return True
        return False

    def get_history(self):
        """Retorna el historial de contraseñas"""
        return self.password_history

    def clear_history(self):
        """Limpia el historial"""
        self.password_history = []

    def export_passwords(self, filename):
        """Exporta el historial a un archivo JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.password_history, f, indent=2, ensure_ascii=False)
        return True

    def set_special_chars(self, preset_name):
        """Configura los caracteres especiales a usar"""
        if preset_name in self.special_chars_presets:
            return self.special_chars_presets[preset_name]
        return self.special_chars_presets['basico']
