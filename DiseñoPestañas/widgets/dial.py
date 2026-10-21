from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QSlider,QDial
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("<Mi aplicacion")

        dial = QDial()
        dial.setRange(-10,10)
        dial.setNotchesVisible(True)

        dial.valueChanged.connect(self.valorCambiado)
        dial.sliderMoved.connect(self.valorCambiado)

        self.setCentralWidget(dial)

    def valorCambiado(self, valor):
        print(valor)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()