from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget
from PyQt6.QtCore import Qt 
from cuadrado import Color 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Mi Aplicacion") 
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        tabs.addTab(Color("red"),"rojo")
        tabs.addTab(Color("green"),"verde")
        tabs.addTab(Color("blue"),"azul")
        tabs.addTab(Color("yellow"),"yellow")

        self.setCentralWidget(tabs)

        
        self.setCentralWidget(tabs)

    


app = QApplication([]) 
window = MainWindow() 
window.show() 
app.exec()
