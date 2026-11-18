from pseudoselectores_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

# Todo el ejercicio está en pseudoselectores.qss.
# Pasa el ratón por los botones, púlsalos, marca el interruptor y haz clic en los campos.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])
with open("pseudoselectores.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()
