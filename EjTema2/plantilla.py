# PLANTILLA: el punto de partida de todos los ejercicios con Qt Designer.
# 1) Diseñas la ventana en Designer y la guardas como plantilla.ui
# 2) La conviertes a Python:  pyuic6 plantilla.ui -o plantilla_ui.py   (ese archivo NO se toca)
# 3) En este archivo importas la clase generada y le das funcionalidad.

from plantilla_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

# Hereda de QMainWindow (la ventana) y de Ui_MainWindow (el diseño del .ui)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # crea todos los widgets del .ui dentro de esta ventana
        self.show()

app = QApplication([])
window = MainWindow()
app.exec()
