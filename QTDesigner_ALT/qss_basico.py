# Estilo Fusion + qss_basico.qss: fuentes, borde punteado con margin/padding, .QWidget y #pushButton_2

from qss_basico_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([]) # Hago un objeto QApplication
app.setStyle("Fusion") # Cambia el estilo de la interfaz en clase hemos visto "Fusion" y "Windows"
with open("qss_basico.qss","r") as f:
    app.setStyleSheet(f.read())

window = MainWindow() # Hago un objeto QMainWindow que es una ventana

app.exec() # Para que se quede la ventana ablierta