from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QGroupBox, QRadioButton 
from PyQt6.QtCore import Qt 
from cuadrado import Color 

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Mi Aplicacion") 
        
        # Creacion de contenedores 
        layout1 = QVBoxLayout() 
        layout2 = QHBoxLayout() 
        layout3 = QVBoxLayout() 
        layout4 = QHBoxLayout() 
        
        grupo1 = QGroupBox("Botones") 
        
        # Creacion de las eqtiquetas de los contenedores 
        boton1 = QPushButton("Boton 1") 
        boton1.clicked.connect(self.botonpulsado) 
        layout1.addWidget(boton1) 
        
        boton2 = QPushButton("Boton 2") 
        boton2.clicked.connect(self.botonpulsado) 
        layout1.addWidget(boton2) 
        
        boton3 = QPushButton("Boton 3") 
        boton3.clicked.connect(self.botonpulsado) 
        layout1.addWidget(boton3) 
        
        grupo1.setLayout(layout1) 
        layout2.addWidget(grupo1) 

        
        
        grupo2 = QGroupBox("Botones") 
        
        # Creacion de las eqtiquetas de los contenedores 
        radio1 = QRadioButton("Radio 1") 
        radio1.clicked.connect(self.botonpulsado) 
        layout3.addWidget(radio1) 
        
        radio2 = QRadioButton("Radio 2") 
        radio2.clicked.connect(self.botonpulsado) 
        layout3.addWidget(radio2) 
        
        radio3 = QRadioButton("Radio 3") 
        radio3.clicked.connect(self.botonpulsado) 
        layout3.addWidget(radio3) 
        
        grupo2.setLayout(layout3) 
        layout2.addWidget(grupo2) 
        
        widget = QWidget() 
        widget.setLayout(layout2) 
        self.setCentralWidget(widget) 

    def botonpulsado(self): 
        boton = self.sender() 
        print(f"{boton.text()} pulsado") 

app = QApplication([]) 
window = MainWindow() 
window.show() 
app.exec()
