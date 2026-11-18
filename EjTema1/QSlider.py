# EJERCICIO - QSlider: barra deslizante
#   QSlider(Qt.Orientation.Horizontal) -> en horizontal (Vertical para de pie)
#   setRange(-10, 10)                  -> mínimo y máximo
#
# Dos señales parecidas:
#   valueChanged -> cambia el valor DE CUALQUIER FORMA (arrastrar, clic, teclado)
#   sliderMoved  -> SOLO cuando se arrastra con el ratón

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        barra = QSlider(Qt.Orientation.Horizontal)
        barra.setRange(-10, 10)

        # --- Señales (cada una a su función para ver cuál salta) ---
        barra.valueChanged.connect(self.valorCambiado)
        barra.sliderMoved.connect(self.barraArrastrada)

        self.setCentralWidget(barra)

    # --- Funciones (slots) ---
    def valorCambiado(self, valor):
        print("Valor cambiado:", valor)

    def barraArrastrada(self, valor):
        print("Arrastrando:", valor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
