"""
Módulo de estilos CSS para la aplicación Generador de Contraseñas
"""

def obtener_tema_claro():
    """Retorna el stylesheet para el tema claro"""
    return """
        QMainWindow {
            background-color: #dce4f0;
            color: black;
        }
        QWidget {
            background-color: #dce4f0;
            color: black;
        }
        QLabel {
            color: black;
        }
        QLabel#titulo {
            font-weight: bold;
            color: #1a73e8;
            font-size: 13px;
        }
        QLabel#info_label {
            font-size: 10px;
            color: #666666;
        }
        QLabel#label_strength {
            font-size: 12px;
            color: black;
            font-weight: bold;
        }
        QLabel#info_text {
            font-size: 11px;
            color: black;
            background-color: #e0e8f0;
            border: 1px solid #d0dce8;
        }
        QLabel#contrasena {
            font-size: 14px;
            font-weight: bold;
            color: black;
            background-color: #e8eef5;
            border: 1px solid #c5d0dd;
        }
        QListWidget {
            font-size: 10px;
            background-color: #e8eef5;
            border: 1px solid #c5d0dd;
            color: black;
        }
        QLineEdit {
            font-size: 11px;
            border: 1px solid #c5d0dd;
            background-color: #e8eef5;
            color: black;
        }
        QSpinBox {
            font-size: 11px;
            border: 1px solid #c5d0dd;
            background-color: #e8eef5;
            color: black;
        }
        QComboBox {
            font-size: 11px;
            border: 1px solid #c5d0dd;
            background-color: #e8eef5;
            color: black;
        }
        QPushButton#boton {
            color: white;
            background-color: #1a73e8;
            border: none;
            font-size: 15px;
            padding: 8px 15px;
        }
        QPushButton#boton_pequeño {
            font-size: 14px;
            color: #1a73e8;
            background-color: #e0e8f0;
            border: 1px solid #c5d0dd;
            padding: 4px 8px;
        }
        QCheckBox {
            font-size: 11px;
            color: black;
        }
        QPushButton#btn_tema {
            font-size: 11px;
            font-weight: bold;
            color: #1a73e8;
            background-color: #d5dce6;
            border: 1px solid #1a73e8;
        }
        QFrame#opciones_frame {
            background-color: #e0e8f0;
            border: 1px solid #d0dce8;
        }
        QProgressBar {
            border: 1px solid #c5d0dd;
            background-color: #d5dce6;
        }
    """

def obtener_tema_oscuro():
    """Retorna el stylesheet para el tema oscuro"""
    return """
        QMainWindow {
            background-color: #1e1e1e;
            color: white;
        }
        QWidget {
            background-color: #1e1e1e;
            color: white;
        }
        QLabel {
            color: white;
        }
        QLabel#titulo {
            font-weight: bold;
            color: #64b5f6;
            font-size: 13px;
        }
        QLabel#info_label {
            font-size: 10px;
            color: #cccccc;
        }
        QLabel#label_strength {
            font-size: 12px;
            color: white;
            font-weight: bold;
        }
        QLabel#info_text {
            font-size: 11px;
            color: white;
            background-color: #2d2d2d;
            border: 1px solid #404040;
        }
        QLabel#contrasena {
            font-size: 14px;
            font-weight: bold;
            color: white;
            background-color: #2d2d2d;
            border: 1px solid #404040;
        }
        QListWidget {
            font-size: 10px;
            background-color: #2d2d2d;
            border: 1px solid #404040;
            color: white;
        }
        QLineEdit {
            font-size: 11px;
            border: 1px solid #404040;
            background-color: #2d2d2d;
            color: white;
        }
        QSpinBox {
            font-size: 11px;
            border: 1px solid #404040;
            background-color: #2d2d2d;
            color: white;
        }
        QComboBox {
            font-size: 11px;
            border: 1px solid #404040;
            background-color: #2d2d2d;
            color: white;
        }
        QPushButton#boton {
            color: #1e1e1e;
            background-color: #64b5f6;
            border: none;
            font-size: 15px;
            padding: 8px 15px;
        }
        QPushButton#boton_pequeño {
            font-size: 14px;
            color: #64b5f6;
            background-color: #2d2d2d;
            border: 1px solid #404040;
            padding: 4px 8px;
        }
        QCheckBox {
            font-size: 11px;
            color: white;
        }
        QPushButton#btn_tema {
            font-size: 11px;
            font-weight: bold;
            color: #64b5f6;
            border: 1px solid #64b5f6;
        }
        QFrame#opciones_frame {
            background-color: #2d2d2d;
            border: 1px solid #404040;
        }
        QProgressBar {
            border: 1px solid #404040;
            background-color: #2d2d2d;
        }
    """
