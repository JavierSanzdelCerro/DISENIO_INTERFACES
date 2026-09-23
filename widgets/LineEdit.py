from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QLineEdit
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("<Mi aplicacion")

        self.texto = QLineEdit()
        self.texto.setMaxLength(10)
        self.texto.setPlaceholderText("Introduce tu nombre...")

        self.texto.textChanged.connect(self.textoCambiado)

        self.setCentralWidget(self.texto)

    def textoCambiado(self, nombre):
        print(nombre)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()