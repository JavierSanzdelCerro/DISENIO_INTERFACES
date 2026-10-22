# Apuntes de PyQt6 — Carpeta `DiseñoPestañas`

Resumen de todos los ejercicios de la carpeta, ordenados de más sencillo a más completo.
Para cada uno: qué hace, qué conceptos enseña y los detalles a tener en cuenta.

**Índice**

0. [Esqueleto común de todos los ejercicios](#0-esqueleto-común-de-todos-los-ejercicios)
1. [Widgets básicos (`widgets/`)](#1-widgets-básicos-carpeta-widgets)
2. [Layouts (`Layouts/`)](#2-layouts-carpeta-layouts)
3. [Pestañas y vistas apiladas](#3-pestañas-y-vistas-apiladas)
4. [Barra de herramientas, menús y barra de estado](#4-barra-de-herramientas-menús-y-barra-de-estado)
5. [Cuadros de diálogo](#5-cuadros-de-diálogo)
6. [Varias ventanas](#6-varias-ventanas)
7. [Tabla resumen de señales](#7-tabla-resumen-de-señales)
8. [Errores y detalles a vigilar](#8-errores-y-detalles-a-vigilar)
9. [Cómo ejecutar los ejercicios](#9-cómo-ejecutar-los-ejercicios)
10. [Preguntas de repaso](#10-preguntas-de-repaso)

---

## 0. Esqueleto común de todos los ejercicios

Todos los ficheros siguen la misma estructura:

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):          # 1. Heredamos de QMainWindow
    def __init__(self):
        super().__init__()              # 2. Llamamos al constructor del padre
        self.setWindowTitle("Mi Aplicacion")

        boton = QPushButton("Pulsa")    # 3. Creamos widgets
        boton.clicked.connect(self.botonPulsado)   # 4. Conectamos señal -> slot
        self.setCentralWidget(boton)    # 5. Ponemos un widget en el centro

    def botonPulsado(self):             # Slot: método que responde a la señal
        print("Botón pulsado")

app = QApplication([])   # Una sola QApplication por programa
window = MainWindow()
window.show()            # Las ventanas nacen ocultas: hay que mostrarlas
app.exec()               # Bucle de eventos: el programa se queda aquí esperando
```

Conceptos clave:

| Concepto | Qué es |
|---|---|
| `QApplication` | Gestiona la aplicación y el **bucle de eventos**. Se crea una vez. |
| `QMainWindow` | Ventana principal. Tiene huecos reservados: *central widget*, barra de menús, barra de herramientas y barra de estado. |
| `QWidget` | Clase base de todo lo visual. Un `QWidget` sin padre es una ventana. |
| **Señal** (*signal*) | Aviso que emite un widget cuando pasa algo (`clicked`, `textChanged`…). |
| **Slot** | Función/método que se ejecuta cuando llega la señal. Se une con `señal.connect(slot)`. |
| `setCentralWidget()` | `QMainWindow` solo admite **un** widget central. Para meter varios se usa un `QWidget` contenedor con un layout (ver apartado 2). |

> Con `self.` delante de una variable: se guarda como atributo y se puede usar en otros métodos (por ejemplo en el slot).
> Sin `self.`: es una variable local que solo existe dentro de `__init__`.

---

## 1. Widgets básicos (carpeta `widgets/`)

### 1.1 `ClaseCreaVentana.py` — Ventana de tamaño fijo

- Ventana con un botón "Pulsa" en el centro.
- `self.setFixedSize(QSize(400, 300))` → la ventana mide 400×300 y **no se puede redimensionar**.
- Variantes útiles: `setMinimumSize(QSize(...))` y `setMaximumSize(QSize(...))`.
- `QSize` se importa de `PyQt6.QtCore`.

### 1.2 `BotonConTextoAlPulsar.py` — Primera señal

- Al pulsar el botón se imprime `"Botón pulsado"` en la consola.
- `boton.clicked.connect(self.botonpulsado)`: se pasa el método **sin paréntesis** (se pasa la función, no se ejecuta).
- El `print("Hola")` dentro de `__init__` se ejecuta **una vez al crear la ventana**, no al pulsar.
- Tiene `setCheckable(True)` (botón de dos estados), aunque aquí no se usa el estado.

### 1.3 `EjerBotones.py` — `clicked`, `pressed` y `released`

Un mismo botón conectado a tres señales distintas:

| Señal | Cuándo se emite |
|---|---|
| `pressed` | Al **hundir** el botón del ratón |
| `released` | Al **soltar** el botón del ratón |
| `clicked` | Al hacer un clic **completo** (pulsar y soltar encima del botón) |

Orden en consola al hacer clic: `Botón pulsado` → `Botón Soltado` → `Botón pulsado y Soltado`.

### 1.4 `BotonPulsadoYNoPulsado.py` — Botón con estado (*checkable*)

```python
self.boton.setCheckable(True)
self.boton.clicked.connect(self.botonPulsado)

def botonPulsado(self, pulsado):        # clicked envía True/False
    self.boton.setText(["No pulsado", "Pulsado"][pulsado])
```

- Con `setCheckable(True)` el botón se queda hundido/levantado (como un interruptor).
- La señal `clicked` envía un `bool` con el estado nuevo.
- Truco: en Python `True == 1` y `False == 0`, así que se puede usar el booleano como **índice de una lista** para elegir el texto.
- El botón se guarda en `self.boton` porque hay que usarlo dentro del slot.

### 1.5 `EjercicioContador.py` — Consultar el estado con `isChecked()`

- Cada clic suma 1 a `self.contador` e imprime `self.boton.isChecked()` (`True`/`False`).
- **Ojo:** llama a `setChecked(True)` **antes** de `setCheckable(True)`. Como en ese momento el botón todavía no es *checkable*, `setChecked` no tiene efecto y el botón empieza **sin marcar**. Para que empiece marcado hay que invertir el orden:

  ```python
  self.boton.setCheckable(True)
  self.boton.setChecked(True)
  ```
- El contador se incrementa pero nunca se muestra (se podría hacer `print(self.contador)`).

### 1.6 `EjercicioCancelarBoton.py` — Desactivar un botón

- Igual que el anterior, pero en el slot hace `self.boton.setEnabled(False)`.
- Resultado: el botón **solo se puede pulsar una vez**; después queda gris y deja de responder.
- `setEnabled(True)` lo volvería a activar.

### 1.7 `TextoConFormato.py` — `QLabel` con fuente y alineación

```python
label = QLabel("Hola")
formato = label.font()          # 1. Obtener la fuente actual
formato.setPointSize(30)        # 2. Modificarla
formato.setFamily("Arial")
formato.setBold(True)
label.setFont(formato)          # 3. Volver a aplicarla
label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
```

- Patrón **obtener → modificar → aplicar** para la fuente.
- Las alineaciones se combinan con `|` (horizontal | vertical).
- `Qt.AlignmentFlag.AlignCenter` equivale a centrar en los dos ejes.

### 1.8 `EtiquetaConFoto.py` — Imagen en un `QLabel`

```python
label = QLabel()
label.setPixmap(QPixmap("Img/imagen-aleatoria-destacada.webp"))
```

- `QPixmap` (de `PyQt6.QtGui`) carga la imagen y `setPixmap` la muestra en la etiqueta.
- La ruta es **relativa a la carpeta desde donde se ejecuta** el script: hay que lanzarlo desde dentro de `widgets/` o no se verá la imagen (no da error, simplemente sale vacío).
- Extra: `label.setScaledContents(True)` hace que la imagen se adapte al tamaño de la ventana.

### 1.9 `InputYLabelConectados.py` — Conectar dos widgets entre sí + primer layout

```python
label = QLabel()
input = QLineEdit()
input.textChanged.connect(label.setText)   # lo que escribes aparece en la etiqueta

layout = QVBoxLayout()
layout.addWidget(input)
layout.addWidget(label)

contenedor = QWidget()
contenedor.setLayout(layout)
self.setCentralWidget(contenedor)
```

- Una señal se puede conectar **directamente al método de otro widget** (`label.setText`), sin escribir un slot propio.
- `textChanged` envía el texto nuevo, que `setText` recibe como parámetro.
- Es el primer ejercicio con **layout**: para tener varios widgets se meten en un layout, el layout en un `QWidget` contenedor y ese contenedor se pone como central.

### 1.10 `LineEdit.py` — Caja de texto

- `setMaxLength(10)` → como máximo 10 caracteres.
- `setPlaceholderText("Introduce tu nombre...")` → texto gris de ayuda que desaparece al escribir.
- `textChanged` → imprime el texto en cada pulsación de tecla.
- Otras señales útiles de `QLineEdit`: `returnPressed` (al pulsar Enter), `editingFinished` (al pulsar Enter o salir del campo).
- Otros métodos: `text()`, `setText()`, `setEchoMode(QLineEdit.EchoMode.Password)` para contraseñas.

### 1.11 `CheckBox.py` — Casilla de verificación

```python
self.casilla.stateChanged.connect(self.muestraEstado)

def muestraEstado(self, pulsado):
    self.casilla.setText(["No pulsado", "", "Pulsado"][pulsado])
```

- `stateChanged` envía un **entero**: `0` = desmarcada, `1` = parcialmente marcada, `2` = marcada.
- Por eso la lista tiene un hueco vacío `""` en la posición 1: el estado "parcial" solo aparece si se activa `setTristate(True)`.
- También pone la fuente en negrita con el patrón `font()` → `setBold(True)` → `setFont()`.
- `isChecked()` devuelve `True/False` si solo interesa saber si está marcada.

### 1.12 `ComboBox.py` — Lista desplegable

```python
lista = QComboBox()
lista.addItems(["Uno", "Dos", "Tres"])   # varios a la vez (lista)
lista.addItem("Cuatro")                  # uno solo
lista.setEditable(True)                  # el usuario puede escribir
lista.currentIndexChanged.connect(self.muestraIndice)   # envía int (posición)
lista.currentTextChanged.connect(self.muestraTexto)     # envía str (texto)
```

- `addItems` (con **s**) recibe una lista; `addItem` un solo elemento.
- `currentIndexChanged` envía la **posición** (empieza en 0); `currentTextChanged` envía el **texto**.
- Con `setEditable(True)` se puede escribir; al pulsar Enter, el texto nuevo se añade al final de la lista.
- El parámetro de `muestraIndice` se llama `texto`, pero en realidad recibe un número.

### 1.13 `Lista.py` — Lista visible (`QListWidget`)

- Como el combo pero todos los elementos están siempre visibles.
- `currentTextChanged` imprime el elemento actual.
- `setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)` → permite seleccionar **varios** elementos haciendo clic.
- Para obtener todos los seleccionados: `[item.text() for item in lista.selectedItems()]`.
- El método `muestraIndice` está definido pero **no se conecta** a nada (se podría conectar a `currentRowChanged`).

### 1.14 `SpinBox.py` — Selector numérico

```python
spinBox.setRange(-10, 10)    # mínimo y máximo
spinBox.setSingleStep(2)     # cuánto sube/baja con cada flecha
spinBox.setSuffix(" €")      # texto detrás del número (también existe setPrefix)
spinBox.textChanged.connect(self.valorCambiado)    # envía "2 €" (str)
spinBox.valueChanged.connect(self.valorCambiado)   # envía 2 (int)
```

- Como están conectadas las dos señales al mismo slot, **cada cambio se imprime dos veces**: una como texto con sufijo y otra como número.
- Para decimales existe `QDoubleSpinBox`.

### 1.15 `slider.py` — Deslizador

- `QSlider(Qt.Orientation.Horizontal)` (o `Vertical`).
- `setRange(-10, 10)`.
- `valueChanged` → se emite con **cualquier** cambio (ratón, teclado, código).
- `sliderMoved` → solo mientras se **arrastra** con el ratón.
- Al arrastrar se imprime dos veces porque las dos señales van al mismo slot.

### 1.16 `dial.py` — Rueda giratoria

- `QDial` funciona igual que el slider pero con forma de rueda.
- `setNotchesVisible(True)` → muestra las marcas alrededor del dial.
- Mismas señales que el slider (`valueChanged`, `sliderMoved`).

### 1.17 `Calendario.py` — Calendario

```python
self.calendario = QCalendarWidget()
self.calendario.selectionChanged.connect(self.mostrarFecha)

def mostrarFecha(self):
    print(self.calendario.selectedDate().toString("dd/MM/yyyy"))
```

- `selectionChanged` **no envía la fecha**: hay que pedirla con `selectedDate()`, que devuelve un `QDate`.
- `toString("dd/MM/yyyy")` le da formato (`dd` día, `MM` mes —en mayúscula—, `yyyy` año).
- Alternativa: la señal `clicked` sí envía el `QDate` pulsado.

---

## 2. Layouts (carpeta `Layouts/`)

Un **layout** (plantilla) organiza automáticamente la posición y el tamaño de los widgets cuando cambia el tamaño de la ventana.

**Patrón que se repite en todos:**

```python
plantilla = QVBoxLayout()        # 1. Crear el layout
plantilla.addWidget(widget1)     # 2. Añadir widgets
plantilla.addLayout(otroLayout)  #    ...o layouts hijos
widget = QWidget()               # 3. Contenedor
widget.setLayout(plantilla)      # 4. Darle el layout al contenedor
self.setCentralWidget(widget)    # 5. Contenedor como widget central
```

| Layout | Organiza los widgets… |
|---|---|
| `QHBoxLayout` | en **fila** (horizontal, de izquierda a derecha) |
| `QVBoxLayout` | en **columna** (vertical, de arriba abajo) |
| `QGridLayout` | en **cuadrícula** (fila, columna) |
| `QStackedLayout` | **uno encima de otro**, solo se ve uno |

### 2.1 `cuadrado.py` — Widget auxiliar `Color`

No es un ejercicio en sí: es una clase que usan casi todos los demás.

```python
class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)          # que pinte su fondo
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)
```

- Crea un **rectángulo de color** para ver fácilmente dónde coloca cada layout sus widgets.
- Patrón **obtener paleta → cambiar color → aplicar** (igual que con la fuente).
- Sin `setAutoFillBackground(True)` el color no se ve.
- Se importa en otros ficheros con `from cuadrado import Color`. Funciona porque está en la **misma carpeta** que el script.

### 2.2 `layout_1.py` — `QHBoxLayout`

- Seis colores (`red`, `green`, `orange`, `grey`, `blue`, `purple`) en **una fila**, repartiendo el ancho a partes iguales.

### 2.3 `multiplesLayout.py` — Layouts anidados

```
plantilla1 (QHBoxLayout)
├── plantilla2 (QVBoxLayout): red, green, orange
├── plantilla3 (QVBoxLayout): grey, blue, purple
└── Color("yellow")
```

- Resultado: dos columnas de 3 colores y una franja amarilla a la derecha.
- `addLayout()` mete un layout dentro de otro; `addWidget()` mete un widget.

### 2.4 `botonesSimple.py` — Botones en filas

```
layout1 (QVBoxLayout)
├── layout2 (QHBoxLayout): Boton1, Boton2
└── layout3 (QHBoxLayout): Boton3
```

- Fila de arriba con dos botones y fila de abajo con uno que ocupa todo el ancho.

### 2.5 `layoutConBotones.py` y `layoutActivo.py` — Márgenes y espaciado

(Los dos ficheros tienen el **mismo código**.)

- Tres botones en vertical.
- `layout.setContentsMargins(10, 10, 10, 10)` → margen interior (**izquierda, arriba, derecha, abajo**).
- `layout.setSpacing(20)` → separación entre widgets, en píxeles.

### 2.6 `layoutCompleto.py` — Formulario sencillo + `sender()`

```
layout1 (QVBoxLayout)
├── layout2 (QHBoxLayout): QLabel("Texto"), QLineEdit
└── layout3 (QVBoxLayout): Opcion 1, Opcion 2, Opcion 3  (QCheckBox)
```

- Las tres casillas se conectan al **mismo slot** `checksel`.
- Dentro del slot, `self.sender()` devuelve **el widget que emitió la señal**, así se sabe qué casilla se ha pulsado:

  ```python
  def checksel(self, s):
      print(f"{self.sender().text()} - {['Desmarcado', '', 'Marcado'][s]}")
  ```
- En el original las comillas de dentro del f-string son dobles, igual que las de fuera. Eso solo funciona en **Python 3.12 o superior**; con comillas simples dentro funciona en cualquier versión.

### 2.7 `gridLayout.py` — `QGridLayout`

```python
plantilla.addWidget(Color("red"),    0, 0)   # fila 0, columna 0
plantilla.addWidget(Color("green"),  0, 1)
plantilla.addWidget(Color("yellow"), 1, 2)
plantilla.addWidget(Color("blue"),   2, 0)
```

- `addWidget(widget, fila, columna)`; filas y columnas empiezan en 0.
- Se crea una cuadrícula de 3×3 con huecos donde no hay nada.
- Para que un widget ocupe varias celdas: `addWidget(widget, fila, col, nFilas, nColumnas)`.

### 2.8 `widgetsAgrupados.py` — `QGroupBox` y `QRadioButton`

- Dos cajas con título (`QGroupBox`): una con 3 `QPushButton` y otra con 3 `QRadioButton`, colocadas en horizontal.
- Cada `QGroupBox` tiene **su propio layout** (`grupo.setLayout(layout)`) y luego el grupo se añade al layout general.
- Los `QRadioButton` dentro del mismo grupo son **excluyentes**: solo puede haber uno marcado a la vez (lo hace Qt automáticamente porque comparten padre).
- Todos se conectan al mismo slot y se usa `self.sender().text()` para saber cuál se ha pulsado.
- Detalles: los dos grupos se llaman `"Botones"` (el segundo debería ser algo como `"Radios"`) y `layout4` se crea pero no se usa.

---

## 3. Pestañas y vistas apiladas

### 3.1 `widgetsSuperPuestos.py` — `QStackedLayout`

- Cinco colores apilados uno encima de otro; **solo se ve uno**.
- `plantilla.setCurrentIndex(2)` → se muestra el tercero (índice 2) = **morado** (`purple`).
- Es la base de las pestañas: varias "páginas" y se elige cuál se ve.

### 3.2 `HBox-VBoxConBotones.py` — Pestañas "hechas a mano"

```
plantilla (QVBoxLayout)
├── botones (QHBoxLayout): red, green, yellow  (QPushButton)
└── colores (QStackedLayout): Color red, green, yellow
```

```python
botonRed.pressed.connect(lambda: colores.setCurrentIndex(0))
```

- Cada botón cambia la página visible del `QStackedLayout`.
- Se usa **`lambda`** porque `connect` necesita una función, y queremos llamar a `setCurrentIndex` **con un argumento** concreto. Sin `lambda` se ejecutaría en el momento de conectar.

### 3.3 `pestañas.py` — `QTabWidget` ⭐ (el ejercicio que da nombre a la carpeta)

```python
tabs = QTabWidget()
tabs.setTabPosition(QTabWidget.TabPosition.North)   # pestañas arriba
tabs.setMovable(True)                               # se pueden arrastrar

tabs.addTab(Color("red"),    "rojo")
tabs.addTab(Color("green"),  "verde")
tabs.addTab(Color("blue"),   "azul")
tabs.addTab(Color("yellow"), "yellow")

self.setCentralWidget(tabs)
```

- `QTabWidget` hace lo mismo que el ejercicio anterior (botones + `QStackedLayout`) pero **automáticamente**.
- `addTab(widget, "texto de la pestaña")`: cada pestaña es un widget (aquí un color, pero puede ser un `QWidget` con su propio layout y formulario).
- Posiciones posibles: `North` (arriba), `South` (abajo), `West` (izquierda), `East` (derecha).
- `setMovable(True)` permite reordenar las pestañas arrastrándolas.
- `setCentralWidget(tabs)` aparece dos veces; sobra una, pero no da error.
- Extras útiles:
  - `tabs.currentChanged.connect(slot)` → avisa al cambiar de pestaña (envía el índice).
  - `tabs.setTabsClosable(True)` + señal `tabCloseRequested` → pestañas con botón de cerrar.
  - `tabs.setDocumentMode(True)` → aspecto más plano, tipo navegador.

### 3.4 `pestañas2.py`

- El fichero está **vacío** (sin empezar).

---

## 4. Barra de herramientas, menús y barra de estado

### 4.1 `toolBar.py` — `QToolBar`, `QAction`, menús y `QStatusBar`

```python
barra = QToolBar("Barra de herramientas")
barra.setIconSize(QSize(16, 16))
self.addToolBar(barra)

boton = QAction(QIcon("icons/bug.png"), "Mi boton", self)
boton.setStatusTip("Este es mi boton")      # texto en la barra de estado al pasar el ratón
boton.triggered.connect(self.botonpulsado)
barra.addAction(boton)
barra.addSeparator()                        # línea separadora

barra.addWidget(QLabel("Texto"))            # también admite widgets normales
barra.addWidget(QCheckBox("Selección"))

menu = self.menuBar()
menu_archivo = menu.addMenu("&Archivo")     # & -> atajo Alt+A
menu_archivo.addAction(boton)               # la MISMA acción en el menú
menu_mas = menu_archivo.addMenu("Más")      # submenú

self.setStatusBar(QStatusBar(self))
```

Conceptos:

- **`QAction`**: una "orden" que se puede poner a la vez en la barra de herramientas y en los menús. Se define una vez (icono, texto, ayuda y slot) y se reutiliza.
- `QAction` y `QIcon` se importan de **`PyQt6.QtGui`** (no de `QtWidgets`).
- La señal de `QAction` es **`triggered`** (no `clicked`). Envía un `bool` (`False` si la acción no es *checkable*), por eso imprime `Pulsado False`.
- `setStatusTip` solo se ve si la ventana tiene **barra de estado** (`setStatusBar`).
- El `&` delante de una letra del menú la subraya y crea el atajo **Alt + letra**.
- Menús: `Archivo` (con las dos acciones y el submenú `Más`), `Editar` e `Insertar` (vacíos).
- Los iconos salen de la carpeta `icons/` (iconos *Fugue*, más de 3.500).

### 4.2 `ejercicioToolBar.py` — Acción que modifica la ventana

- Una acción con icono de bicho en la barra y en el menú `Archivo`.
- Cada vez que se pulsa, la etiqueta central cambia a `Texto cambiado 1`, `Texto cambiado 2`…

  ```python
  def botonClick(self):
      self.veces += 1
      self.etiqueta.setText(f"Texto cambiado {self.veces}")
  ```
- La etiqueta y el contador se guardan con `self.` para poder usarlos en el slot.
- Iconos más grandes: `setIconSize(QSize(32, 32))`.

---

## 5. Cuadros de diálogo

Un diálogo es una ventana pequeña para avisar o preguntar algo al usuario. `exec()` lo abre en modo **modal**: bloquea la ventana principal hasta que se cierra.

### 5.1 `Ej30-Dialog.py` — `QDialog` vacío

```python
def botonPulsado(self, s):
    dlg = QDialog(self)                 # self = ventana padre
    dlg.setWindowTitle("Cuadro de diálogo")
    dlg.exec()
```

- Pasar `self` como padre hace que el diálogo salga **centrado sobre** la ventana principal.
- El parámetro `s` recibe el `bool` que envía `clicked`.

### 5.2 `dialogs.py` + `Ej31-DialogButtonBox.py` — Diálogo personalizado con botones

`dialogs.py` define la clase `CustomDialog`:

```python
QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
self.dialogBox = QDialogButtonBox(QBtn)
self.dialogBox.accepted.connect(self.accept)   # OK -> accept
self.dialogBox.rejected.connect(self.reject)   # Cancel -> reject
```

`Ej31` lo usa:

```python
dlg = CustomDialog()
if dlg.exec():                      # 1 si accept, 0 si reject
    print("El usuario ha aceptado")
else:
    print("El usuario ha rechazado")
```

- `QDialogButtonBox` pone los botones estándar en el orden correcto de cada sistema operativo.
- Los botones se combinan con `|`.
- `accept()` y `reject()` cierran el diálogo y hacen que `exec()` devuelva `1` o `0`.
- Separar el diálogo en otro fichero (`dialogs.py`) y luego importarlo es una buena práctica.
- Mejora: crear el diálogo con padre (`CustomDialog(self)` añadiendo `parent=None` al constructor) para que salga centrado sobre la ventana.

### 5.3 `Ej32-MessageBox.py` — `QMessageBox`

```python
dlg = QMessageBox(self)
dlg.setWindowTitle("Cuadro de mensaje")
dlg.setText("Este es el mensaje de mi cuadro de mensaje")
dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
dlg.setIcon(QMessageBox.Icon.Information)

if dlg.exec() == QMessageBox.StandardButton.Yes:
    print("El usuario ha aceptado")
```

- Diálogo ya preparado para mensajes: texto, icono y botones.
- Aquí `exec()` devuelve **el botón pulsado**, por eso se compara con `StandardButton.Yes`.
- Iconos: `NoIcon`, `Question`, `Information`, `Warning`, `Critical`.
- Atajo en una sola línea con los métodos estáticos:

  ```python
  respuesta = QMessageBox.question(self, "Título", "¿Seguro?")
  QMessageBox.information(self, "Título", "Mensaje")
  QMessageBox.warning(self, "Título", "Cuidado")
  QMessageBox.critical(self, "Título", "Error")
  ```

---

## 6. Varias ventanas

En todos se define una segunda clase `OtraVentana(QWidget)` con una etiqueta. Un `QWidget` **sin padre** se muestra como una ventana independiente (y, a diferencia de un diálogo con `exec()`, no bloquea la principal).

### 6.1 `Ej33-Ventana_1.py` — Abrir una segunda ventana

```python
def mostrarVentana(self):
    self.window = OtraVentana()
    self.window.show()
```

- Hay que guardarla en **`self.`**. Si fuera una variable local, Python la borraría al terminar el método y la ventana se cerraría al instante.
- Cada clic crea una ventana **nueva** que sustituye a la anterior.

### 6.2 `Ej34CerrarVentana.py` — Abrir / cerrar con el mismo botón

```python
def mostrarVentana(self):
    if self.window is None:
        self.window = OtraVentana()
        self.window.show()
    else:
        self.window.close()
        self.window = None
```

- `self.window = None` en `__init__` para empezar sin ventana.
- Cada vez que se abre se crea **de cero**: si tuviera datos escritos, se perderían.

### 6.3 `VentanasPersistentes.py` — Mostrar / ocultar sin destruir

```python
# en __init__
self.window = OtraVentana()     # se crea UNA sola vez

def mostrarVentana(self):
    if self.window.isVisible():
        self.window.hide()
    else:
        self.window.show()
```

- La ventana se crea al principio y solo se **oculta/muestra**, así **conserva su estado**.

| | `Ej34CerrarVentana` | `VentanasPersistentes` |
|---|---|---|
| Se crea | Cada vez que se abre | Una vez, al iniciar |
| Al "cerrar" | `close()` + `None` (se destruye) | `hide()` (se oculta) |
| Conserva datos | No | Sí |

### 6.4 `ventanaConectaDatos.py` — Pasar datos de una ventana a otra

```python
self.window = OtraVentana()
self.input = QLineEdit()
self.input.textChanged.connect(self.window.etiqueta.setText)
```

- Lo que se escribe en la ventana principal aparece **en directo** en la etiqueta de la segunda ventana.
- Funciona porque `etiqueta` es un atributo (`self.etiqueta`) de `OtraVentana`, así que se puede acceder desde fuera.
- Combina: layout con botón + caja de texto, ventana persistente y conexión de señales entre ventanas.

#### Lo que se pidió en clase: `QDateEdit` con calendario desplegable

En el fichero hay un comentario sobre `fecha.setCalendarPopup(True)` y `setMinimumDate(QDate(2006,1,1))`. Es un **`QDateEdit`** (campo de fecha):

```python
from PyQt6.QtWidgets import QDateEdit
from PyQt6.QtCore import QDate

fecha = QDateEdit()
fecha.setCalendarPopup(True)               # al pulsar la flecha se despliega un calendario
fecha.setMinimumDate(QDate(2006, 1, 1))    # no deja elegir antes del 1/1/2006
fecha.setDate(QDate.currentDate())         # fecha inicial: hoy
fecha.setDisplayFormat("dd/MM/yyyy")       # formato que se ve
fecha.dateChanged.connect(lambda d: print(d.toString("dd/MM/yyyy")))
```

- `QDateEdit` está en `QtWidgets`; `QDate` está en `QtCore`.
- Se añade al layout como cualquier otro widget (`plantilla.addWidget(fecha)`).
- `setMaximumDate(...)` pone el límite superior; `fecha.date()` devuelve la fecha elegida.

---

## 7. Tabla resumen de señales

| Widget | Señal | Envía | Ejercicio |
|---|---|---|---|
| `QPushButton` | `clicked` | `bool` (estado si es *checkable*) | varios |
| `QPushButton` | `pressed` / `released` | nada | `EjerBotones` |
| `QLineEdit` | `textChanged` | `str` | `LineEdit`, `InputYLabelConectados` |
| `QCheckBox` | `stateChanged` | `int` (0, 1, 2) | `CheckBox`, `layoutCompleto` |
| `QRadioButton` | `clicked` | `bool` | `widgetsAgrupados` |
| `QComboBox` | `currentIndexChanged` | `int` | `ComboBox` |
| `QComboBox` / `QListWidget` | `currentTextChanged` | `str` | `ComboBox`, `Lista` |
| `QSpinBox` | `valueChanged` / `textChanged` | `int` / `str` | `SpinBox` |
| `QSlider` / `QDial` | `valueChanged` / `sliderMoved` | `int` | `slider`, `dial` |
| `QCalendarWidget` | `selectionChanged` | nada (usar `selectedDate()`) | `Calendario` |
| `QAction` | `triggered` | `bool` | `toolBar`, `ejercicioToolBar` |
| `QDialogButtonBox` | `accepted` / `rejected` | nada | `dialogs` |
| `QTabWidget` | `currentChanged` | `int` (índice) | (extra para `pestañas`) |

---

## 8. Errores y detalles a vigilar

1. **`setChecked` antes de `setCheckable`** (`EjercicioContador`, `EjercicioCancelarBoton`): no tiene efecto. Primero `setCheckable(True)`, luego `setChecked(True)`.
2. **Dos señales al mismo slot** (`SpinBox`, `slider`, `dial`): cada cambio se imprime dos veces. Normalmente basta con `valueChanged`.
3. **Rutas relativas** de imágenes e iconos (`EtiquetaConFoto`, `toolBar`): dependen de la carpeta desde la que se ejecuta el script (ver apartado 9).
4. **Título `"<Mi aplicacion"`**: en varios ficheros de `widgets/` hay un `<` de más en el título de la ventana.
5. **`self.window`** (ejercicios de ventanas): `QMainWindow` ya tiene un método `window()`, y al hacer `self.window = ...` se tapa. Funciona, pero es mejor otro nombre, como `self.ventana`.
6. **f-string con comillas dobles dentro de comillas dobles** (`layoutCompleto`): necesita Python 3.12+.
7. **Código repetido o sin usar**: `layoutActivo.py` y `layoutConBotones.py` son iguales; `Color` se importa sin usarse en varios ficheros; `layout4` en `widgetsAgrupados`; `muestraIndice` en `Lista`; `setCentralWidget` duplicado en `pestañas`.
8. **No se pueden poner layouts directamente en `QMainWindow`**: siempre hace falta el `QWidget` contenedor + `setCentralWidget`.
9. **`connect(self.metodo)` sin paréntesis**: con paréntesis se ejecutaría al conectar, no al pulsar. Si hay que pasar argumentos, usar `lambda`.

---

## 9. Cómo ejecutar los ejercicios

Requisito: `pip install PyQt6`.

```bash
# Widgets: desde dentro de widgets/ (para que cargue la imagen de Img/)
cd DiseñoPestañas/widgets
python EtiquetaConFoto.py

# Layouts: desde DiseñoPestañas/ (para que encuentre icons/)
cd DiseñoPestañas
python Layouts/toolBar.py
python Layouts/pestañas.py
```

- Los `import` de `cuadrado` y `dialogs` funcionan desde cualquier carpeta, porque Python busca módulos en la carpeta del propio script.
- Los iconos (`icons/bug.png`, `icons/android.png`) y la imagen (`Img/...`) se buscan desde la carpeta **en la que estás** al ejecutar.

---

## 10. Preguntas de repaso

<details>
<summary>1. ¿Por qué no se puede llamar a <code>setLayout()</code> directamente sobre la <code>QMainWindow</code>?</summary>

Porque `QMainWindow` ya tiene su propio layout interno (menú, barras, zona central). Se crea un `QWidget` contenedor, se le pone el layout y se usa `setCentralWidget(contenedor)`.
</details>

<details>
<summary>2. ¿Qué diferencia hay entre <code>clicked</code>, <code>pressed</code> y <code>released</code>?</summary>

`pressed` al hundir el botón, `released` al soltarlo y `clicked` cuando se completa el clic (pulsar y soltar encima del botón).
</details>

<details>
<summary>3. ¿Qué valores envía <code>stateChanged</code> de un <code>QCheckBox</code>?</summary>

Un entero: 0 desmarcado, 1 parcialmente marcado (solo con `setTristate(True)`) y 2 marcado.
</details>

<details>
<summary>4. ¿Para qué sirve <code>self.sender()</code>?</summary>

Para saber, dentro de un slot compartido por varios widgets, cuál de ellos ha emitido la señal (por ejemplo, para leer su `text()`).
</details>

<details>
<summary>5. ¿Qué diferencia hay entre <code>QStackedLayout</code> y <code>QTabWidget</code>?</summary>

Los dos muestran una sola "página" de varias. `QStackedLayout` no trae controles: hay que cambiar de página con código (`setCurrentIndex`, por ejemplo desde botones). `QTabWidget` trae las pestañas ya hechas para que el usuario cambie de página.
</details>

<details>
<summary>6. ¿Por qué se usa <code>lambda</code> en <code>botonRed.pressed.connect(lambda: colores.setCurrentIndex(0))</code>?</summary>

Porque `connect` necesita una función sin ejecutar, y queremos llamar a `setCurrentIndex` con el argumento `0`. La `lambda` crea esa función pequeña que se ejecutará al pulsar.
</details>

<details>
<summary>7. ¿Qué ventaja tiene usar <code>QAction</code> en lugar de botones normales en barras y menús?</summary>

Una sola acción (icono, texto, ayuda y slot) se reutiliza en la barra de herramientas, en los menús y en atajos de teclado, sin repetir código.
</details>

<details>
<summary>8. ¿Qué devuelve <code>exec()</code> en un <code>QDialog</code> y en un <code>QMessageBox</code>?</summary>

En un `QDialog`, 1 si se llamó a `accept()` y 0 si se llamó a `reject()`. En un `QMessageBox`, el botón estándar pulsado (por ejemplo `QMessageBox.StandardButton.Yes`).
</details>

<details>
<summary>9. ¿Por qué la segunda ventana se guarda en <code>self.window</code> y no en una variable local?</summary>

Porque una variable local desaparece al terminar el método y Python destruiría la ventana, que se cerraría al instante.
</details>

<details>
<summary>10. ¿Qué diferencia hay entre cerrar con <code>close()</code> + <code>None</code> y ocultar con <code>hide()</code>?</summary>

Con `close()` + `None` la ventana se destruye y se crea de nuevo al abrirla (pierde lo que tuviera). Con `hide()`/`show()` es siempre la misma ventana y conserva su estado.
</details>
