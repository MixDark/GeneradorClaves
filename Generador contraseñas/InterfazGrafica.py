import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox,
                            QCheckBox, QFrame)
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator, QIcon
from GeneradorContraseñas import PasswordManager

class Generador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tema_actual = 'claro'  # Por defecto iniciamos en modo claro
        self.setWindowTitle("Generador de contraseñas")
        self.setFixedSize(400, 500)
        self.setWindowIcon(QIcon('icono.png'))    
        
        # Centrar la ventana
        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(
            (screen.width() - self.width()) // 2,
            (screen.height() - self.height()) // 2,
            self.width(),
            self.height()
        )

        self.manager = PasswordManager()
        self.setup_ui()
        self.apply_light_theme()  # Aplicamos el tema claro por defecto

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QVBoxLayout()
        layout.setSpacing(5)
        layout.setContentsMargins(20, 20, 20, 20)
        central_widget.setLayout(layout)

        # Layout para el botón de tema
        theme_layout = QHBoxLayout()
        theme_layout.setContentsMargins(0, 0, 0, 10)  
        
        # Agregar espaciador a la izquierda
        theme_layout.addStretch()
        
        # Botón para cambiar tema
        self.btn_tema = QPushButton("🌙 Oscuro")
        self.btn_tema.setObjectName("btn_tema")
        self.btn_tema.setFixedWidth(100)  # Ancho fijo para el botón
        self.btn_tema.clicked.connect(self.toggle_tema)
        theme_layout.addWidget(self.btn_tema)
        
        # Agregar el layout del botón al layout principal
        layout.addLayout(theme_layout)

        lbl_mensaje = QLabel("Longitud")
        lbl_mensaje.setObjectName("titulo")
        layout.addWidget(lbl_mensaje, alignment=Qt.AlignmentFlag.AlignCenter)

        self.txt_longitud = QLineEdit()
        self.txt_longitud.setObjectName("entrada")
        validator = QRegularExpressionValidator(QRegularExpression("[0-9]*"))
        self.txt_longitud.setValidator(validator)
        layout.addWidget(self.txt_longitud, alignment=Qt.AlignmentFlag.AlignCenter)

        # Frame para las opciones
        opciones_frame = QFrame()
        opciones_frame.setObjectName("opciones_frame")
        opciones_layout = QVBoxLayout()
        opciones_frame.setLayout(opciones_layout)

        lbl_opciones = QLabel("Opciones de personalización")
        lbl_opciones.setObjectName("titulo")
        opciones_layout.addWidget(lbl_opciones, alignment=Qt.AlignmentFlag.AlignCenter)

        self.chk_mayusculas = QCheckBox("Mayúsculas (A-Z)")
        self.chk_mayusculas.setChecked(False)
        self.chk_minusculas = QCheckBox("Minúsculas (a-z)")
        self.chk_minusculas.setChecked(False)
        self.chk_numeros = QCheckBox("Números (0-9)")
        self.chk_numeros.setChecked(False)
        self.chk_especiales = QCheckBox("Caracteres especiales (!@#$%^&*)")
        self.chk_especiales.setChecked(False)

        for chk in [self.chk_mayusculas, self.chk_minusculas, 
                   self.chk_numeros, self.chk_especiales]:
            chk.setObjectName("checkbox")
            opciones_layout.addWidget(chk)

        layout.addWidget(opciones_frame)

        lbl_generada2 = QLabel("Contraseña generada")
        lbl_generada2.setObjectName("titulo")
        layout.addWidget(lbl_generada2, alignment=Qt.AlignmentFlag.AlignCenter)

        self.lbl_contrasena = QLabel("")
        self.lbl_contrasena.setObjectName("contrasena")
        layout.addWidget(self.lbl_contrasena, alignment=Qt.AlignmentFlag.AlignCenter)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)
        
        self.btn_generar = QPushButton("Generar")
        self.btn_generar.setObjectName("boton")
        self.btn_generar.clicked.connect(self.generar_contrasena)
        
        self.btn_copiar = QPushButton("Copiar")
        self.btn_copiar.setObjectName("boton")
        self.btn_copiar.clicked.connect(self.copiar_contrasena)

        btn_layout.addWidget(self.btn_generar)
        btn_layout.addWidget(self.btn_copiar)
        layout.addLayout(btn_layout)

    def apply_light_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
            QLabel#titulo {
                font-family: 'Arial';
                font-size: 14px;
                font-weight: bold;
                color: #1a73e8;
                margin-bottom: 2px;
            }
            QLabel#contrasena {
                font-family: 'Arial';
                font-size: 13px;
                color: #202124;
                padding: 10px;
                background-color: white;
                border: 1px solid #dadce0;
                border-radius: 5px;
                min-width: 200px;
                margin-top: 2px;
            }
            QLineEdit#entrada {
                font-family: 'Arial';
                font-size: 13px;
                padding: 8px;
                border: 1px solid #dadce0;
                border-radius: 5px;
                max-width: 200px;
                background-color: white;
                color: #202124;
                margin-top: 2px;
                margin-bottom: 10px;
            }
            QLineEdit#entrada:focus {
                border: 2px solid #1a73e8;
                outline: none;
            }
            QPushButton#boton {
                font-family: 'Arial';
                font-size: 13px;
                font-weight: bold;
                color: white;
                background-color: #1a73e8;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                margin: 10px;
            }
            QPushButton#boton:hover {
                background-color: #1557b0;
            }
            QPushButton#boton:pressed {
                background-color: #174ea6;
            }
            QFrame#opciones_frame {
                background-color: white;
                border: 1px solid #dadce0;
                border-radius: 5px;
                margin: 10px 0;
                padding: 10px;
            }
            QCheckBox#checkbox {
                font-family: 'Arial';
                font-size: 13px;
                color: #202124;
                padding: 5px;
            }
            QCheckBox#checkbox::indicator {
                width: 18px;
                height: 18px;
            }
            QCheckBox#checkbox::indicator:unchecked {
                border: 2px solid #5f6368;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox#checkbox::indicator:checked {
                border: 2px solid #1a73e8;
                border-radius: 3px;
                background-color: #1a73e8;
            }
            QPushButton#btn_tema {
                font-family: 'Arial';
                font-size: 13px;
                font-weight: bold;
                color: #1a73e8;
                background-color: transparent;
                border: 2px solid #1a73e8;
                border-radius: 5px;
                padding: 5px 15px;
                margin: 0;           
            }
            QPushButton#btn_tema:hover {
                background-color: #1a73e8;
                color: white;
            }
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #202124;
            }
            QLabel#titulo {
                font-family: 'Arial';
                font-size: 14px;
                font-weight: bold;
                color: #8ab4f8;
                margin-bottom: 2px;
            }
            QLabel#contrasena {
                font-family: 'Arial';
                font-size: 13px;
                color: #e8eaed;
                padding: 10px;
                background-color: #303134;
                border: 1px solid #5f6368;
                border-radius: 5px;
                min-width: 200px;
                margin-top: 2px;
            }
            QLineEdit#entrada {
                font-family: 'Arial';
                font-size: 13px;
                padding: 8px;
                border: 1px solid #5f6368;
                border-radius: 5px;
                max-width: 200px;
                background-color: #303134;
                color: #e8eaed;
                margin-top: 2px;
                margin-bottom: 10px;
            }
            QLineEdit#entrada:focus {
                border: 2px solid #8ab4f8;
                outline: none;
            }
            QPushButton#boton {
                font-family: 'Arial';
                font-size: 13px;
                font-weight: bold;
                color: #202124;
                background-color: #8ab4f8;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                margin: 10px;
            }
            QPushButton#boton:hover {
                background-color: #93b8f7;
            }
            QPushButton#boton:pressed {
                background-color: #7aa3e8;
            }
            QFrame#opciones_frame {
                background-color: #303134;
                border: 1px solid #5f6368;
                border-radius: 5px;
                margin: 10px 0;
                padding: 10px;
            }
            QCheckBox#checkbox {
                font-family: 'Arial';
                font-size: 13px;
                color: #e8eaed;
                padding: 5px;
            }
            QCheckBox#checkbox::indicator {
                width: 18px;
                height: 18px;
            }
            QCheckBox#checkbox::indicator:unchecked {
                border: 2px solid #5f6368;
                border-radius: 3px;
                background-color: #303134;
            }
            QCheckBox#checkbox::indicator:checked {
                border: 2px solid #8ab4f8;
                border-radius: 3px;
                background-color: #8ab4f8;
            }
            QPushButton#btn_tema {
                font-family: 'Arial';
                font-size: 13px;
                font-weight: bold;
                color: #8ab4f8;
                background-color: transparent;
                border: 2px solid #8ab4f8;
                border-radius: 5px;
                padding: 5px 15px;
                margin: 0;           
            }
            QPushButton#btn_tema:hover {
                background-color: #8ab4f8;
                color: #202124;
            }
        """)

    def toggle_tema(self):
        if self.tema_actual == 'claro':
            self.apply_dark_theme()
            self.tema_actual = 'oscuro'
            self.btn_tema.setText("☀️ Claro")  # Sol para modo claro
        else:
            self.apply_light_theme()
            self.tema_actual = 'claro'
            self.btn_tema.setText("🌙 Oscuro")  # Luna para modo oscuro

    def generar_contrasena(self):
        if not self.txt_longitud.text():
            QMessageBox.warning(self, "Entrada vacía", 
                              "Ingresa un número para la longitud de la contraseña.")
            self.txt_longitud.setFocus()
            return

        if not any([self.chk_mayusculas.isChecked(), self.chk_minusculas.isChecked(),
                   self.chk_numeros.isChecked(), self.chk_especiales.isChecked()]):
            QMessageBox.warning(self, "Sin opciones seleccionadas",
                              "Debes seleccionar al menos un tipo de carácter.")
            return

        try:
            longi = int(self.txt_longitud.text())
            if longi <= 0:
                raise ValueError("La longitud debe ser mayor que cero.")
            
            # Configurar opciones para el generador
            opciones = {
                'mayusculas': self.chk_mayusculas.isChecked(),
                'minusculas': self.chk_minusculas.isChecked(),
                'numeros': self.chk_numeros.isChecked(),
                'especiales': self.chk_especiales.isChecked()
            }
            
            contra = self.manager.generate_password(longi, opciones)
            self.lbl_contrasena.setText(contra)
        except ValueError as e:
            QMessageBox.warning(self, "Entrada no válida", str(e))
            self.txt_longitud.setFocus()
            self.txt_longitud.selectAll()

    def copiar_contrasena(self):
        self.manager.copy_password()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Generador()
    ventana.show()
    sys.exit(app.exec())
