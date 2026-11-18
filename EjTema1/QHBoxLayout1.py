# EJERCICIO - Layouts anidados con botones: dos filas de botones
#
# Resultado:   [ Botón 1 ][ Botón 2 ]   <- fila 1 (QHBoxLayout)
#              [      Botón 3       ]   <- fila 2 (QHBoxLayout)
#              Las dos filas van dentro de un QVBoxLayout (una debajo de otra)

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Layouts ---
        layoutPrincipal = QVBoxLayout()   # Padre (vertical)
        fila1 = QHBoxLayout()             # Hijo 1
        fila2 = QHBoxLayout()             # Hijo 2

        # --- Botones en cada fila ---
        fila1.addWidget(QPushButton("Botón 1"))
        fila1.addWidget(QPushButton("Botón 2"))
        fila2.addWidget(QPushButton("Botón 3"))

        # --- Meter las filas en el padre ---
        layoutPrincipal.addLayout(fila1)
        layoutPrincipal.addLayout(fila2)

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layoutPrincipal)
        self.setCentralWidget(contenedor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
