# EJERCICIO - QMainWindow: la ventana básica con un botón y un tamaño fijo
# Es la plantilla que se repite en TODOS los ejercicios:
#   1. Una clase que hereda de QMainWindow
#   2. Crear los widgets en __init__
#   3. Poner un widget en el centro           -> self.setCentralWidget(widget)
#
# setFixedSize(QSize(ancho, alto)) -> la ventana NO se puede redimensionar

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        boton = QPushButton("Pulsa")

        # --- Tamaño fijo de la ventana (400 de ancho x 300 de alto) ---
        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(boton)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
