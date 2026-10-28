from primer import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
        
app = QApplication([])
app.setStyle("Fusion") # SI NO PONES ESTA LINEA LA PALETA NO VA A FUNCIONAR

paleta = QPalette()
paleta.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.red)
app.setPalette(paleta)

ventana = MainWindow()
app.exec()
        