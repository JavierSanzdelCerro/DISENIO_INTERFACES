from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt 
from cuadrado import Color 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Mi Aplicacion") 
        
        plantilla = QVBoxLayout()
        botones = QHBoxLayout()
        colores = QStackedLayout()

        botonRed = QPushButton("red")
        botonRed.pressed.connect(lambda: colores.setCurrentIndex(0))

        botonGreen = QPushButton("green")
        botonGreen.pressed.connect(lambda: colores.setCurrentIndex(1))

        botonYellow = QPushButton("yellow")
        botonYellow.pressed.connect(lambda: colores.setCurrentIndex(2))

        colores.addWidget(Color("red"))
        colores.addWidget(Color("green"))
        colores.addWidget(Color("yellow"))

        botones.addWidget(botonRed)
        botones.addWidget(botonGreen)
        botones.addWidget(botonYellow)

        plantilla.addLayout(botones)
        plantilla.addLayout(colores)


        widget = QWidget()
        widget.setLayout(plantilla)
        self.setCentralWidget(widget)

    


app = QApplication([]) 
window = MainWindow() 
window.show() 
app.exec()
