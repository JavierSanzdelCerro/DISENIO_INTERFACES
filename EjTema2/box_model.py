from box_model_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

# Todo el ejercicio está en box_model.qss (border, border-radius, padding y margin)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])
with open("box_model.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()
