# EJERCICIO - QGridLayout: colocar widgets en una cuadrícula (filas y columnas)
#   addWidget(widget, fila, columna)  -> fila y columna empiezan en 0
#
# Resultado:   fila 0: [ rojo  | verde |          ]
#              fila 1: [       |       | amarillo ]
#              fila 2: [ azul  |       |          ]

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from cuadrado import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Layout en cuadrícula ---
        cuadricula = QGridLayout()
        cuadricula.addWidget(Color("red"), 0, 0)
        cuadricula.addWidget(Color("green"), 0, 1)
        cuadricula.addWidget(Color("yellow"), 1, 2)
        cuadricula.addWidget(Color("blue"), 2, 0)

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(cuadricula)
        self.setCentralWidget(contenedor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
