# Estilo Fusion + hoja .qss sobre la ventana de distribucion_grid
# Ojo: estilo2.qss no está en la carpeta, sin ese archivo da FileNotFoundError

from distribucion_grid_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])
# Podemos establecer estilos personalizados y colores
app.setStyle("Fusion")

with open("estilo2.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()