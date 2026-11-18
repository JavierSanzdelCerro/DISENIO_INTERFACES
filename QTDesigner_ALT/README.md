# QTDesigner_ALT · Qt Designer, paletas y estilos (versión alternativa)

> ⚠️ **Abre la carpeta `QTDesigner_ALT` en VS Code** antes de ejecutar.
> Los `.qss` y los iconos de `fugue-icons-3.5.6` se cargan con rutas relativas a la carpeta desde la que se ejecuta.

Los pasos para preparar el entorno están en [`comandos.txt`](comandos.txt).

## Cómo está hecho cada ejercicio

| Archivo | Qué es |
|---|---|
| `nombre.ui` | El diseño hecho en Qt Designer |
| `nombre_ui.py` | Generado con `pyuic6` (PyQt6). Es el que se importa. **No se edita a mano** |
| `nombre_pyside6_ui.py` | El mismo diseño generado con `pyside6-uic` (PySide6). No lo usa ningún ejercicio |
| `nombre.py` | La funcionalidad. **Este es el que se ejecuta** |
| `nombre.qss` | Su hoja de estilos |

## Ejercicios

| Ejercicio | Qué explica | Usa |
|---|---|---|
| `qss_basico` | Primera hoja `.qss`: fuentes, borde punteado, `margin`/`padding`, `.QWidget` y `#pushButton_2` | `qss_basico.qss` |
| `paleta` | Estilo `Fusion` + `QPalette` básica (Window, WindowText, Button, Highlight) | `distribucion_grid` |
| `paleta_oscura` | Tema oscuro completo con `QPalette` | `distribucion_grid` |
| `estilos_widgets` | `.qss` por tipo de widget (`QPushButton`, `QLineEdit`, `QSpinBox`) y por `#label_4` | `estilos_widgets.qss` |
| `leds` | `QPalette` para el fondo + selector `QPushButton[text="ON"]` / `[text="OFF"]` | `leds.qss` |
| `login` | Login con `QPalette` gris y la hoja de `leds`. `login.qss` tiene su propio estilo pero no se carga | `leds.qss` |
| `calculadora` | Calculadora que suma, hecha a mano con un `for` para los botones 0-9 | `calculadora.qss` |
| `pseudoestados` | `:hover`, `:pressed`, `:checked`, `:on` y subcontroles `::handle`, `::down-arrow` con icono | `pseudoestados.qss`, `fugue-icons-3.5.6` |
| `cambiar_estilo` | Cambiar la hoja `.qss` de toda la app desde un `QComboBox` | `cambiar_estilo_rojo/azul/verde.qss` |
| `estilo_widget` | `setStyleSheet` sobre un solo `QLabel` con `lambda` (color, fuente y tamaño) | `estilo_widget.qss` |
| `iconos` | Icono estándar `SP_MessageBoxCritical` con `style().standardIcon()` | |
| `plantilla` | Plantilla base para empezar: diseño + `.qss` + paleta comentada | `repaso_ui`, `cambiar_estilo_rojo.qss` |
| `repaso` | Repaso: el `QComboBox` cambia de tema y Aceptar cambia la fuente de un campo | `repaso_base.qss`, `repaso_tema1/2/3.qss` |

## Solo diseños (sin `.py` que los ejecute)

| Diseño | Contenido |
|---|---|
| `distribucion_grid` | Bloc de notas, botones, radios, checkbox y un botón que ocupa 2 celdas |
| `formulario_opciones` | Nombre, apellidos, opciones y descripción con botones Grabar/Borrar (solo `.ui`) |
| `formulario_groupbox` | Dos `QGroupBox` (botones y textos), lista y número |
