from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QHBoxLayout, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

from cuadrado import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        layout = QVBoxLayout()

        # Le damos margen y espaciado entre botones
        layout.setContentsMargins(10,10,10,10)
        layout.setSpacing(20)

        boton1 = QPushButton("Boton 1")
        boton2 = QPushButton("Boton 2")
        boton3 = QPushButton("Boton 3")

        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        




        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        
app = QApplication([])

window = MainWindow()

window.show()

app.exec()
