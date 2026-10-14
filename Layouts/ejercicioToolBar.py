from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox, QMenuBar
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from cuadrado import Color 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Mi Aplicacion") 
        
        self.etiqueta = QLabel("Hola")
        
        self.veces = 0

        self.setCentralWidget(self.etiqueta)

        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(32,32))
        self.addToolBar(barra)

        boton = QAction(QIcon("icons/bug.png"),"Mi boton", self)
        boton.setStatusTip("Este es mi boton")
        boton.triggered.connect(self.botonClick)
        barra.addAction(boton)
        
        barra.addSeparator()

        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Archivo")
        
        menu_archivo.addAction(boton)

        self.setStatusBar(QStatusBar(self))
    
    def botonClick(self):
        self.veces += 1
        self.etiqueta.setText(f"Texto cambiado {self.veces}")
        
app = QApplication([]) 
window = MainWindow() 
window.show() 
app.exec()
