from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QCheckBox
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

        # Creacion de las eqtiquetas de los contenedores
        etiqueta = QLabel("Texto")
        lineEdit = QLineEdit()
        checkbox1 = QCheckBox("Opcion 1")
        checkbox2 = QCheckBox("Opcion 2")
        checkbox3 = QCheckBox("Opcion 3")

        # Añadimos los contenedores hijos al padre
        layout1.addLayout(layout2)
        layout1.addLayout(layout3)

        # Añadimos al contenedor hijo los widget
        layout2.addWidget(etiqueta)
        layout2.addWidget(lineEdit)

        # Añadimos al contenedor hijo los widget
        layout3.addWidget(checkbox1)       
        layout3.addWidget(checkbox2)
        layout3.addWidget(checkbox3)   

        checkbox1.stateChanged.connect(self.checksel)    
        checkbox2.stateChanged.connect(self.checksel)    
        checkbox3.stateChanged.connect(self.checksel)    

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


    def checksel(self, s):
        print(f"{self.sender().text()} - {["Desmarcado", "", "Marcado"][s]}")
        

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
