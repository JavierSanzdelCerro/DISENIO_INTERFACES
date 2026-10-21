from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("<Mi aplicacion")

        self.casilla = QCheckBox("Casilla de verificacion")
        formato = self.casilla.font()
        formato.setBold(True)
        self.casilla.setFont(formato)

        self.casilla.stateChanged.connect(self.muestraEstado)


        self.setCentralWidget(self.casilla)

    def muestraEstado(self, pulsado):
        self.casilla.setText(["No pulsado", "", "Pulsado"][pulsado])
        print(["No pulsado", "", "Pulsado"][pulsado])

app = QApplication([])

window = MainWindow()

window.show()

app.exec()