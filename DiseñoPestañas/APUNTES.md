# Apuntes de PyQt6 — Diseño de interfaces

## Índice

1. [Los tres módulos de PyQt6](#1-los-tres-módulos-de-pyqt6)
2. [Estructura de una aplicación](#2-estructura-de-una-aplicación)
3. [La ventana principal: `QMainWindow`](#3-la-ventana-principal-qmainwindow)
4. [Señales y slots](#4-señales-y-slots)
5. [Widgets](#5-widgets)
6. [Fuentes y colores](#6-fuentes-y-colores)
7. [Layouts: colocar varios widgets](#7-layouts-colocar-varios-widgets)
8. [Páginas y pestañas](#8-páginas-y-pestañas)
9. [Barra de herramientas, menús y barra de estado](#9-barra-de-herramientas-menús-y-barra-de-estado)
10. [Cuadros de diálogo](#10-cuadros-de-diálogo)
11. [Varias ventanas](#11-varias-ventanas)
12. [Ejemplo completo: todo junto](#12-ejemplo-completo-todo-junto)
13. [Chuleta de señales](#13-chuleta-de-señales)
14. [Errores típicos](#14-errores-típicos)
15. [Preguntas de repaso](#15-preguntas-de-repaso)

---

## 1. Los tres módulos de PyQt6

Casi todo se importa de tres módulos. Saber cuál es cuál evita la mitad de los errores de `ImportError`.

| Módulo | Qué contiene | Clases que usamos |
|---|---|---|
| `PyQt6.QtWidgets` | Todo lo que se **ve** y con lo que se interactúa | `QApplication`, `QMainWindow`, `QWidget`, `QPushButton`, `QLabel`, `QLineEdit`, `QCheckBox`, `QRadioButton`, `QComboBox`, `QListWidget`, `QSpinBox`, `QSlider`, `QDial`, `QCalendarWidget`, `QDateEdit`, layouts, `QTabWidget`, `QGroupBox`, `QToolBar`, `QStatusBar`, `QDialog`, `QDialogButtonBox`, `QMessageBox`, `QAbstractItemView` |
| `PyQt6.QtCore` | Cosas **no visuales**: constantes y tipos de datos | `Qt` (alineaciones, orientaciones…), `QSize`, `QDate` |
| `PyQt6.QtGui` | Recursos **gráficos** | `QAction`, `QIcon`, `QPixmap`, `QFont`, `QColor`, `QPalette`, `QKeySequence` |

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt, QSize, QDate
from PyQt6.QtGui import QAction, QIcon, QPixmap
```

> Truco para recordarlo: `QAction` e `QIcon` **no** están en `QtWidgets`, están en `QtGui`.

---

## 2. Estructura de una aplicación

Toda aplicación PyQt6 tiene la misma forma:

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):          # nuestra ventana hereda de QMainWindow
    def __init__(self):
        super().__init__()              # inicializa la parte de QMainWindow
        self.setWindowTitle("Mi aplicación")

        boton = QPushButton("Pulsa")    # creamos un widget...
        self.setCentralWidget(boton)    # ...y lo colocamos en la ventana


app = QApplication([])      # 1. crear la aplicación (solo una por programa)
window = MainWindow()       # 2. crear la ventana
window.show()               # 3. mostrarla (las ventanas nacen ocultas)
app.exec()                  # 4. arrancar el bucle de eventos
```

Qué hace cada paso:

1. **`QApplication([])`**: crea la aplicación. Tiene que existir **antes** de crear cualquier widget. Recibe una lista de argumentos; con `[]` vale. (Si se quieren pasar los argumentos de la línea de comandos: `QApplication(sys.argv)`.)
2. **`MainWindow()`**: construye la ventana y todo lo que hay dentro (se ejecuta `__init__`).
3. **`show()`**: la hace visible.
4. **`app.exec()`**: el programa se queda aquí **esperando eventos** (clics, teclas…) hasta que se cierra la ventana. Sin esta línea la ventana se cerraría al instante.

### `self.` o variable local

```python
boton = QPushButton("A")        # local: solo existe dentro de __init__
self.boton = QPushButton("B")   # atributo: se puede usar en cualquier método de la clase
```

Regla práctica: si vas a necesitar el widget **en otro método** (por ejemplo, en el que responde a un clic), créalo con `self.`.

---

## 3. La ventana principal: `QMainWindow`

`QMainWindow` es una ventana con zonas ya reservadas:

```
┌──────────────────────────────────┐
│ Barra de menús      (menuBar)    │
├──────────────────────────────────┤
│ Barra de herramientas (QToolBar) │
├──────────────────────────────────┤
│                                  │
│        Widget central            │
│     (setCentralWidget)           │
│                                  │
├──────────────────────────────────┤
│ Barra de estado     (QStatusBar) │
└──────────────────────────────────┘
```

### Métodos de la ventana

```python
self.setWindowTitle("Mi aplicación")      # título
self.setWindowIcon(QIcon("icons/bug.png"))  # icono de la ventana

self.setFixedSize(QSize(400, 300))        # tamaño fijo, no se puede redimensionar
self.setMinimumSize(QSize(200, 150))      # tamaño mínimo
self.setMaximumSize(QSize(800, 600))      # tamaño máximo
self.resize(600, 400)                     # tamaño inicial (sí se puede redimensionar)

self.setCentralWidget(widget)             # widget que ocupa la zona central
```

> **Importante:** `setCentralWidget` admite **un único widget**. Para poner varios hace falta un **layout** dentro de un widget contenedor (apartado 7).

---

## 4. Señales y slots

Es el mecanismo con el que la interfaz **reacciona** a lo que hace el usuario.

- **Señal**: aviso que emite un widget cuando le pasa algo. Ej.: un botón emite `clicked` al pulsarlo.
- **Slot**: función que se ejecuta cuando llega esa señal.
- Se unen con **`widget.señal.connect(slot)`**.

### 4.1 Conexión básica

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        boton = QPushButton("Pulsa")
        boton.clicked.connect(self.saludar)   # SIN paréntesis
        self.setCentralWidget(boton)

    def saludar(self):
        print("Hola")
```

`self.saludar` va **sin paréntesis**: le pasamos la función para que Qt la llame cuando toque. Con paréntesis (`self.saludar()`) se ejecutaría en ese momento, una sola vez.

### 4.2 Slots que reciben datos

Muchas señales envían un valor. El slot lo recibe como parámetro:

```python
caja = QLineEdit()
caja.textChanged.connect(self.mostrar)    # textChanged envía el texto nuevo (str)

def mostrar(self, texto):
    print("Has escrito:", texto)
```

### 4.3 Conectar un widget directamente con otro

No hace falta escribir un método propio si el de otro widget ya hace lo que queremos:

```python
caja = QLineEdit()
etiqueta = QLabel()
caja.textChanged.connect(etiqueta.setText)   # lo que escribes aparece en la etiqueta
```

### 4.4 Pasar argumentos con `lambda`

Si queremos llamar a una función **con un argumento concreto**, la envolvemos en una `lambda`:

```python
boton_rojo.clicked.connect(lambda: self.cambiar_color("red"))
boton_verde.clicked.connect(lambda: self.cambiar_color("green"))
```

La `lambda` crea una función pequeña sin nombre que se ejecutará al pulsar.

### 4.5 Varios widgets, un solo slot: `sender()`

Dentro de un slot, `self.sender()` devuelve **el widget que ha emitido la señal**:

```python
for texto in ["Uno", "Dos", "Tres"]:
    boton = QPushButton(texto)
    boton.clicked.connect(self.pulsado)
    layout.addWidget(boton)

def pulsado(self):
    print(self.sender().text(), "pulsado")    # "Dos pulsado"
```

### 4.6 Una señal, varios slots

Una misma señal puede conectarse a varios slots; se ejecutan todos:

```python
boton.clicked.connect(self.guardar)
boton.clicked.connect(self.avisar)
```

Cuidado con lo contrario: si conectas **dos señales que saltan a la vez** al mismo slot, el slot se ejecuta dos veces (ver errores típicos).

---

## 5. Widgets

Un **widget** es cualquier elemento visual: botones, etiquetas, cajas de texto… Todos heredan de `QWidget`, así que todos comparten estos métodos:

```python
widget.setEnabled(False)     # desactivado (gris, no responde)
widget.setVisible(False)     # oculto  (equivalente a widget.hide())
widget.setToolTip("Ayuda")   # texto al dejar el ratón encima
widget.setFixedSize(QSize(100, 30))
```

### 5.1 `QPushButton` — Botón

**Instanciación**

```python
boton = QPushButton("Aceptar")
boton = QPushButton(QIcon("icons/bug.png"), "Aceptar")   # con icono
```

**Métodos**

| Método | Para qué |
|---|---|
| `setText("…")` / `text()` | Cambiar / leer el texto |
| `setCheckable(True)` | Botón de **dos estados** (se queda hundido, como un interruptor) |
| `setChecked(True)` / `isChecked()` | Marcar / consultar el estado (solo si es *checkable*) |
| `setEnabled(False)` | Desactivarlo |

**Señales**

| Señal | Cuándo | Envía |
|---|---|---|
| `clicked` | Clic completo (pulsar y soltar encima) | `bool`: estado si es *checkable* |
| `pressed` | Al hundir el botón del ratón | — |
| `released` | Al soltarlo | — |
| `toggled` | Cambia el estado de un botón *checkable* | `bool` |

Orden al hacer un clic: `pressed` → `released` → `clicked`.

**Ejemplo: botón interruptor**

```python
self.boton = QPushButton("No pulsado")
self.boton.setCheckable(True)
self.boton.clicked.connect(self.cambiado)

def cambiado(self, pulsado):                 # pulsado es True o False
    self.boton.setText(["No pulsado", "Pulsado"][pulsado])
```

> Truco: `True` vale `1` y `False` vale `0`, así que se pueden usar como **índice de una lista**.

**Ejemplo: botón de un solo uso**

```python
def pulsado(self):
    self.boton.setEnabled(False)    # tras el primer clic queda desactivado
```

### 5.2 `QLabel` — Etiqueta (texto o imagen)

**Instanciación**

```python
etiqueta = QLabel("Hola")
etiqueta = QLabel()          # vacía, se rellena después
```

**Métodos**

| Método | Para qué |
|---|---|
| `setText("…")` / `text()` | Texto |
| `setAlignment(Qt.AlignmentFlag.AlignCenter)` | Alineación |
| `setFont(fuente)` | Fuente (apartado 6) |
| `setPixmap(QPixmap("ruta"))` | Mostrar una **imagen** |
| `setScaledContents(True)` | La imagen se adapta al tamaño de la etiqueta |
| `setWordWrap(True)` | El texto largo salta de línea |

**Alineación.** Se combinan horizontal y vertical con `|`:

```python
etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)    # lo mismo, en corto
```

| Horizontal | Vertical |
|---|---|
| `AlignLeft`, `AlignRight`, `AlignHCenter`, `AlignJustify` | `AlignTop`, `AlignBottom`, `AlignVCenter` |

**Imagen**

```python
from PyQt6.QtGui import QPixmap

foto = QLabel()
foto.setPixmap(QPixmap("Img/foto.webp"))
foto.setScaledContents(True)
```

> La ruta es **relativa a la carpeta desde la que ejecutas** el programa. Si la ruta está mal no da error: la etiqueta simplemente sale vacía.

### 5.3 `QLineEdit` — Caja de texto de una línea

**Instanciación**

```python
caja = QLineEdit()
caja = QLineEdit("texto inicial")
```

**Métodos**

| Método | Para qué |
|---|---|
| `text()` / `setText("…")` / `clear()` | Leer / escribir / vaciar |
| `setPlaceholderText("Tu nombre…")` | Texto gris de ayuda que desaparece al escribir |
| `setMaxLength(10)` | Máximo de caracteres |
| `setReadOnly(True)` | Solo lectura |
| `setEchoMode(QLineEdit.EchoMode.Password)` | Oculta lo escrito (contraseñas) |

**Señales**

| Señal | Cuándo | Envía |
|---|---|---|
| `textChanged` | Cada vez que cambia el texto (cada tecla) | `str` |
| `returnPressed` | Al pulsar Enter | — |
| `editingFinished` | Al pulsar Enter o salir de la caja | — |

**Ejemplo**

```python
self.nombre = QLineEdit()
self.nombre.setPlaceholderText("Introduce tu nombre...")
self.nombre.setMaxLength(10)
self.nombre.returnPressed.connect(self.enviar)

def enviar(self):
    print("Hola,", self.nombre.text())
```

### 5.4 `QCheckBox` — Casilla de verificación

Opciones **independientes**: se pueden marcar varias a la vez.

**Instanciación**

```python
casilla = QCheckBox("Acepto las condiciones")
```

**Métodos**

| Método | Para qué |
|---|---|
| `isChecked()` / `setChecked(True)` | Consultar / marcar |
| `setTristate(True)` | Permite un tercer estado "parcialmente marcada" |
| `text()` | Texto de la casilla |

**Señal `stateChanged`**: envía un **entero**:

| Valor | Estado |
|---|---|
| `0` | Desmarcada |
| `1` | Parcialmente marcada (solo con `setTristate(True)`) |
| `2` | Marcada |

```python
casilla.stateChanged.connect(self.cambio)

def cambio(self, estado):
    print(["Desmarcada", "Parcial", "Marcada"][estado])
```

Si solo te interesa sí/no, es más sencilla `toggled`, que envía `True`/`False`:

```python
casilla.toggled.connect(lambda marcada: print(marcada))
```

### 5.5 `QRadioButton` — Botón de opción

Opciones **excluyentes**: solo puede haber **una marcada** a la vez.

**Instanciación**

```python
opcion1 = QRadioButton("Pequeño")
opcion2 = QRadioButton("Mediano")
opcion1.setChecked(True)          # marcada por defecto
```

- Los radio buttons que están **dentro del mismo contenedor** se excluyen entre sí automáticamente.
- Para tener **varios grupos independientes**, mete cada grupo en su propio `QGroupBox` (apartado 7.6).
- Señales: `toggled(bool)`, `clicked(bool)`.

```python
opcion1.toggled.connect(self.elegido)

def elegido(self, marcado):
    if marcado:
        print(self.sender().text())
```

### 5.6 `QComboBox` — Lista desplegable

**Instanciación y elementos**

```python
combo = QComboBox()
combo.addItems(["Uno", "Dos", "Tres"])   # varios: recibe una LISTA
combo.addItem("Cuatro")                  # uno solo
```

**Métodos**

| Método | Para qué |
|---|---|
| `currentText()` / `currentIndex()` | Texto / posición del elemento elegido (desde 0) |
| `setCurrentIndex(2)` | Seleccionar por posición |
| `setEditable(True)` | El usuario puede **escribir**; al pulsar Enter se añade a la lista |
| `count()` / `clear()` | Nº de elementos / vaciar |

**Señales**

| Señal | Envía |
|---|---|
| `currentIndexChanged` | `int` (posición) |
| `currentTextChanged` | `str` (texto) |

```python
combo.currentIndexChanged.connect(lambda i: print("Posición:", i))
combo.currentTextChanged.connect(lambda t: print("Texto:", t))
```

### 5.7 `QListWidget` — Lista visible

Como el combo, pero con todos los elementos siempre a la vista.

**Instanciación**

```python
from PyQt6.QtWidgets import QListWidget, QAbstractItemView

lista = QListWidget()
lista.addItems(["Uno", "Dos", "Tres"])
lista.addItem("Cuatro")
```

**Selección múltiple**

```python
lista.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
```

| Modo | Comportamiento |
|---|---|
| `SingleSelection` | Uno solo (por defecto) |
| `MultiSelection` | Varios, cada clic marca/desmarca |
| `ExtendedSelection` | Varios con Ctrl y Mayús (como en el explorador de archivos) |

**Leer la selección**

```python
lista.currentItem().text()                         # elemento actual
[item.text() for item in lista.selectedItems()]    # todos los seleccionados
lista.currentRow()                                 # posición del actual
```

**Señales**: `currentTextChanged(str)`, `currentRowChanged(int)`, `itemClicked(item)`, `itemSelectionChanged()`.

### 5.8 `QSpinBox` / `QDoubleSpinBox` — Selector numérico

**Instanciación**

```python
numero = QSpinBox()
numero.setRange(-10, 10)       # mínimo y máximo (o setMinimum / setMaximum)
numero.setSingleStep(2)        # cuánto sube o baja cada flecha
numero.setValue(0)             # valor inicial
numero.setPrefix("Total: ")    # texto delante
numero.setSuffix(" €")         # texto detrás
```

Para decimales:

```python
precio = QDoubleSpinBox()
precio.setDecimals(2)
precio.setSingleStep(0.5)
```

**Leer**: `numero.value()`.

**Señales**

| Señal | Envía | Ejemplo |
|---|---|---|
| `valueChanged` | el número | `2` |
| `textChanged` | el texto completo | `"Total: 2 €"` |

### 5.9 `QSlider` y `QDial` — Deslizador y rueda

Funcionan igual; solo cambia la forma.

**Instanciación**

```python
deslizador = QSlider(Qt.Orientation.Horizontal)   # o Qt.Orientation.Vertical
deslizador.setRange(-10, 10)
deslizador.setValue(0)
deslizador.setTickPosition(QSlider.TickPosition.TicksBelow)   # rayitas debajo
deslizador.setTickInterval(5)

rueda = QDial()
rueda.setRange(0, 100)
rueda.setNotchesVisible(True)    # marcas alrededor de la rueda
rueda.setWrapping(True)          # al pasar del máximo vuelve al mínimo
```

**Leer**: `value()`.

**Señales**

| Señal | Cuándo |
|---|---|
| `valueChanged(int)` | Con **cualquier** cambio (ratón, teclado o código) |
| `sliderMoved(int)` | Solo mientras se **arrastra** con el ratón |
| `sliderPressed` / `sliderReleased` | Al coger / soltar el control |

Normalmente basta con `valueChanged`.

### 5.10 `QCalendarWidget` — Calendario

**Instanciación**

```python
self.calendario = QCalendarWidget()
self.calendario.setMinimumDate(QDate(2006, 1, 1))
self.calendario.setSelectedDate(QDate.currentDate())   # hoy
```

**Señales**

- `selectionChanged`: **no envía la fecha**, hay que pedirla con `selectedDate()`.
- `clicked(QDate)`: sí envía la fecha pulsada.

```python
self.calendario.selectionChanged.connect(self.mostrar)

def mostrar(self):
    fecha = self.calendario.selectedDate()        # devuelve un QDate
    print(fecha.toString("dd/MM/yyyy"))           # "22/10/2026"
```

### 5.11 `QDateEdit` — Campo de fecha

Una caja compacta para elegir una fecha, con calendario desplegable opcional.

**Instanciación**

```python
from PyQt6.QtWidgets import QDateEdit
from PyQt6.QtCore import QDate

fecha = QDateEdit()
fecha.setCalendarPopup(True)              # flecha que despliega un calendario
fecha.setDate(QDate.currentDate())        # fecha inicial: hoy
fecha.setMinimumDate(QDate(2006, 1, 1))   # no deja elegir antes de esta fecha
fecha.setMaximumDate(QDate(2030, 12, 31))
fecha.setDisplayFormat("dd/MM/yyyy")      # cómo se muestra
```

**Leer**: `fecha.date()` (devuelve un `QDate`).
**Señal**: `dateChanged(QDate)`.

### 5.12 `QDate` — Fechas

No es un widget, pero lo usan el calendario y el campo de fecha.

```python
from PyQt6.QtCore import QDate

d = QDate(2006, 1, 1)               # año, mes, día
hoy = QDate.currentDate()
hoy.toString("dd/MM/yyyy")          # "22/10/2026"
hoy.year(), hoy.month(), hoy.day()
hoy.addDays(7)                      # dentro de una semana
```

Formato: `dd` día, `MM` mes (**mayúscula**; `mm` son minutos), `yyyy` año, `dddd` nombre del día, `MMMM` nombre del mes.

---

## 6. Fuentes y colores

### 6.1 Fuente (`QFont`)

**Forma 1: obtener → modificar → aplicar** (mantiene lo que ya tenía la fuente)

```python
etiqueta = QLabel("Hola")
fuente = etiqueta.font()      # 1. obtener la fuente actual
fuente.setPointSize(30)       # 2. modificarla
fuente.setFamily("Arial")
fuente.setBold(True)
fuente.setItalic(True)
fuente.setUnderline(True)
etiqueta.setFont(fuente)      # 3. aplicarla
```

**Forma 2: crear una fuente nueva**

```python
from PyQt6.QtGui import QFont

etiqueta.setFont(QFont("Arial", 30))
```

Sirve para cualquier widget con texto (`QCheckBox`, `QPushButton`…).

### 6.2 Color de fondo (`QPalette`)

Mismo patrón: obtener la paleta → cambiar un color → aplicarla.

```python
from PyQt6.QtGui import QColor, QPalette

widget.setAutoFillBackground(True)      # sin esto, el fondo NO se pinta
paleta = widget.palette()
paleta.setColor(QPalette.ColorRole.Window, QColor("red"))
widget.setPalette(paleta)
```

`QColor` acepta nombres (`"red"`, `"purple"`), hexadecimal (`"#ff8800"`) o RGB (`QColor(255, 136, 0)`).

Roles más usados: `Window` (fondo), `WindowText` (texto), `Button` (fondo de botón), `ButtonText`, `Base` (fondo de cajas de texto).

### 6.3 Widget de color reutilizable

Muy útil para **practicar layouts**, porque se ve claramente dónde queda cada cosa:

```python
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)
```

Se guarda en un fichero (por ejemplo `cuadrado.py`) y se importa donde haga falta:

```python
from cuadrado import Color

rojo = Color("red")
```

En el resto de los apuntes `Color("…")` es esta clase: un rectángulo de color.

---

## 7. Layouts: colocar varios widgets

Un **layout** coloca y redimensiona los widgets automáticamente cuando cambia el tamaño de la ventana.

| Layout | Coloca los widgets… |
|---|---|
| `QHBoxLayout` | en **fila** (de izquierda a derecha) |
| `QVBoxLayout` | en **columna** (de arriba abajo) |
| `QGridLayout` | en **cuadrícula** (fila, columna) |
| `QStackedLayout` | **uno encima de otro**; solo se ve uno (apartado 8) |

### 7.1 Los 5 pasos (siempre iguales)

```python
layout = QVBoxLayout()            # 1. crear el layout
layout.addWidget(QLabel("A"))     # 2. añadir widgets
layout.addWidget(QPushButton("B"))

contenedor = QWidget()            # 3. crear un widget contenedor vacío
contenedor.setLayout(layout)      # 4. darle el layout
self.setCentralWidget(contenedor) # 5. ponerlo en el centro de la ventana
```

¿Por qué el contenedor? Porque `QMainWindow` no acepta un layout directamente: su widget central tiene que ser **un widget**, y ese widget es el que lleva el layout.

### 7.2 `QHBoxLayout` y `QVBoxLayout`

```python
fila = QHBoxLayout()
fila.addWidget(Color("red"))
fila.addWidget(Color("green"))
fila.addWidget(Color("blue"))
```

```
┌─────┬─────┬─────┐
│ red │green│blue │
└─────┴─────┴─────┘
```

Con `QVBoxLayout` quedarían uno debajo de otro.

**Métodos útiles**

```python
layout.addWidget(widget)          # añadir un widget
layout.addWidget(widget, 2)       # con "factor de estiramiento": ocupa el doble que uno con 1
layout.addLayout(otro_layout)     # meter un layout dentro de otro
layout.addStretch()               # espacio vacío elástico (empuja los widgets)
layout.setSpacing(20)             # separación entre widgets (px)
layout.setContentsMargins(10, 10, 10, 10)   # margen: izquierda, arriba, derecha, abajo
```

### 7.3 Layouts anidados

Combinando filas y columnas se puede construir cualquier diseño. Se usa **`addLayout`** para meter un layout dentro de otro.

```python
principal = QHBoxLayout()

columna1 = QVBoxLayout()
columna1.addWidget(Color("red"))
columna1.addWidget(Color("green"))

columna2 = QVBoxLayout()
columna2.addWidget(Color("grey"))
columna2.addWidget(Color("blue"))

principal.addLayout(columna1)
principal.addLayout(columna2)
principal.addWidget(Color("yellow"))
```

```
┌─────┬─────┬──────┐
│ red │grey │      │
├─────┼─────┤yellow│
│green│blue │      │
└─────┴─────┴──────┘
```

**Ejemplo: formulario sencillo**

```python
principal = QVBoxLayout()

fila = QHBoxLayout()
fila.addWidget(QLabel("Nombre:"))
fila.addWidget(QLineEdit())

opciones = QVBoxLayout()
opciones.addWidget(QCheckBox("Opción 1"))
opciones.addWidget(QCheckBox("Opción 2"))

principal.addLayout(fila)
principal.addLayout(opciones)
```

```
┌─────────────────────────┐
│ Nombre: [_____________] │
│ ☐ Opción 1              │
│ ☐ Opción 2              │
└─────────────────────────┘
```

> Truco: antes de programar, **dibuja el diseño** en papel y marca qué es fila (H) y qué es columna (V). Luego se programa de dentro hacia fuera.

### 7.4 `QGridLayout` — Cuadrícula

```python
rejilla = QGridLayout()
rejilla.addWidget(Color("red"),    0, 0)    # (widget, fila, columna)
rejilla.addWidget(Color("green"),  0, 1)
rejilla.addWidget(Color("yellow"), 1, 2)
rejilla.addWidget(Color("blue"),   2, 0)
```

```
┌──────┬──────┬──────┐   fila 0
│ red  │green │      │
├──────┼──────┼──────┤   fila 1
│      │      │yellow│
├──────┼──────┼──────┤   fila 2
│ blue │      │      │
└──────┴──────┴──────┘
```

- Filas y columnas empiezan en **0**; las celdas sin widget quedan vacías.
- Para que un widget **ocupe varias celdas**: `addWidget(widget, fila, columna, nº_filas, nº_columnas)`.

```python
rejilla.addWidget(QLabel("Título"), 0, 0, 1, 3)   # fila 0, ocupa 3 columnas
```

Muy cómodo para formularios (etiqueta en la columna 0, campo en la 1):

```python
form = QGridLayout()
form.addWidget(QLabel("Nombre"), 0, 0)
form.addWidget(QLineEdit(),      0, 1)
form.addWidget(QLabel("Edad"),   1, 0)
form.addWidget(QSpinBox(),       1, 1)
```

### 7.5 Márgenes y espaciado

```python
layout.setContentsMargins(10, 10, 10, 10)   # izquierda, arriba, derecha, abajo
layout.setSpacing(20)                       # hueco entre un widget y el siguiente
```

```
         margen superior (10)
      ┌─────────────────────┐
  10  │ [     Botón 1     ] │  10
      │        ↕ 20         │
      │ [     Botón 2     ] │
      └─────────────────────┘
         margen inferior (10)
```

### 7.6 `QGroupBox` — Agrupar con un marco y título

Un `QGroupBox` es un contenedor con borde y título. Tiene **su propio layout**.

```python
grupo = QGroupBox("Tamaño")
interior = QVBoxLayout()
interior.addWidget(QRadioButton("Pequeño"))
interior.addWidget(QRadioButton("Grande"))
grupo.setLayout(interior)        # el grupo lleva su layout

principal.addWidget(grupo)       # y el grupo se añade como un widget más
```

```
┌─ Tamaño ───────┐
│ ○ Pequeño      │
│ ○ Grande       │
└────────────────┘
```

Además de ordenar visualmente, hace que los `QRadioButton` de **cada grupo** sean excluyentes **solo entre ellos**:

```python
grupo_tamaño = QGroupBox("Tamaño")   # Pequeño / Grande  → se elige uno
grupo_color  = QGroupBox("Color")    # Rojo / Azul       → se elige otro, independiente
```

---

## 8. Páginas y pestañas

Cuando no caben todos los widgets a la vez, se reparten en **páginas** y se muestra una sola.

### 8.1 `QStackedLayout` — Páginas apiladas

Coloca los widgets uno encima de otro; **solo se ve uno**. No trae botones: la página se cambia **por código**.

```python
paginas = QStackedLayout()
paginas.addWidget(Color("red"))      # índice 0
paginas.addWidget(Color("blue"))     # índice 1
paginas.addWidget(Color("purple"))   # índice 2

paginas.setCurrentIndex(2)           # se ve la morada
paginas.currentIndex()               # → 2
```

**Pestañas hechas a mano**: botones arriba que cambian la página de abajo.

```python
principal = QVBoxLayout()
botones = QHBoxLayout()
paginas = QStackedLayout()

for i, color in enumerate(["red", "green", "yellow"]):
    boton = QPushButton(color)
    boton.clicked.connect(lambda _, i=i: paginas.setCurrentIndex(i))
    botones.addWidget(boton)
    paginas.addWidget(Color(color))

principal.addLayout(botones)
principal.addLayout(paginas)
```

> En el bucle se usa `i=i` dentro de la `lambda` para que cada botón **guarde su propio número**. Sin eso, todos usarían el último valor de `i`. El `_` recoge el `bool` que envía `clicked` y que no necesitamos.
> Sin bucle es más sencillo: `boton_rojo.clicked.connect(lambda: paginas.setCurrentIndex(0))`.

### 8.2 `QTabWidget` — Pestañas

Hace lo mismo que lo anterior pero **con las pestañas ya hechas**. Es lo normal para aplicaciones con pestañas.

**Instanciación**

```python
pestañas = QTabWidget()
pestañas.addTab(Color("red"),   "Rojo")      # addTab(widget, "texto de la pestaña")
pestañas.addTab(Color("green"), "Verde")
pestañas.addTab(Color("blue"),  "Azul")
self.setCentralWidget(pestañas)
```

```
┌──────┬───────┬──────┐
│ Rojo │ Verde │ Azul │
├──────┴───────┴──────┴────────┐
│                              │
│   contenido de la pestaña    │
│                              │
└──────────────────────────────┘
```

**Configuración**

```python
pestañas.setTabPosition(QTabWidget.TabPosition.North)  # North (arriba), South, West, East
pestañas.setMovable(True)          # se pueden reordenar arrastrando
pestañas.setTabsClosable(True)     # cada pestaña tiene una X para cerrarla
pestañas.setDocumentMode(True)     # aspecto plano, tipo navegador
```

**Métodos**

| Método | Para qué |
|---|---|
| `addTab(widget, "texto")` | Añadir pestaña al final |
| `addTab(widget, QIcon("ruta"), "texto")` | Pestaña con icono |
| `insertTab(posición, widget, "texto")` | Insertar en una posición |
| `removeTab(índice)` | Quitar una pestaña |
| `setCurrentIndex(i)` / `currentIndex()` | Ir a / saber qué pestaña está activa |
| `setTabText(i, "texto")` | Cambiar el título de una pestaña |
| `count()` | Número de pestañas |

**Señales**

| Señal | Cuándo | Envía |
|---|---|---|
| `currentChanged` | Al cambiar de pestaña | `int` (índice nuevo) |
| `tabCloseRequested` | Al pulsar la X de una pestaña | `int` (índice) |

```python
pestañas.setTabsClosable(True)
pestañas.tabCloseRequested.connect(pestañas.removeTab)    # la X cierra la pestaña
pestañas.currentChanged.connect(lambda i: print("Pestaña", i))
```

**Cada pestaña puede tener su propio layout**: se crea un `QWidget`, se le pone un layout con lo que queramos y se añade como pestaña.

```python
def crear_pestaña_datos(self):
    pagina = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QLabel("Nombre"))
    layout.addWidget(QLineEdit())
    layout.addWidget(QPushButton("Guardar"))
    pagina.setLayout(layout)
    return pagina

pestañas.addTab(self.crear_pestaña_datos(), "Datos")
```

---

## 9. Barra de herramientas, menús y barra de estado

### 9.1 `QAction` — Una acción reutilizable

Una **acción** es una orden de la aplicación ("Guardar", "Abrir"…). Se define **una vez** (icono, texto, ayuda, atajo y qué hace) y se coloca en la barra de herramientas, en los menús o en ambos.

```python
from PyQt6.QtGui import QAction, QIcon, QKeySequence

accion_guardar = QAction(QIcon("icons/disk.png"), "Guardar", self)
accion_guardar.setStatusTip("Guarda el documento")     # texto en la barra de estado
accion_guardar.setShortcut(QKeySequence("Ctrl+S"))      # atajo de teclado
accion_guardar.triggered.connect(self.guardar)          # su señal es triggered
```

- Constructor: `QAction(icono, "texto", self)` o `QAction("texto", self)` sin icono.
- La señal es **`triggered`** (no `clicked`). Envía un `bool` (`False` si la acción no es *checkable*).
- `setCheckable(True)` → la acción funciona como interruptor (marcada / no marcada).

### 9.2 `QToolBar` — Barra de herramientas

```python
barra = QToolBar("Barra principal")
barra.setIconSize(QSize(16, 16))      # tamaño de los iconos
self.addToolBar(barra)                # añadirla a la ventana

barra.addAction(accion_guardar)       # botón con la acción
barra.addSeparator()                  # línea separadora
barra.addWidget(QLabel("Buscar:"))    # también admite widgets normales
barra.addWidget(QLineEdit())
```

### 9.3 Menús

```python
menu = self.menuBar()                     # barra de menús de la ventana

menu_archivo = menu.addMenu("&Archivo")   # & → letra subrayada y atajo Alt+A
menu_archivo.addAction(accion_guardar)    # la MISMA acción que en la barra
menu_archivo.addSeparator()

submenu = menu_archivo.addMenu("Exportar")   # submenú: un menú dentro de otro
submenu.addAction(accion_pdf)

menu_editar = menu.addMenu("&Editar")
```

```
 Archivo   Editar
┌───────────────┐
│ 💾 Guardar    │
│───────────────│
│ Exportar    ▶ │──┐
└───────────────┘  │ PDF │
```

### 9.4 `QStatusBar` — Barra de estado

```python
self.setStatusBar(QStatusBar(self))

self.statusBar().showMessage("Guardado", 3000)   # mensaje durante 3 segundos
```

> El `setStatusTip` de las acciones **solo se ve si la ventana tiene barra de estado**.

### 9.5 Ejemplo

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barras y menús")

        self.veces = 0
        self.etiqueta = QLabel("Pulsa el bicho")
        self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.etiqueta)

        # Acción
        accion = QAction(QIcon("icons/bug.png"), "Contar", self)
        accion.setStatusTip("Suma uno al contador")
        accion.triggered.connect(self.contar)

        # Barra de herramientas
        barra = QToolBar("Herramientas")
        barra.setIconSize(QSize(32, 32))
        self.addToolBar(barra)
        barra.addAction(accion)

        # Menú
        menu_archivo = self.menuBar().addMenu("&Archivo")
        menu_archivo.addAction(accion)

        # Barra de estado
        self.setStatusBar(QStatusBar(self))

    def contar(self):
        self.veces += 1
        self.etiqueta.setText(f"Pulsado {self.veces} veces")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
```

---

## 10. Cuadros de diálogo

Un diálogo es una ventana pequeña para **avisar o preguntar** algo. Con `exec()` se abre en modo **modal**: la ventana principal queda bloqueada hasta que se cierra el diálogo, y `exec()` devuelve la respuesta.

### 10.1 `QDialog` — Diálogo básico

```python
from PyQt6.QtWidgets import QDialog

def abrir_dialogo(self):
    dlg = QDialog(self)              # self = ventana padre
    dlg.setWindowTitle("Diálogo")
    dlg.exec()
```

Pasar **`self` como padre** hace que el diálogo aparezca **centrado sobre** la ventana principal.

### 10.2 Diálogo propio con `QDialogButtonBox`

Lo habitual es crear una **clase** que herede de `QDialog`, con su contenido y sus botones:

```python
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class MiDialogo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmación")

        botones = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.caja_botones = QDialogButtonBox(botones)
        self.caja_botones.accepted.connect(self.accept)   # OK     → accept()
        self.caja_botones.rejected.connect(self.reject)   # Cancel → reject()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("¿Seguro que quieres continuar?"))
        layout.addWidget(self.caja_botones)
        self.setLayout(layout)       # un QDialog sí admite setLayout directamente
```

Uso:

```python
def preguntar(self):
    dlg = MiDialogo(self)
    if dlg.exec():                   # 1 si se aceptó, 0 si se canceló
        print("Aceptado")
    else:
        print("Cancelado")
```

- `QDialogButtonBox` coloca los botones en el orden correcto de cada sistema operativo.
- Botones estándar (se combinan con `|`): `Ok`, `Cancel`, `Yes`, `No`, `Save`, `Close`, `Apply`, `Abort`, `Retry`, `Ignore`…
- `accept()` y `reject()` cierran el diálogo y hacen que `exec()` devuelva `1` o `0`.
- Es buena práctica tener los diálogos en un fichero aparte (`dialogs.py`) e importarlos: `from dialogs import MiDialogo`.

### 10.3 `QMessageBox` — Mensajes ya preparados

**Forma completa**

```python
from PyQt6.QtWidgets import QMessageBox

dlg = QMessageBox(self)
dlg.setWindowTitle("Pregunta")
dlg.setText("¿Quieres guardar los cambios?")
dlg.setIcon(QMessageBox.Icon.Question)
dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

respuesta = dlg.exec()
if respuesta == QMessageBox.StandardButton.Yes:
    print("Sí")
```

Aquí `exec()` devuelve **el botón pulsado**, por eso se compara con `StandardButton.Yes`.

Iconos: `NoIcon`, `Question` (?), `Information` (i), `Warning` (!), `Critical` (X).

**Forma corta: métodos estáticos** (crean, muestran y devuelven el resultado en una línea)

```python
respuesta = QMessageBox.question(self, "Título", "¿Seguro?")
if respuesta == QMessageBox.StandardButton.Yes:
    ...

QMessageBox.information(self, "Título", "Operación completada")
QMessageBox.warning(self, "Título", "Cuidado con esto")
QMessageBox.critical(self, "Título", "Ha ocurrido un error")
```

---

## 11. Varias ventanas

### 11.1 Crear una segunda ventana

Un **`QWidget` sin padre** se muestra como una ventana independiente. A diferencia de un diálogo con `exec()`, **no bloquea** la ventana principal.

```python
class OtraVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Otra ventana")
        layout = QVBoxLayout()
        self.etiqueta = QLabel("Soy otra ventana")
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)        # un QWidget sí admite setLayout directamente
```

Para abrirla desde la principal:

```python
def abrir(self):
    self.ventana = OtraVentana()      # con self.
    self.ventana.show()
```

> Hay que guardarla en **`self.`**: si fuera una variable local, Python la borraría al terminar el método y la ventana se cerraría al instante.
> Evita llamar al atributo `self.window`, porque las ventanas ya tienen un método `window()` y lo taparías.

### 11.2 Dos formas de abrir y cerrar con el mismo botón

**A) Crear y destruir** — la ventana se crea de cero cada vez (pierde lo que tuviera):

```python
def __init__(self):
    ...
    self.ventana = None

def alternar(self):
    if self.ventana is None:
        self.ventana = OtraVentana()
        self.ventana.show()
    else:
        self.ventana.close()
        self.ventana = None
```

**B) Mostrar y ocultar** — la ventana se crea una vez y conserva su estado:

```python
def __init__(self):
    ...
    self.ventana = OtraVentana()      # se crea al principio

def alternar(self):
    if self.ventana.isVisible():
        self.ventana.hide()
    else:
        self.ventana.show()
```

| | Crear / destruir | Mostrar / ocultar |
|---|---|---|
| Cuándo se crea | Cada vez que se abre | Una vez, al iniciar |
| Al cerrar | `close()` + `None` | `hide()` |
| Conserva lo escrito | ❌ | ✅ |

### 11.3 Pasar datos entre ventanas

Como la segunda ventana guarda su etiqueta en `self.etiqueta`, se puede acceder a ella desde la principal y conectarle señales:

```python
self.ventana = OtraVentana()
self.caja = QLineEdit()
self.caja.textChanged.connect(self.ventana.etiqueta.setText)
```

Lo que se escribe en la ventana principal aparece **en directo** en la otra.

---

## 12. Ejemplo completo: todo junto

Aplicación con pestañas, formulario con distintos widgets, barra de herramientas, menú, barra de estado y diálogo de confirmación.

```python
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit, QSpinBox, QComboBox, QCheckBox,
    QRadioButton, QDateEdit, QPushButton, QListWidget, QSlider, QToolBar,
    QStatusBar, QMessageBox,
)
from PyQt6.QtCore import Qt, QSize, QDate
from PyQt6.QtGui import QAction, QIcon, QKeySequence


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de alumnos")
        self.resize(500, 400)

        # ---------- Pestañas ----------
        self.pestañas = QTabWidget()
        self.pestañas.addTab(self.pestaña_formulario(), "Alta")
        self.pestañas.addTab(self.pestaña_lista(), "Listado")
        self.pestañas.currentChanged.connect(
            lambda i: self.statusBar().showMessage(f"Pestaña {self.pestañas.tabText(i)}")
        )
        self.setCentralWidget(self.pestañas)

        # ---------- Acción, barra y menú ----------
        accion_guardar = QAction(QIcon("icons/disk.png"), "Guardar", self)
        accion_guardar.setStatusTip("Guarda el alumno")
        accion_guardar.setShortcut(QKeySequence("Ctrl+S"))
        accion_guardar.triggered.connect(self.guardar)

        barra = QToolBar("Herramientas")
        barra.setIconSize(QSize(16, 16))
        barra.addAction(accion_guardar)
        self.addToolBar(barra)

        menu_archivo = self.menuBar().addMenu("&Archivo")
        menu_archivo.addAction(accion_guardar)

        self.setStatusBar(QStatusBar(self))

    # Pestaña 1: formulario
    def pestaña_formulario(self):
        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Nombre y apellidos")

        self.edad = QSpinBox()
        self.edad.setRange(16, 99)
        self.edad.setSuffix(" años")

        self.ciclo = QComboBox()
        self.ciclo.addItems(["DAM", "DAW", "ASIR"])

        self.nacimiento = QDateEdit(QDate(2006, 1, 1))
        self.nacimiento.setCalendarPopup(True)
        self.nacimiento.setDisplayFormat("dd/MM/yyyy")

        form = QGridLayout()
        form.addWidget(QLabel("Nombre"), 0, 0)
        form.addWidget(self.nombre, 0, 1)
        form.addWidget(QLabel("Edad"), 1, 0)
        form.addWidget(self.edad, 1, 1)
        form.addWidget(QLabel("Ciclo"), 2, 0)
        form.addWidget(self.ciclo, 2, 1)
        form.addWidget(QLabel("Nacimiento"), 3, 0)
        form.addWidget(self.nacimiento, 3, 1)

        # Turno: radio buttons dentro de un grupo
        self.mañana = QRadioButton("Mañana")
        self.mañana.setChecked(True)
        self.tarde = QRadioButton("Tarde")
        turno_layout = QHBoxLayout()
        turno_layout.addWidget(self.mañana)
        turno_layout.addWidget(self.tarde)
        turno = QGroupBox("Turno")
        turno.setLayout(turno_layout)

        self.beca = QCheckBox("Tiene beca")

        self.nota = QSlider(Qt.Orientation.Horizontal)
        self.nota.setRange(0, 10)
        etiqueta_nota = QLabel("Nota: 0")
        self.nota.valueChanged.connect(lambda v: etiqueta_nota.setText(f"Nota: {v}"))

        boton = QPushButton("Guardar")
        boton.clicked.connect(self.guardar)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(turno)
        layout.addWidget(self.beca)
        layout.addWidget(etiqueta_nota)
        layout.addWidget(self.nota)
        layout.addStretch()
        layout.addWidget(boton)

        pagina = QWidget()
        pagina.setLayout(layout)
        return pagina

    # Pestaña 2: listado
    def pestaña_lista(self):
        self.lista = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.lista)
        pagina = QWidget()
        pagina.setLayout(layout)
        return pagina

    def guardar(self):
        if not self.nombre.text():
            QMessageBox.warning(self, "Falta el nombre", "Escribe un nombre")
            return

        respuesta = QMessageBox.question(self, "Confirmar", f"¿Guardar a {self.nombre.text()}?")
        if respuesta == QMessageBox.StandardButton.Yes:
            turno = "mañana" if self.mañana.isChecked() else "tarde"
            texto = (f"{self.nombre.text()} · {self.edad.value()} años · "
                     f"{self.ciclo.currentText()} · {turno} · "
                     f"nota {self.nota.value()}"
                     f"{' · beca' if self.beca.isChecked() else ''}")
            self.lista.addItem(texto)
            self.nombre.clear()
            self.pestañas.setCurrentIndex(1)   # saltar al listado
            self.statusBar().showMessage("Alumno guardado", 3000)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
```

---

## 13. Chuleta de señales

| Widget | Señal | Envía |
|---|---|---|
| `QPushButton` | `clicked` | `bool` |
| `QPushButton` | `pressed` / `released` | — |
| `QPushButton` (checkable) | `toggled` | `bool` |
| `QLineEdit` | `textChanged` | `str` |
| `QLineEdit` | `returnPressed` / `editingFinished` | — |
| `QCheckBox` | `stateChanged` | `int` (0, 1, 2) |
| `QCheckBox` / `QRadioButton` | `toggled` | `bool` |
| `QComboBox` | `currentIndexChanged` | `int` |
| `QComboBox` / `QListWidget` | `currentTextChanged` | `str` |
| `QListWidget` | `currentRowChanged` | `int` |
| `QListWidget` | `itemSelectionChanged` | — |
| `QSpinBox` | `valueChanged` | `int` |
| `QSpinBox` | `textChanged` | `str` (con prefijo/sufijo) |
| `QSlider` / `QDial` | `valueChanged` / `sliderMoved` | `int` |
| `QCalendarWidget` | `selectionChanged` | — (usar `selectedDate()`) |
| `QCalendarWidget` | `clicked` | `QDate` |
| `QDateEdit` | `dateChanged` | `QDate` |
| `QTabWidget` | `currentChanged` / `tabCloseRequested` | `int` |
| `QAction` | `triggered` | `bool` |
| `QDialogButtonBox` | `accepted` / `rejected` | — |

---

## 14. Errores típicos

| Error | Qué pasa | Solución |
|---|---|---|
| `connect(self.metodo())` con paréntesis | Se ejecuta una vez al conectar, no al pulsar | `connect(self.metodo)` sin paréntesis, o `lambda` si hay argumentos |
| `setChecked(True)` antes de `setCheckable(True)` | No tiene efecto: el botón empieza sin marcar | Primero `setCheckable(True)`, luego `setChecked(True)` |
| `self.setLayout(layout)` en una `QMainWindow` | No funciona (avisa de que ya tiene layout) | Widget contenedor + `setLayout` + `setCentralWidget` |
| Llamar dos veces a `setCentralWidget` | Solo queda el último widget | Meter todos en un layout dentro de un contenedor |
| Conectar `valueChanged` y `textChanged` (o `sliderMoved`) al mismo slot | El slot se ejecuta dos veces | Conectar solo una señal |
| Segunda ventana en variable local | Se cierra al instante | Guardarla en `self.ventana` |
| Imagen o icono que no aparece | La ruta relativa depende de la carpeta desde la que ejecutas | Ejecutar desde la carpeta correcta o usar rutas absolutas |
| No se ve el color de fondo | Falta `setAutoFillBackground(True)` | Añadirlo antes de cambiar la paleta |
| No se ve el `setStatusTip` | La ventana no tiene barra de estado | `self.setStatusBar(QStatusBar(self))` |
| `ImportError` con `QAction` | Se importó de `QtWidgets` | Importar de `PyQt6.QtGui` |
| Formato de fecha con `mm` | `mm` son minutos | Mes con `MM` mayúscula: `"dd/MM/yyyy"` |
| `lambda` en un bucle | Todas usan el último valor | `lambda _, i=i: ...` |

---

## 15. Preguntas de repaso

<details>
<summary>1. ¿Por qué no se puede llamar a <code>setLayout()</code> directamente sobre una <code>QMainWindow</code>?</summary>

Porque `QMainWindow` ya tiene su propio layout interno (menús, barras, zona central). Se crea un `QWidget` contenedor, se le pone el layout y se usa `setCentralWidget(contenedor)`.
</details>

<details>
<summary>2. ¿De qué módulo se importan <code>QAction</code>, <code>QSize</code> y <code>QLabel</code>?</summary>

`QAction` de `PyQt6.QtGui`, `QSize` de `PyQt6.QtCore` y `QLabel` de `PyQt6.QtWidgets`.
</details>

<details>
<summary>3. ¿Qué diferencia hay entre <code>clicked</code>, <code>pressed</code> y <code>released</code>?</summary>

`pressed` al hundir el botón, `released` al soltarlo y `clicked` cuando se completa el clic (pulsar y soltar encima del botón).
</details>

<details>
<summary>4. ¿Qué valores envía <code>stateChanged</code> de un <code>QCheckBox</code>?</summary>

Un entero: 0 desmarcada, 1 parcialmente marcada (solo con `setTristate(True)`) y 2 marcada.
</details>

<details>
<summary>5. ¿Qué diferencia hay entre <code>QCheckBox</code> y <code>QRadioButton</code>?</summary>

Las casillas son independientes (se pueden marcar varias). Los radio buttons son excluyentes: dentro del mismo contenedor solo puede haber uno marcado.
</details>

<details>
<summary>6. ¿Para qué sirve <code>self.sender()</code>?</summary>

Dentro de un slot compartido por varios widgets, devuelve el widget que ha emitido la señal (por ejemplo, para leer su `text()`).
</details>

<details>
<summary>7. ¿Cómo se haría que un widget ocupe dos columnas en un <code>QGridLayout</code>?</summary>

`rejilla.addWidget(widget, fila, columna, 1, 2)`: los dos últimos números son las filas y columnas que ocupa.
</details>

<details>
<summary>8. ¿Qué diferencia hay entre <code>QStackedLayout</code> y <code>QTabWidget</code>?</summary>

Los dos muestran una sola página de varias. `QStackedLayout` no trae controles: la página se cambia por código (`setCurrentIndex`). `QTabWidget` trae las pestañas ya hechas para que el usuario cambie de página.
</details>

<details>
<summary>9. ¿Cómo se consigue que cada pestaña de un <code>QTabWidget</code> tenga varios widgets?</summary>

Se crea un `QWidget`, se le pone un layout con los widgets y se añade con `addTab(widget, "texto")`.
</details>

<details>
<summary>10. ¿Qué ventaja tiene <code>QAction</code> frente a poner botones en barras y menús?</summary>

Una sola acción (icono, texto, ayuda, atajo y slot) se reutiliza en la barra de herramientas y en los menús sin repetir código.
</details>

<details>
<summary>11. ¿Qué devuelve <code>exec()</code> en un <code>QDialog</code> y en un <code>QMessageBox</code>?</summary>

En un `QDialog`, 1 si se llamó a `accept()` y 0 si se llamó a `reject()`. En un `QMessageBox`, el botón pulsado (por ejemplo `QMessageBox.StandardButton.Yes`).
</details>

<details>
<summary>12. ¿Qué diferencia hay entre cerrar una ventana con <code>close()</code> + <code>None</code> y ocultarla con <code>hide()</code>?</summary>

Con `close()` + `None` se destruye y al abrirla se crea de nuevo (pierde lo que tuviera). Con `hide()` / `show()` es siempre la misma ventana y conserva su estado.
</details>
