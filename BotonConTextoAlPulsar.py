from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        boton = QPushButton("Pulsa")
        boton.setCheckable(True)
        boton.clicked.connect(self.botonpulsado)
        print("Hola")


        self.setCentralWidget(boton)

    def botonpulsado(self):
        print("Botón pulsado")

app = QApplication([])

window = MainWindow()

window.show()

app.exec()