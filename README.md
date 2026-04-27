# STAR - Sistema de Subtítulos

Un proyecto para crear, editar y gestionar subtítulos en español de manera fácil y eficiente.

## 📋 Características

- ✅ Crear subtítulos desde cero
- ✅ Editar subtítulos existentes
- ✅ Soporta formato SRT (SubRip)
- ✅ Sincronización de tiempos
- ✅ Validación de subtítulos
- ✅ Ejemplos prácticos

## 🚀 Instalación

### Requisitos
- Python 3.8+

### Pasos
1. Clona el repositorio
```bash
git clone https://github.com/licmiriamjc-collab/STAR.git
cd STAR
```

2. Instala las dependencias
```bash
pip install -r requirements.txt
```

## 📖 Uso

### Crear un nuevo archivo de subtítulos

```python
from subtitles.manager import SubtitleManager

# Crear gestor de subtítulos
sm = SubtitleManager()

# Agregar subtítulos
sm.add_subtitle(1, "00:00:01,000", "00:00:05,000", "¡Hola! Este es el primer subtítulo")
sm.add_subtitle(2, "00:00:06,000", "00:00:10,000", "Este es el segundo subtítulo")
sm.add_subtitle(3, "00:00:11,000", "00:00:15,000", "Y este es el tercero")

# Guardar a archivo
sm.save("mi_video.srt")
```

### Cargar y editar subtítulos

```python
from subtitles.manager import SubtitleManager

# Cargar subtítulos existentes
sm = SubtitleManager()
sm.load("mi_video.srt")

# Editar un subtítulo
sm.edit_subtitle(1, text="Nuevo texto para el primer subtítulo")

# Desplazar todos los tiempos (en milisegundos)
sm.shift_time(2000)  # Desplaza 2 segundos hacia adelante

# Guardar cambios
sm.save("mi_video.srt")
```

### Ver subtítulos cargados

```python
# Mostrar todos los subtítulos
subtitles = sm.get_all_subtitles()
for subtitle in subtitles:
    print(subtitle)
```

## 📁 Estructura del Proyecto

```
STAR/
├── README.md
├── requirements.txt
├── subtitles/
│   ├── __init__.py
│   ├── manager.py          # Gestor principal de subtítulos
│   ├── subtitle.py         # Clase Subtitle
│   └── utils.py            # Funciones de utilidad
├── examples/
│   ├── ejemplo_basico.py   # Ejemplo básico
│   └── ejemplo_completo.py # Ejemplo completo
└── tests/
    └── test_subtitles.py   # Pruebas unitarias
```

## 🛠️ Ejemplos

Consulta la carpeta `examples/` para ejemplos prácticos de uso.

## 📝 Formato SRT

El formato SRT es el más simple y común:

```
1
00:00:01,000 --> 00:00:05,000
¡Hola! Este es el primer subtítulo

2
00:00:06,000 --> 00:00:10,000
Este es el segundo subtítulo

3
00:00:11,000 --> 00:00:15,000
Y este es el tercero
```

Cada subtítulo tiene:
- **Número de secuencia** (1, 2, 3...)
- **Tiempo de inicio y fin** (HH:MM:SS,mmm)
- **Texto del subtítulo**

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Haz un fork del proyecto
2. Crea una rama con tu feature
3. Haz commit de tus cambios
4. Haz push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT.

## 👤 Autor

**licmiriamjc-collab**

---

¡Disfruta creando subtítulos! 🎬
