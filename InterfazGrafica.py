import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox,
                            QCheckBox, QFrame, QSlider, QSpinBox, QComboBox, QScrollArea,
                            QListWidget, QListWidgetItem, QTabWidget, QProgressBar, QFileDialog)
from PyQt6.QtCore import Qt, QRegularExpression, QTimer
from PyQt6.QtGui import QRegularExpressionValidator, QIcon
from GeneradorContraseñas import PasswordManager
from estilos import obtener_tema_claro, obtener_tema_oscuro

class Generador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tema_actual = 'claro'
        self.setWindowTitle("Generador de contraseñas")
        self.setFixedSize(750, 700)
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
        self.password_showing = False
        self.password_real = ""  # Guardar la contraseña real
        self.setup_ui()
        self.apply_light_theme()
        
        # Atajos de teclado
        self.setup_shortcuts()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Crear tabs
        self.tabs = QTabWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Botón para cambiar tema en la esquina superior
        theme_layout = QHBoxLayout()
        theme_layout.addStretch()
        self.btn_tema = QPushButton("🌙 Oscuro")
        self.btn_tema.setObjectName("btn_tema")
        self.btn_tema.setFixedWidth(100)
        self.btn_tema.clicked.connect(self.toggle_tema)
        theme_layout.addWidget(self.btn_tema)
        
        # Tab 1: Generador principal
        tab1 = self.create_main_tab()
        
        # Tab 2: Historial
        self.tab_historial = self.create_history_tab()
        
        # Tab 3: Configuración
        tab3 = self.create_settings_tab()
        
        self.tabs.addTab(tab1, "Generador")
        self.tabs.addTab(self.tab_historial, "Historial")
        self.tabs.addTab(tab3, "Configuración")
        
        main_layout.addLayout(theme_layout)
        main_layout.addWidget(self.tabs)

    def create_main_tab(self):
        """Crea la pestaña principal del generador"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 15, 20, 15)
        
        # Sección de Presets
        presets_layout = QHBoxLayout()
        presets_layout.addWidget(QLabel("Modo preestablecido:"))
        self.combo_presets = QComboBox()
        self.combo_presets.addItems(["Personalizado", "Débil", "Media", "Fuerte"])
        self.combo_presets.currentTextChanged.connect(self.apply_preset)
        presets_layout.addWidget(self.combo_presets)
        presets_layout.addStretch()
        layout.addLayout(presets_layout)
        
        # Longitud con slider
        length_label = QLabel("Longitud de la contraseña")
        length_label.setObjectName("titulo")
        layout.addWidget(length_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        length_layout = QHBoxLayout()
        self.slider_longitud = QSlider(Qt.Orientation.Horizontal)
        self.slider_longitud.setMinimum(4)
        self.slider_longitud.setMaximum(128)
        self.slider_longitud.setValue(12)
        self.slider_longitud.setObjectName("slider")
        
        self.spin_longitud = QSpinBox()
        self.spin_longitud.setMinimum(4)
        self.spin_longitud.setMaximum(128)
        self.spin_longitud.setValue(12)
        
        self.slider_longitud.valueChanged.connect(self.spin_longitud.setValue)
        self.spin_longitud.valueChanged.connect(self.slider_longitud.setValue)
        
        length_layout.addWidget(self.slider_longitud)
        length_layout.addWidget(self.spin_longitud, 0, Qt.AlignmentFlag.AlignRight)
        layout.addLayout(length_layout)
        
        # Opciones de caracteres
        opciones_frame = QFrame()
        opciones_frame.setObjectName("opciones_frame")
        opciones_layout = QVBoxLayout()
        
        lbl_opciones = QLabel("Tipos de caracteres")
        lbl_opciones.setObjectName("titulo")
        opciones_layout.addWidget(lbl_opciones, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.chk_mayusculas = QCheckBox("Mayúsculas (A-Z)")
        self.chk_mayusculas.setChecked(True)
        self.chk_minusculas = QCheckBox("Minúsculas (a-z)")
        self.chk_minusculas.setChecked(True)
        self.chk_numeros = QCheckBox("Números (0-9)")
        self.chk_numeros.setChecked(True)
        self.chk_especiales = QCheckBox("Caracteres especiales")
        self.chk_especiales.setChecked(True)
        self.chk_ambiguos = QCheckBox("Excluir caracteres ambiguos (0, O, l, 1)")
        self.chk_ambiguos.setChecked(False)
        
        for chk in [self.chk_mayusculas, self.chk_minusculas, self.chk_numeros, 
                    self.chk_especiales, self.chk_ambiguos]:
            chk.setObjectName("checkbox")
            opciones_layout.addWidget(chk)
        
        # Preset de caracteres especiales
        special_layout = QHBoxLayout()
        special_layout.addWidget(QLabel("Caracteres especiales:"))
        self.combo_special_chars = QComboBox()
        self.combo_special_chars.addItems(["Básico", "Expandido", "Estricto"])
        special_layout.addWidget(self.combo_special_chars)
        special_layout.addStretch()
        opciones_layout.addLayout(special_layout)
        
        opciones_frame.setLayout(opciones_layout)
        layout.addWidget(opciones_frame)
        
        # Indicador de fortaleza
        strength_label = QLabel("Fortaleza de la contraseña")
        strength_label.setObjectName("titulo")
        layout.addWidget(strength_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.progress_fortaleza = QProgressBar()
        self.progress_fortaleza.setObjectName("progress_strength")
        self.progress_fortaleza.setMinimum(0)
        self.progress_fortaleza.setMaximum(100)
        self.progress_fortaleza.setValue(0)
        layout.addWidget(self.progress_fortaleza)
        
        self.lbl_strength = QLabel("Genera una contraseña para ver su fortaleza")
        self.lbl_strength.setObjectName("label_strength")
        layout.addWidget(self.lbl_strength, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Información de entropía y tiempo de crack
        info_layout = QHBoxLayout()
        self.lbl_entropia = QLabel("Entropía: N/A")
        self.lbl_entropia.setObjectName("info_label")
        self.lbl_tiempo_crack = QLabel("Tiempo de crack: N/A")
        self.lbl_tiempo_crack.setObjectName("info_label")
        info_layout.addWidget(self.lbl_entropia)
        info_layout.addStretch()
        info_layout.addWidget(self.lbl_tiempo_crack)
        layout.addLayout(info_layout)
        
        # Contraseña generada
        lbl_generada = QLabel("Contraseña generada")
        lbl_generada.setObjectName("titulo")
        layout.addWidget(lbl_generada, alignment=Qt.AlignmentFlag.AlignCenter)
        
        password_layout = QHBoxLayout()
        self.lbl_contrasena = QLabel("")
        self.lbl_contrasena.setObjectName("contrasena")
        password_layout.addWidget(self.lbl_contrasena)
        
        self.btn_mostrar = QPushButton("👁️")
        self.btn_mostrar.setObjectName("boton_pequeño")
        self.btn_mostrar.setFixedWidth(40)
        self.btn_mostrar.setFixedHeight(35)
        self.btn_mostrar.clicked.connect(self.toggle_password_visibility)
        password_layout.addWidget(self.btn_mostrar)
        
        layout.addLayout(password_layout)
        
        # Botones de acción
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)
        
        self.btn_generar = QPushButton("✨ Generar")
        self.btn_generar.setObjectName("boton")
        self.btn_generar.clicked.connect(self.generar_contrasena)
        
        self.btn_copiar = QPushButton("📋 Copiar")
        self.btn_copiar.setObjectName("boton")
        self.btn_copiar.clicked.connect(self.copiar_contrasena)
        
        self.btn_multiples = QPushButton("🔄 Generar x5")
        self.btn_multiples.setObjectName("boton")
        self.btn_multiples.clicked.connect(self.generar_multiples)
        
        btn_layout.addWidget(self.btn_generar)
        btn_layout.addWidget(self.btn_copiar)
        btn_layout.addWidget(self.btn_multiples)
        layout.addLayout(btn_layout)
        
        widget.setLayout(layout)
        return widget

    def create_history_tab(self):
        """Crea la pestaña de historial"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 15, 20, 15)
        
        lbl_historial = QLabel("Historial de contraseñas")
        lbl_historial.setObjectName("titulo")
        layout.addWidget(lbl_historial, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Lista de historial
        self.list_historial = QListWidget()
        self.list_historial.setObjectName("list_history")
        layout.addWidget(self.list_historial)
        
        # Botones
        btn_history_layout = QHBoxLayout()
        btn_export = QPushButton("💾 Exportar")
        btn_export.setObjectName("boton")
        btn_export.clicked.connect(self.exportar_historial)
        
        btn_clear = QPushButton("🗑️ Limpiar")
        btn_clear.setObjectName("boton")
        btn_clear.clicked.connect(self.limpiar_historial)
        
        btn_history_layout.addWidget(btn_export)
        btn_history_layout.addWidget(btn_clear)
        btn_history_layout.addStretch()
        layout.addLayout(btn_history_layout)
        
        widget.setLayout(layout)
        return widget

    def create_settings_tab(self):
        """Crea la pestaña de configuración"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 15, 20, 15)
        
        lbl_settings = QLabel("Configuración")
        lbl_settings.setObjectName("titulo")
        layout.addWidget(lbl_settings, alignment=Qt.AlignmentFlag.AlignCenter)
        
        info_text = QLabel(
            "<b>Información sobre la aplicación:</b><br>"
            "• <b>Atajos de teclado:</b><br>"
            "  - Enter: Generar contraseña<br>"
            "  - Ctrl+C: Copiar contraseña<br>"
            "  - Ctrl+H: Mostrar/ocultar contraseña<br>"
            "  - Ctrl+E: Exportar historial<br><br>"
            "• <b>Fortaleza:</b> Basada en longitud, tipos de caracteres y entropía<br>"
            "• <b>Entropía:</b> Medida de la complejidad de la contraseña<br>"
            "• <b>Tiempo de crack:</b> Estimación con ~1 billón de intentos/segundos<br><br>"
            "<b>¡Siempre usa contraseñas únicas y seguras!</b>"
        )
        info_text.setObjectName("info_text")
        info_text.setWordWrap(True)
        layout.addWidget(info_text)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget

    def apply_light_theme(self):
        self.setStyleSheet(obtener_tema_claro())

    def apply_dark_theme(self):
        self.setStyleSheet(obtener_tema_oscuro())

    def toggle_tema(self):
        if self.tema_actual == 'claro':
            self.apply_dark_theme()
            self.tema_actual = 'oscuro'
            self.btn_tema.setText("☀️ Claro")
        else:
            self.apply_light_theme()
            self.tema_actual = 'claro'
            self.btn_tema.setText("🌙 Oscuro")

    def apply_preset(self, preset_name):
        """Aplica un preset de configuración"""
        if preset_name == "Personalizado":
            return
        
        presets = self.manager.get_presets()
        preset_key = preset_name.lower()
        
        if preset_key in presets:
            preset = presets[preset_key]
            self.chk_mayusculas.setChecked(preset['mayusculas'])
            self.chk_minusculas.setChecked(preset['minusculas'])
            self.chk_numeros.setChecked(preset['numeros'])
            self.chk_especiales.setChecked(preset['especiales'])
            self.spin_longitud.setValue(preset['length'])

    def toggle_password_visibility(self):
        """Muestra u oculta la contraseña"""
        if self.password_real:
            if self.password_showing:
                # Ocultar: mostrar asteriscos
                self.lbl_contrasena.setText("*" * len(self.password_real))
                self.btn_mostrar.setText("👁️")
                self.password_showing = False
            else:
                # Mostrar: revelar contraseña
                self.lbl_contrasena.setText(self.password_real)
                self.btn_mostrar.setText("👁️‍🗨️")
                self.password_showing = True

    def generar_contrasena(self):
        """Genera una contraseña"""
        if not any([self.chk_mayusculas.isChecked(), self.chk_minusculas.isChecked(),
                   self.chk_numeros.isChecked(), self.chk_especiales.isChecked()]):
            QMessageBox.warning(self, "Sin opciones",
                              "Debes seleccionar al menos un tipo de carácter.")
            return

        try:
            length = self.spin_longitud.value()
            
            # Mapa de presets de caracteres especiales
            special_preset_map = {
                'Básico': 'basico',
                'Expandido': 'expandido',
                'Estricto': 'strict'
            }
            
            special_chars = self.manager.set_special_chars(
                special_preset_map.get(self.combo_special_chars.currentText(), 'basico')
            )
            
            opciones = {
                'mayusculas': self.chk_mayusculas.isChecked(),
                'minusculas': self.chk_minusculas.isChecked(),
                'numeros': self.chk_numeros.isChecked(),
                'especiales': self.chk_especiales.isChecked(),
                'special_chars': special_chars
            }
            
            contra = self.manager.generate_password(
                length, 
                opciones, 
                self.chk_ambiguos.isChecked()
            )
            
            self.password_real = contra  # Guardar la contraseña real
            self.lbl_contrasena.setText(contra)
            self.password_showing = False
            self.btn_mostrar.setText("👁️")
            
            # Actualizar fortaleza
            self.actualizar_fortaleza(contra)
            
            # Actualizar historial
            self.actualizar_historial()
            
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def actualizar_fortaleza(self, password):
        """Actualiza el indicador de fortaleza"""
        strength = self.manager.analyze_strength(password)
        
        self.progress_fortaleza.setValue(strength['score'])
        self.lbl_strength.setText(f"Fortaleza: {strength['level']}")
        # Usar solamente color sin font-weight para evitar conflictos de estilo
        color = strength.get('color', '#000000')
        self.lbl_strength.setStyleSheet(f"color: {color};")
        
        entropy = strength['entropy']
        self.lbl_entropia.setText(f"Entropía: {entropy:.2f} bits")
        
        crack_time = self.manager.estimate_crack_time(password)
        self.lbl_tiempo_crack.setText(f"Tiempo de crack: {crack_time}")

    def generar_multiples(self):
        """Genera múltiples contraseñas a la vez"""
        if not any([self.chk_mayusculas.isChecked(), self.chk_minusculas.isChecked(),
                   self.chk_numeros.isChecked(), self.chk_especiales.isChecked()]):
            QMessageBox.warning(self, "Sin opciones",
                              "Debes seleccionar al menos un tipo de carácter.")
            return

        try:
            length = self.spin_longitud.value()
            
            special_preset_map = {
                'Básico': 'basico',
                'Expandido': 'expandido',
                'Estricto': 'strict'
            }
            
            special_chars = self.manager.set_special_chars(
                special_preset_map.get(self.combo_special_chars.currentText(), 'basico')
            )
            
            opciones = {
                'mayusculas': self.chk_mayusculas.isChecked(),
                'minusculas': self.chk_minusculas.isChecked(),
                'numeros': self.chk_numeros.isChecked(),
                'especiales': self.chk_especiales.isChecked(),
                'special_chars': special_chars
            }
            
            passwords = self.manager.generate_multiple(
                5, 
                length, 
                opciones, 
                self.chk_ambiguos.isChecked()
            )
            
            # Mostrar las contraseñas en un mensaje
            msg_text = "Se han generado 5 contraseñas:\n\n" + "\n".join(passwords)
            QMessageBox.information(self, "Contraseñas generadas", msg_text)
            
            # Usar la última como la principal
            self.password_real = passwords[-1]  # Guardar la contraseña real
            self.lbl_contrasena.setText(passwords[-1])
            self.password_showing = False
            self.btn_mostrar.setText("👁️")
            self.actualizar_fortaleza(passwords[-1])
            self.actualizar_historial()
            
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def copiar_contrasena(self):
        """Copia la contraseña al portapapeles"""
        if self.manager.copy_password():
            # Mostrar mensaje de confirmación
            msg = QMessageBox(self)
            msg.setWindowTitle("✓ Copiado")
            msg.setText("¡Contraseña copiada al portapapeles!")
            msg.setIcon(QMessageBox.Icon.Information)
            
            # Cerrar automáticamente después de 1.5 segundos
            QTimer.singleShot(1500, msg.close)
            msg.exec()
        else:
            QMessageBox.warning(self, "Error", "No hay contraseña para copiar.")

    def actualizar_historial(self):
        """Actualiza la lista de historial"""
        self.list_historial.clear()
        history = self.manager.get_history()
        
        for entry in history[-20:]:  # Mostrar últimas 20
            password = entry['password']
            timestamp = entry['timestamp'][:19]  # Formato fecha-hora
            item_text = f"{password}  ({timestamp})"
            item = QListWidgetItem(item_text)
            self.list_historial.addItem(item)

    def exportar_historial(self):
        """Exporta el historial a un archivo JSON"""
        if not self.manager.get_history():
            QMessageBox.warning(self, "Historial vacío", 
                              "No hay contraseñas para exportar.")
            return
        
        filename, _ = QFileDialog.getSaveFileName(
            self, 
            "Guardar historial", 
            "", 
            "JSON Files (*.json)"
        )
        
        if filename:
            try:
                self.manager.export_passwords(filename)
                QMessageBox.information(self, "Éxito", 
                                      f"Historial exportado a:\n{filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al exportar: {str(e)}")

    def limpiar_historial(self):
        """Limpia el historial con confirmación"""
        reply = QMessageBox.question(
            self, 
            "Confirmar",
            "¿Estás seguro de que deseas limpiar todo el historial?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.manager.clear_history()
            self.list_historial.clear()
            QMessageBox.information(self, "Hecho", "Historial limpiado.")

    def setup_shortcuts(self):
        """Configura los atajos de teclado"""
        from PyQt6.QtGui import QKeySequence, QShortcut
        
        # Enter para generar
        QShortcut(QKeySequence(Qt.Key.Key_Return), self, self.generar_contrasena)
        
        # Ctrl+C para copiar (usando formato estándar)
        QShortcut(QKeySequence("Ctrl+C"), self, self.copiar_contrasena)
        
        # Ctrl+H para mostrar/ocultar
        QShortcut(QKeySequence("Ctrl+H"), self, self.toggle_password_visibility)
        
        # Ctrl+E para exportar
        QShortcut(QKeySequence("Ctrl+E"), self, self.exportar_historial)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Generador()
    ventana.show()
    sys.exit(app.exec())
