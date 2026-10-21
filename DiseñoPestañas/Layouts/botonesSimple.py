from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QCheckBox
from PyQt6.QtCore import Qt

from cuadrado import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        # Creacion de contenedores
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        # Creacion de las eqtiquetas de los contenedores
        boton1 = QPushButton("Boton1")              
        boton2 = QPushButton("Boton2")      
        boton3 = QPushButton("Boton3")  

        # Añadimos los contenedores hijos al padre
        layout1.addLayout(layout2)
        layout1.addLayout(layout3)

        # Añadimos al contenedor hijo los widget
        layout2.addWidget(boton1)
        layout2.addWidget(boton2)

        # Añadimos al contenedor hijo los widget
        layout3.addWidget(boton3)   


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
