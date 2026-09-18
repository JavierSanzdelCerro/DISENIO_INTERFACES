from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("<Mi aplicacion")

        lista = QComboBox()
        lista.addItems(["Uno", "Dos", "Tres"])
        lista.addItem("Cuatro")
        lista.setEditable(True)

        lista.currentIndexChanged.connect(self.muestraIndice)
        lista.currentTextChanged.connect(self.muestraTexto)


        self.setCentralWidget(lista)

    def muestraIndice(self, texto):
        print(texto)

    def muestraTexto(self, texto):
        print(texto)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()