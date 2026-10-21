from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        boton = QPushButton("Pulsa")
        boton.clicked.connect(self.botonpulsadoysoltado)
        boton.pressed.connect(self.botonpulsado)
        boton.released.connect(self.botonsoltado)
        
        print("Hola")


        self.setCentralWidget(boton)

    def botonpulsadoysoltado(self):
        print("Botón pulsado y Soltado")

    def botonpulsado(self):
            print("Botón pulsado")

    def botonsoltado(self):
            print("Botón Soltado")

    

app = QApplication([])

window = MainWindow()

window.show()

app.exec()