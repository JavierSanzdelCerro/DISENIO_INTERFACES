# EJERCICIO - Ejercicio de barra de herramientas: el botón cuenta los clics
# Al pulsar la acción (en la barra o en el menú Archivo) la etiqueta cambia:
# "Texto cambiado 1", "Texto cambiado 2"...

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Datos ---
        self.veces = 0   # Contador de clics (con self para usarlo en botonClick)

        # --- Widget central ---
        self.etiqueta = QLabel("Hola")   # Con self porque se cambia luego en botonClick
        self.setCentralWidget(self.etiqueta)

        # --- Acción ---
        accionBug = QAction(QIcon("icons/bug.png"), "Mi botón", self)
        accionBug.setStatusTip("Este es mi botón")
        accionBug.triggered.connect(self.botonClick)

        # --- Barra de herramientas ---
        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(32, 32))
        self.addToolBar(barra)
        barra.addAction(accionBug)

        # --- Barra de menú ---
        menuArchivo = self.menuBar().addMenu("&Archivo")
        menuArchivo.addAction(accionBug)

        # --- Barra de estado ---
        self.setStatusBar(QStatusBar(self))

    # --- Funciones (slots) ---
    def botonClick(self):
        self.veces += 1
        self.etiqueta.setText(f"Texto cambiado {self.veces}")


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
