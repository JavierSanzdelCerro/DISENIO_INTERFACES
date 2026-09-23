from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("<Mi aplicacion")

        spinBox = QSpinBox()
        spinBox.setRange(-10,10)
        spinBox.setSingleStep(2)
        spinBox.setSuffix(" €")

        spinBox.textChanged.connect(self.valorCambiado)
        spinBox.valueChanged.connect(self.valorCambiado)

        self.setCentralWidget(spinBox)

    def valorCambiado(self, valor):
        print(valor)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()