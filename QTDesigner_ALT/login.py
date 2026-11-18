# Login con QPalette gris claro y la hoja leds.qss (botones grises y redondeados)
# login.qss tiene un estilo propio para este login, pero no se carga

from login_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([]) # Hago un objeto QApplication
# app.setStyle("Fusion") # Cambia el estilo de la interfaz en clase hemos visto "Fusion" y "Windows"

with open("leds.qss","r") as f:
    app.setStyleSheet(f.read())

paleta = QPalette()
paleta.setColor(QPalette.ColorRole.Window, QColor("#d4d4d4"))

app.setPalette(paleta)

window = MainWindow() # Hago un objeto QMainWindow que es una ventana
app.exec() # Para que se quede la ventana ablierta