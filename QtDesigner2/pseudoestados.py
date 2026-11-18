# Pseudoestados (:hover, :pressed, :checked, :on) y subcontroles (::handle, ::down-arrow)
# con iconos de img/icons, sobre una ventana con pestañas, slider, combo y dial

from pseudoestados_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])

with open("pseudoestados.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()