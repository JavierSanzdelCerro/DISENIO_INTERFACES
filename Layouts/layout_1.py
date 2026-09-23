from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt

from cuadrado import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        plantilla = QHBoxLayout()

        plantilla.addWidget(Color("red"))
        plantilla.addWidget(Color("green"))
        plantilla.addWidget(Color("orange"))
        plantilla.addWidget(Color("grey"))
        plantilla.addWidget(Color("blue"))
        plantilla.addWidget(Color("purple"))

        widget = QWidget()
        widget.setLayout(plantilla)
        self.setCentralWidget(widget)

        
app = QApplication([])

window = MainWindow()

window.show()

app.exec()
