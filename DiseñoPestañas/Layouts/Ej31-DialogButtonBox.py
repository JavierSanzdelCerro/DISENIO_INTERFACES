import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from dialogs import CustomDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")

        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.botonPulsado)
        self.setCentralWidget(boton)


    def botonPulsado (self):
       dlg = CustomDialog() 
       if dlg.exec():
           print("El usuario ha aceptado")
       else:
           print("El usuario ha rechazado")   
        

app = QApplication([])

window = MainWindow()

window.show()

app.exec()