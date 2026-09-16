from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.contador = 0
        self.setWindowTitle("mi aplicacion")

        self.boton = QPushButton("pulsa")
        self.boton.setChecked(True)
        self.boton.setCheckable(True)
        self.boton.clicked.connect(self.botonPulsado)


        self.setCentralWidget(self.boton)

    def botonPulsado(self):
        self.contador +=1
        # Este es el cambio
        self.boton.setEnabled(False)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()