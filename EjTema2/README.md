# Tema 2 · Qt Designer y estilos

> ⚠️ **Abre la carpeta `EjTema2` en VS Code** (Archivo > Abrir carpeta) antes de ejecutar.
> Los `.qss` y el `icono_guardar.png` se cargan con rutas relativas (`open("qss_archivo.qss")`),
> que se buscan en la carpeta desde la que se ejecuta. Si abres la raíz del repositorio, no los encuentra.

## Comandos

```bash
pip install PyQt6 PySide6          # PyQt6 para programar, PySide6 trae el Designer
pyside6-designer                   # abre Qt Designer
pyuic6 nombre.ui -o nombre_ui.py   # convierte el diseño a Python
```

Si `pyuic6` no se reconoce en Windows, añade al PATH la carpeta `Scripts` de Python
(por ejemplo `%APPDATA%\Python\Python314\Scripts`).

## Cómo está hecho cada ejercicio

Cada ejercicio tiene 3 archivos con el mismo nombre:

| Archivo | Qué es |
|---|---|
| `nombre.ui` | El diseño hecho en Qt Designer (QMainWindow con layouts) |
| `nombre_ui.py` | Generado con `pyuic6`. **No se edita a mano** (se pierde al regenerar) |
| `nombre.py` | La funcionalidad. **Este es el que se ejecuta** |

## Ejercicios

| # | Ejercicio | Qué explica | Archivos extra |
|---|---|---|---|
| 1 | `plantilla` | Convertir el `.ui` y abrir la ventana, sin funcionalidad | |
| 2 | `senales` | Usar los widgets por su objectName y conectar señales (`textChanged`, `clicked`) | |
| 3 | `fusion` | `app.setStyle("Fusion")` frente al estilo por defecto | |
| 4 | `paleta` | `QPalette` básica: Window, Base, Button, Highlight... con `QColor` | |
| 5 | `paleta_oscura` | Tema oscuro completo, `Qt.GlobalColor` y `ColorGroup.Disabled` | |
| 6 | `iconos` | Iconos estándar `SP_...` desde código y un icono `.png` puesto en Designer | `icono_guardar.png` |
| 7 | `qss_archivo` | Cargar una hoja `.qss` con `with open` + `app.setStyleSheet` | `qss_archivo.qss` |
| 8 | `box_model` | `border`, `border-radius`, `padding` y `margin` | `box_model.qss` |
| 9 | `selectores` | Clase, `.ClaseExacta`, `#objectName` y varios a la vez | `selectores.qss` |
| 10 | `pseudoselectores` | `:hover`, `:pressed`, `:checked`, `:focus`, `:disabled`, encadenados y `:!negados` | `pseudoselectores.qss` |
| 11 | `subcontroles` | `::groove`, `::handle`, `::drop-down`, `::up-button`, `::indicator`, `::chunk`... | `subcontroles.qss` |
| 12 | `estilo_widget` | `setStyleSheet` sobre un solo widget con `lambda` | |
| 13 | `cambiar_tema` | Cambiar la hoja `.qss` al momento desde un `QComboBox` | `tema_claro.qss`, `tema_oscuro.qss`, `tema_verde.qss` |
| 14 | `menus` | Menús y `QAction` creadas en Designer, `triggered` y `QMessageBox` | |
| 15 | `distribucion` | `layoutStretch`, `sizePolicy`, `maximumSize` y spacers (todo en el `.ui`) | |
