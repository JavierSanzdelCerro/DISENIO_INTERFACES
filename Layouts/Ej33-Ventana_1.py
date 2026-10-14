import sys
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QMainWindow, QPushButton, QWidget

# Nueva ventana
class OtraVentana(QWidget):
    def __init__(self):
        super().__init__()

        plantilla = QVBoxLayout()
        self.etiqueta = QLabel("Otra ventana")
        plantilla.addWidget(self.etiqueta)
        self.setLayout(plantilla)
    
# Ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")

        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.mostrarVentana)
        self.setCentralWidget(boton)


    def mostrarVentana (self):
        self.window = OtraVentana()
        self.window.show()
      

        
app = QApplication([])

window = MainWindow()

window.show()

app.exec()