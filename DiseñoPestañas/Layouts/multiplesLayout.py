from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QHBoxLayout, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from cuadrado import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        plantilla1 = QHBoxLayout()
        plantilla2 = QVBoxLayout()
        plantilla3 = QVBoxLayout()

        plantilla2.addWidget(Color("red"))
        plantilla2.addWidget(Color("green"))
        plantilla2.addWidget(Color("orange"))

        plantilla3.addWidget(Color("grey"))
        plantilla3.addWidget(Color("blue"))
        plantilla3.addWidget(Color("purple"))

        plantilla1.addLayout(plantilla2)
        plantilla1.addLayout(plantilla3)
        plantilla1.addWidget(Color("yellow"))




        widget = QWidget()
        widget.setLayout(plantilla1)
        self.setCentralWidget(widget)

        
app = QApplication([])

window = MainWindow()

window.show()

app.exec()
