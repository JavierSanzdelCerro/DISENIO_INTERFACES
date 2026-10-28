# EJERCICIO - QDial: rueda giratoria (como el volumen de una radio)
# Funciona igual que QSlider, solo cambia la forma.
#   setRange(-10, 10)        -> mínimo y máximo
#   setNotchesVisible(True)  -> dibuja las marquitas alrededor de la rueda
#
#   valueChanged -> cambia el valor DE CUALQUIER FORMA
#   sliderMoved  -> SOLO cuando se gira arrastrando con el ratón

from PyQt6.QtWidgets import QApplication, QMainWindow, QDial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        rueda = QDial()
        rueda.setRange(-10, 10)
        rueda.setNotchesVisible(True)

        # --- Señales ---
        rueda.valueChanged.connect(self.valorCambiado)
        rueda.sliderMoved.connect(self.ruedaGirada)

        self.setCentralWidget(rueda)

    # --- Funciones (slots) ---
    def valorCambiado(self, valor):
        print("Valor cambiado:", valor)

    def ruedaGirada(self, valor):
        print("Girando:", valor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
