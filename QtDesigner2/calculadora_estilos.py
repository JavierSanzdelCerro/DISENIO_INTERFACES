# Intento de importar la calculadora como módulo para darle estilos
# Ojo: al importar calculadora se abre su ventana (su código se ejecuta entero) y al cerrarla falla:
# heredar de QMainWindow y de MainWindow (que ya es un QMainWindow) a la vez da error de MRO

from calculadora import MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow, MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])

with open("calculadora.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()