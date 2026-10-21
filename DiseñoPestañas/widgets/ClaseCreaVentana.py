from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        boton = QPushButton("Pulsa")

        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(boton)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()