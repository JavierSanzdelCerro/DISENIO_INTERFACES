from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox, QMenuBar
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from cuadrado import Color 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Mi Aplicacion") 
        
        etiqueta = QLabel("Hola")
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(etiqueta)

        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(16,16))
        self.addToolBar(barra)

        boton = QAction(QIcon("icons/bug.png"),"Mi boton", self)
        boton.setStatusTip("Este es mi boton")
        boton.triggered.connect(self.botonpulsado)
        barra.addAction(boton)
        
        barra.addSeparator()
        
        botonAndroid = QAction(QIcon("icons/android.png"),"Mi botonAndroid", self)
        botonAndroid.setStatusTip("Este es mi botonAndroid")
        botonAndroid.triggered.connect(self.botonpulsado)
        barra.addAction(botonAndroid)
        
        barra.addSeparator()
        
        barra.addWidget(QLabel("Texto"))
        barra.addWidget(QCheckBox("Selección"))

        barra.addSeparator()

        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Archivo")
        menu_editar = menu.addMenu("&Editar")
        menu_insertar = menu.addMenu("&Insertar")
        
        menu_archivo.addAction(boton)
        menu_archivo.addAction(botonAndroid)

        barra.addSeparator()

        menu_mas = menu_archivo.addMenu("Más")
        menu_mas.addAction(boton)
        menu_mas.addAction(botonAndroid)

        self.setStatusBar(QStatusBar(self))

    def botonpulsado(self,s):
        print("Pulsado",s)

        
app = QApplication([]) 
window = MainWindow() 
window.show() 
app.exec()
