from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout 
from PyQt6.QtCore import Qt 
from cuadrado import Color 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Mi Aplicacion") 
        
        plantilla = QGridLayout()

        # Aqui se crean los widgets para la plantilla
        plantilla.addWidget(Color("red"),0,0)
        plantilla.addWidget(Color("green"),0,1)
        plantilla.addWidget(Color("yellow"),1,2)
        plantilla.addWidget(Color("blue"),2,0)

        widget = QWidget()
        widget.setLayout(plantilla)
        self.setCentralWidget(widget)


app = QApplication([]) 
window = MainWindow() 
window.show() 
app.exec()
