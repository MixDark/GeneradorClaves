# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [1.0.0] - 2026-02-05

### Agregado
- Interfaz gráfica completa con PyQt6
- Generación de contraseñas con múltiples opciones de caracteres
- Análisis de fortaleza de contraseñas con indicador visual
- Cálculo de entropía en bits
- Estimación del tiempo de crack
- Función de mostrar/ocultar contraseña (botón ojo)
- Copia al portapapeles con pyperclip
- Historial de contraseñas generadas
- Generación de múltiples contraseñas (5 a la vez)
- Exportación de historial a JSON
- Tema claro con paleta gris azulada
- Tema oscuro
- Presets predefinidos (Débil, Medio, Fuerte)
- Configuración de caracteres especiales (Básico, Expandido, Estricto)
- Opción para excluir caracteres ambiguos (0, O, l, 1)
- Atajos de teclado (Enter, Ctrl+C, Ctrl+H, Ctrl+E)
- Documentación completa (README.md)
- Archivo .gitignore optimizado
- Módulo estilos.py separado para mejor organización
- Interfaz con pestañas (Generador, Historial, Configuración)

### Características técnicas
- Python 3.7+
- PyQt6 6.8.0 para interfaz gráfica
- pyperclip 1.9.0 para gestión del portapapeles
- Uso de módulo `secrets` para generación criptográficamente segura
- Ventana fija de 800x750 píxeles
- Centrado automático en la pantalla
- Soporte para múltiples idiomas (interfaz en español)

### Seguridad
- Generación de números aleatorios criptográficamente segura
- Cálculo de entropía basado en teoría de información
- Estimación de tiempo de crack considerando hardware moderno
- No almacenamiento permanente de contraseñas sin consentimiento del usuario

### Interfaz
- Diseño limpio y moderno
- Botones con iconos emoji
- Indicador de fortaleza con barra de progreso
- Visualización clara de entropía y tiempo de crack
- Respuesta visual inmediata a cambios de configuración
- Tema personalizable según preferencia del usuario

## Próximas versiones planeadas

### [1.1.0] - Próximo
- [ ] Almacenamiento local encriptado de contraseñas
- [ ] Sincronización con la nube
- [ ] Generador de frases contraseña (passphrase)
- [ ] Verificación de contraseña contra bases de datos comprometidas
- [ ] Estadísticas de uso
- [ ] Opciones de exportación adicionales (CSV, TXT, PDF)
- [ ] Soporte para múltiples idiomas en la interfaz

### [1.2.0] - Mejoras de rendimiento
- [ ] Caché de cálculos de fortaleza
- [ ] Optimización de búsqueda en historial
- [ ] Interfaz más responsiva con largo historial

### [2.0.0] - Características avanzadas (largo plazo)
- [ ] Plugin system
- [ ] API REST
- [ ] Aplicación web
- [ ] Integración con navegadores
- [ ] Autenticación de dos factores

## Notas de Desarrollo

### 2026-02-05 - Día de lanzamiento
- Inicialización del proyecto
- Todas las características principales implementadas
- Pruebas completadas en Windows 10/11, Linux y macOS
- Documentación exhaustiva creada
- Código limpio y bien comentado

### Problemas resueltos durante el desarrollo
1. ✅ Botón de mostrar/ocultar contraseña no funcionaba
   - Solucionado: Almacenar contraseña real separadamente y alternar entre asteriscos y texto

2. ✅ Errores de QFont en terminal
   - Solucionado: Simplificar aplicación de estilos dinámicos

3. ✅ Errores de parsing de stylesheet
   - Solucionado: Remover propiedades QSS inválidas y mover CSS a módulo separado

4. ✅ Tema claro demasiado blanco
   - Solucionado: Cambiar a paleta gris azulada más suave

5. ✅ Checkboxes no visibles en tema claro
   - Solucionado: Remover colores de fondo conflictivos

6. ✅ Espacio sobrante en parte inferior
   - Solucionado: Remover spacer al final del layout

7. ✅ Tamaño de texto de botones muy pequeño
   - Solucionado: Aumentar tamaño de fuente a 15px para botones principales

## Contribuciones

Este proyecto agradece las contribuciones. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Reconocimientos

- PyQt6 Documentation
- Python Security Best Practices
- OWASP Password Guidelines

## Licencia

Distribuido bajo licencia MIT. Ver `LICENSE` para más detalles.
