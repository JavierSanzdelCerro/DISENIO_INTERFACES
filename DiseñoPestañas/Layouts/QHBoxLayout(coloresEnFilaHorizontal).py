# EJERCICIO - QHBoxLayout: colores colocados en horizontal (uno al lado de otro)
#
# Esquema para poner VARIOS widgets en una QMainWindow (se repite en todos):
#   1. Crear un layout y añadirle widgets        -> layout.addWidget(...)
#   2. Crear un QWidget "contenedor" vacío y darle el layout -> contenedor.setLayout(layout)
#   3. Poner el contenedor en el centro de la ventana        -> self.setCentralWidget(contenedor)

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from cuadrado import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- 1. Layout horizontal con 6 colores ---
        layoutHorizontal = QHBoxLayout()
        layoutHorizontal.addWidget(Color("red"))
        layoutHorizontal.addWidget(Color("green"))
        layoutHorizontal.addWidget(Color("orange"))
        layoutHorizontal.addWidget(Color("grey"))
        layoutHorizontal.addWidget(Color("blue"))
        layoutHorizontal.addWidget(Color("purple"))

        # --- 2 y 3. Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layoutHorizontal)
        self.setCentralWidget(contenedor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
