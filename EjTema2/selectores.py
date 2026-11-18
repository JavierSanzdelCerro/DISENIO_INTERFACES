from selectores_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

# Todo el ejercicio está en selectores.qss (clase, .clase exacta, #nombre y varios a la vez)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])
with open("selectores.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()
