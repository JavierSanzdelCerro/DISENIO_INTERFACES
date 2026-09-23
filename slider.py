from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QSlider
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("<Mi aplicacion")

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(-10,10)

        slider.valueChanged.connect(self.valorCambiado)
        slider.sliderMoved.connect(self.valorCambiado)

        self.setCentralWidget(slider)

    def valorCambiado(self, valor):
        print(valor)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()