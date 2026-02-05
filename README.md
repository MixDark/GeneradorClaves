# Generador de contraseñas

Una aplicación de escritorio moderna para generar contraseñas seguras con análisis de fortaleza en tiempo real.

## Características

✨ **Generación de contraseñas**
- Generación de contraseñas customizables con diferentes tipos de caracteres
- Soporte para mayúsculas, minúsculas, números y caracteres especiales
- Generación de múltiples contraseñas (5 a la vez)
- Opción para excluir caracteres ambiguos

🔒 **Análisis de seguridad**
- Indicador de fortaleza con barra de progreso visual
- Cálculo de entropía en bits
- Estimación del tiempo de crack basado en la complejidad
- Clasificación de fortaleza (Débil, Medio, Fuerte)

📋 **Gestión de contraseñas**
- Historial de contraseñas generadas
- Copiar contraseña al portapapeles con un clic
- Mostrar/ocultar contraseña (botón ojo)
- Exportar historial a JSON

🎨 **Interfaz de usuario**
- Temas claro (gris azulado) y oscuro
- Interfaz intuitiva con pestañas
- Botones de tamaño optimizado para fácil acceso
- Diseño responsivo (800x750px)

⚙️ **Configuración**
- Presets predefinidos (Débil, Medio, Fuerte)
- Tipología de caracteres especiales (Básico, Expandido, Estricto)
- Personalizacao completa de opciones

## Requisitos

- Python 3.7+
- PyQt6 6.8.0
- pyperclip 1.9.0

## Instalación

1. **Clonar o descargar el repositorio**
```bash
git clone https://github.com/tu-usuario/generador-contraseñas.git
cd "Generador contraseñas"
```

2. **Crear un entorno virtual (opcional pero recomendado)**
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## Uso

**Ejecutar la aplicación:**
```bash
python InterfazGrafica.py
```

### Pasos básicos:

1. **Configurar opciones** - Selecciona los tipos de caracteres a incluir
2. **Generar contraseña** - Haz clic en "Generar" para una nueva contraseña
3. **Ver análisis** - Observa la fortaleza y entropía en tiempo real
4. **Copiar** - Usa el ojo para mostrar/ocultar, luego copia al portapapeles
5. **Exportar** - Guarda el historial como JSON

## Atajos de teclado

| Atajo | Función |
|-------|---------|
| `Enter` | Generar contraseña |
| `Ctrl+C` | Copiar contraseña al portapapeles |
| `Ctrl+H` | Mostrar/ocultar contraseña |
| `Ctrl+E` | Exportar historial |

## Estructura del proyecto

```
Generador contraseñas/
├── InterfazGrafica.py          # Aplicación principal (interfaz PyQt6)
├── GeneradorContraseñas.py     # Motor para generación y análisis
├── estilos.py                  # Estilos CSS para temas
├── requirements.txt            # Dependencias Python
├── README.md                   # Este archivo
├── .gitignore                  # Archivos a ignorar en Git
├── icono.png                   # Icono de la aplicación
└── __pycache__/               # Caché de Python (ignorado)
```

## Funcionalidades principales

### GeneradorContraseñas.py
Motor de contraseñas con:
- `generate_password()` - Genera una contraseña según criterios
- `analyze_strength()` - Analiza fortaleza y entropía
- `estimate_crack_time()` - Estima tiempo de crack
- `generate_multiple()` - Genera lote de 5 contraseñas

### InterfazGrafica.py
Interfaz completa con:
- Pestañas: Generador, Historial, Configuración
- Soporte para temas personalizables
- Gestión de historial
- Exportación de datos

### estilos.py
Estilos CSS combinados:
- Tema claro (gris azulado #dce4f0)
- Tema oscuro (#1e1e1e)
- Configuraciones de colores coherentes

## Configuración de caracteres

### Presets
- **Débil**: Solo letras minúsculas y números
- **Medio**: Letras mayúsculas, minúsculas y números
- **Fuerte**: Todo incluido (caracteres especiales)

### Tipos de caracteres especiales
- **Básico**: `!@#$%`
- **Expandido**: `!@#$%^&*()_+-=[]{}|;:'",.<>?/`
- **Estricto**: Solo caracteres seguros: `!#$%&*+-.=?^_|~`

## Análisis de seguridad

La aplicación calcula:
- **Entropía**: Medida en bits de la aleatoriedad
- **Fortaleza**: Basada en complejidad y longitud
- **Tiempo de Crack**: Estimado con diccionarios y GPU estándar

### Niveles de fortaleza
- 🔴 Débil (< 40 bits)
- 🟡 Medio (40-59 bits)
- 🟢 Fuerte (≥ 60 bits)

## Temas

### Tema claro
Paleta gris azulada para uso diurno:
- Fondo: #dce4f0
- Campos de entrada: #e8eef5
- Acentos: #1a73e8 (azul)

### Tema oscuro
Paleta oscura para uso nocturno:
- Fondo: #1e1e1e
- Campos de entrada: #2d2d2d
- Acentos: #64b5f6 (azul claro)

## Notas técnicas

- **Generación de aleatoriedad**: Usa `secrets` module de Python
- **Clipboard**: Integración con pyperclip
- **GUI**: Basada en PyQt6
- **Tamaño de ventana**: Fijo en 800x750px
- **Codificación**: UTF-8

## Compatibilidad

- ✅ Windows 10+
- ✅ Windows 11
- ✅ Linux (probado en Ubuntu 20.04+)
- ✅ macOS (probado en 10.14+)

## Licencia

Este proyecto está disponible bajo licencia MIT.

## Autor

Desarrollado como herramienta de seguridad personal.

## Contribuciones

Las sugerencias y reportes de bugs son bienvenidos. Por favor, abre un issue o envía un pull request.

## Changelog

### v1.0
- Lanzamiento inicial
- Generación de contraseñas con análisis completo
- Soporte para tema claro/oscuro
- Historial y exportación
