# EJERCICIO - Margen y separación dentro de un layout
#   setContentsMargins(izq, arriba, der, abajo) -> hueco entre el borde de la ventana y los widgets
#   setSpacing(n)                               -> hueco ENTRE un widget y el siguiente

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Layout vertical con margen y separación ---
        layoutVertical = QVBoxLayout()
        layoutVertical.setContentsMargins(10, 10, 10, 10)
        layoutVertical.setSpacing(20)

        # --- Botones ---
        layoutVertical.addWidget(QPushButton("Botón 1"))
        layoutVertical.addWidget(QPushButton("Botón 2"))
        layoutVertical.addWidget(QPushButton("Botón 3"))

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layoutVertical)
        self.setCentralWidget(contenedor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
