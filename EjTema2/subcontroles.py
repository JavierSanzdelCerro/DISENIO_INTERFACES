from subcontroles_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

# Los estilos de cada sub-control están en subcontroles.qss
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Al mover el slider se mueve el "chunk" de la barra de progreso
        self.sliVolumen.valueChanged.connect(self.barProgreso.setValue)

app = QApplication([])
with open("subcontroles.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()
