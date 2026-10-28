# EJERCICIO - Layouts anidados: meter layouts dentro de otro layout
#   addWidget(...) -> mete un WIDGET     addLayout(...) -> mete un LAYOUT
#
# Resultado:   [ rojo   | gris   |          ]
#              [ verde  | azul   | amarillo ]
#              [ naranja| morado |          ]

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from cuadrado import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Layouts ---
        layoutPrincipal = QHBoxLayout()    # Padre (horizontal): contiene todo
        columnaIzquierda = QVBoxLayout()   # Hijo 1 (vertical)
        columnaCentro = QVBoxLayout()      # Hijo 2 (vertical)

        # --- Colores de cada columna ---
        columnaIzquierda.addWidget(Color("red"))
        columnaIzquierda.addWidget(Color("green"))
        columnaIzquierda.addWidget(Color("orange"))

        columnaCentro.addWidget(Color("grey"))
        columnaCentro.addWidget(Color("blue"))
        columnaCentro.addWidget(Color("purple"))

        # --- Meter las columnas (layouts) y un color suelto (widget) en el padre ---
        layoutPrincipal.addLayout(columnaIzquierda)
        layoutPrincipal.addLayout(columnaCentro)
        layoutPrincipal.addWidget(Color("yellow"))

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layoutPrincipal)
        self.setCentralWidget(contenedor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
