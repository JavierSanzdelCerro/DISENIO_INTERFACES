import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")

        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.botonPulsado)
        self.setCentralWidget(boton)


    def botonPulsado (self,s):
        dlg = QDialog(self)
        dlg.setWindowTitle("Cuadro de diálogo")
        dlg.exec()  
        

app = QApplication([])

window = MainWindow()

window.show()

app.exec()