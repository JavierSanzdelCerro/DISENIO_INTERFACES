# EJERCICIO - Barra de herramientas, menú y barra de estado
#
#   QAction    -> una "acción" (botón con icono y texto). La MISMA acción se puede
#                 poner en la barra de herramientas Y en el menú a la vez.
#   QToolBar   -> barra de herramientas         self.addToolBar(barra)
#   menuBar()  -> barra de menú (ya viene en QMainWindow, no se importa nada)
#   QStatusBar -> barra de abajo; muestra el setStatusTip al pasar el ratón
#
# Los iconos se buscan en la carpeta "icons" (si no existe, sale el texto sin icono).

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon  # OJO: QAction y QIcon vienen de QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widget central ---
        etiqueta = QLabel("Hola")
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(etiqueta)

        # --- Acciones ---
        accionBug = QAction(QIcon("icons/bug.png"), "Mi botón", self)
        accionBug.setStatusTip("Este es mi botón")             # Texto en la barra de estado
        accionBug.triggered.connect(self.botonPulsado)         # triggered = se ha pulsado

        accionAndroid = QAction(QIcon("icons/android.png"), "Mi botón Android", self)
        accionAndroid.setStatusTip("Este es mi botón Android")
        accionAndroid.triggered.connect(self.botonPulsado)

        # --- Barra de herramientas ---
        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(16, 16))
        self.addToolBar(barra)

        barra.addAction(accionBug)
        barra.addSeparator()                       # Rayita separadora
        barra.addAction(accionAndroid)
        barra.addSeparator()
        barra.addWidget(QLabel("Texto"))           # También admite widgets normales
        barra.addWidget(QCheckBox("Selección"))

        # --- Barra de menú ---
        # El & subraya la letra siguiente -> atajo con Alt (Alt+A abre Archivo)
        menu = self.menuBar()
        menuArchivo = menu.addMenu("&Archivo")
        menu.addMenu("&Editar")                    # Menús vacíos, solo de ejemplo
        menu.addMenu("&Insertar")

        menuArchivo.addAction(accionBug)
        menuArchivo.addAction(accionAndroid)

        # Submenú dentro de Archivo
        menuMas = menuArchivo.addMenu("Más")
        menuMas.addAction(accionBug)
        menuMas.addAction(accionAndroid)

        # --- Barra de estado ---
        self.setStatusBar(QStatusBar(self))

    # --- Funciones (slots) ---
    def botonPulsado(self, s):  # s = True/False (si la acción está marcada)
        print("Pulsado", s)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
