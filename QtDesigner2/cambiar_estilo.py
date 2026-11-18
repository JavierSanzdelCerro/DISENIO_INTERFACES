# Cambia la hoja .qss de toda la app al elegir una opción del QComboBox (rojo, verde o azul)

from cambiar_estilo_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.comboBox.currentIndexChanged.connect(self.cambiar)

    def cambiar(self, x):
        with open(f"{["cambiar_estilo_rojo", "cambiar_estilo_verde", "cambiar_estilo_azul"][x]}.qss", "r") as f:
            app.setStyleSheet(f.read())
        print(x)

app = QApplication([])

with open("pseudoestados.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()