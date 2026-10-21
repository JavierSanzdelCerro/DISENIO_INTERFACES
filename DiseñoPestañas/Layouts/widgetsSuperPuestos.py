from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from PyQt6.QtCore import Qt 
from cuadrado import Color 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Mi Aplicacion") 
        
        plantilla = QStackedLayout()

        plantilla.addWidget(Color("red"))
        plantilla.addWidget(Color("blue"))
        plantilla.addWidget(Color("purple"))
        plantilla.addWidget(Color("green"))
        plantilla.addWidget(Color("pink"))

        plantilla.setCurrentIndex(2)

        widget = QWidget()
        widget.setLayout(plantilla)
        self.setCentralWidget(widget)


app = QApplication([]) 
window = MainWindow() 
window.show() 
app.exec()
