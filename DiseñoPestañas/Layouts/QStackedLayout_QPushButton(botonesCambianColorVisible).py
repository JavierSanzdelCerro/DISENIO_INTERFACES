# EJERCICIO - QStackedLayout + botones: cada botón cambia el color que se ve
#
#   [ red ][ green ][ yellow ]   <- fila de botones (QHBoxLayout)
#   [                        ]
#   [    color elegido       ]   <- colores apilados (QStackedLayout)
#
# lambda: crea una función "en el momento". Se usa porque connect necesita
# una función, y aquí queremos llamar a setCurrentIndex CON un número.

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton
from cuadrado import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Layouts ---
        layoutPrincipal = QVBoxLayout()   # Padre: botones arriba, colores abajo
        filaBotones = QHBoxLayout()
        pilaColores = QStackedLayout()

        # --- Colores apilados ---
        pilaColores.addWidget(Color("red"))      # índice 0
        pilaColores.addWidget(Color("green"))    # índice 1
        pilaColores.addWidget(Color("yellow"))   # índice 2

        # --- Botones + señales ---
        botonRojo = QPushButton("red")
        botonRojo.pressed.connect(lambda: pilaColores.setCurrentIndex(0))

        botonVerde = QPushButton("green")
        botonVerde.pressed.connect(lambda: pilaColores.setCurrentIndex(1))

        botonAmarillo = QPushButton("yellow")
        botonAmarillo.pressed.connect(lambda: pilaColores.setCurrentIndex(2))

        filaBotones.addWidget(botonRojo)
        filaBotones.addWidget(botonVerde)
        filaBotones.addWidget(botonAmarillo)

        # --- Meter los dos layouts en el padre ---
        layoutPrincipal.addLayout(filaBotones)
        layoutPrincipal.addLayout(pilaColores)

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layoutPrincipal)
        self.setCentralWidget(contenedor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
