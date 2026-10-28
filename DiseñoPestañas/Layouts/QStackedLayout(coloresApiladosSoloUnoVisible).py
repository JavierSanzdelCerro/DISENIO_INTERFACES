# EJERCICIO - QStackedLayout: widgets apilados (uno encima de otro, como cartas)
# Solo se ve UNO a la vez. setCurrentIndex(n) elige cuál se ve (empieza en 0).

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from cuadrado import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Layout apilado ---
        pila = QStackedLayout()
        pila.addWidget(Color("red"))      # índice 0
        pila.addWidget(Color("blue"))     # índice 1
        pila.addWidget(Color("purple"))   # índice 2
        pila.addWidget(Color("green"))    # índice 3
        pila.addWidget(Color("pink"))     # índice 4

        pila.setCurrentIndex(2)           # Se ve el morado

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(pila)
        self.setCentralWidget(contenedor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
