import sys
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")

        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.botonPulsado)
        self.setCentralWidget(boton)


    def botonPulsado (self):
       dlg = QMessageBox(self)
       dlg.setWindowTitle("Cuadro de mensaje")
       dlg.setText("Este es el mensaje de mi cuadro de mensaje")
       dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
       dlg.setIcon(QMessageBox.Icon.Information)
        

       if dlg.exec() == QMessageBox.StandardButton.Yes:
           print("El usuario ha aceptado")
       else:
           print("El usuario ha rechazado")   
        

app = QApplication([])

window = MainWindow()

window.show()

app.exec()