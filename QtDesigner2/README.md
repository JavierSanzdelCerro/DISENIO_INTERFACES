# QtDesigner2 · Qt Designer, paletas y estilos

> ⚠️ **Abre la carpeta `QtDesigner2` en VS Code** antes de ejecutar.
> Los `.qss` y los iconos de `img/icons` se cargan con rutas relativas a la carpeta desde la que se ejecuta.

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
| `paleta` | Estilo `Fusion` + `QPalette` básica (Window, WindowText, Button) | `distribucion_grid` |
| `paleta_oscura` | Tema oscuro completo con `QPalette`, `Qt.GlobalColor` y `ColorGroup.Disabled` | `distribucion_grid` |
| `fusion_qss` | Estilo `Fusion` + hoja `.qss`. ⚠️ Busca `estilo2.qss`, que no existe, así que da `FileNotFoundError` | `distribucion_grid` |
| `login` | `.qss` por tipo de widget y por `#objectName` (`#btnAceptar`, `#btnCancelar`) | `login.qss` |
| `leds` | Selector de propiedad `QPushButton[text="ON"]` / `[text="OFF"]` | `leds.qss` |
| `pseudoestados` | `:hover`, `:pressed`, `:checked`, `:on` y subcontroles `::handle`, `::down-arrow` con iconos | `pseudoestados.qss`, `img/icons` |
| `cambiar_estilo` | Cambiar la hoja `.qss` de toda la app desde un `QComboBox` | `pseudoestados.qss`, `cambiar_estilo_rojo/verde/azul.qss` |
| `calculadora` | Calculadora que suma, hecha a mano con `QGridLayout` y decorada con `.qss` | `calculadora.qss` |
| `calculadora_estilos` | Intento de importar la calculadora para darle estilos. ⚠️ Abre la calculadora y al cerrarla falla por error de MRO | `calculadora` |
| `iconos` | Icono estándar `SP_ArrowRight` con `style().standardIcon()` | |

## Solo diseños (sin `.py` que los ejecute)

| Diseño | Contenido |
|---|---|
| `distribucion_grid` | `QGridLayout` con bloc de notas, botones, radios, checkbox y un botón que ocupa 2 celdas |
| `formulario_opciones` | Nombre, apellido, descripción, `QGroupBox` con opciones y botones Grabar/Borrar |
| `formulario_datos` | Nombre, edad (`QSpinBox`), sexo (radios) y comentarios |
| `formulario_groupbox` | Dos `QGroupBox` (botones y textos), lista y número |

`qss_basico.qss` (fuentes, `margin`/`padding`, `.QWidget`) no lo carga ningún ejercicio.
