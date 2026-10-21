from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.contador = 0
        self.setWindowTitle("mi aplicacion")

        self.boton = QPushButton("pulsa")
        self.boton.setCheckable(True)
        self.boton.clicked.connect(self.botonPulsado)


        self.setCentralWidget(self.boton)

    def botonPulsado(self, pulsado):
        self.boton.setText(["No pulsado", "Pulsado"][pulsado])

app = QApplication([])

window = MainWindow()

window.show()

app.exec()