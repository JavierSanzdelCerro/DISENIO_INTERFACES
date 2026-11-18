from paleta_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])
app.setStyle("Fusion")  # SIN Fusion la paleta NO funciona (el estilo de Windows la ignora)

paleta = QPalette()
# Cada ColorRole es una "zona" de los widgets. QColor admite 3 formas:
paleta.setColor(QPalette.ColorRole.Window, QColor("lightyellow"))    # nombre -> fondo de la ventana
paleta.setColor(QPalette.ColorRole.WindowText, QColor("#7a4b00"))    # hexadecimal -> texto de la ventana (QLabel)
paleta.setColor(QPalette.ColorRole.Base, QColor(255, 250, 230))      # RGB -> fondo de campos y listas
paleta.setColor(QPalette.ColorRole.Text, QColor("darkblue"))         # texto dentro de campos y listas
paleta.setColor(QPalette.ColorRole.Button, QColor("#ffcc66"))        # fondo de los botones
paleta.setColor(QPalette.ColorRole.ButtonText, QColor(90, 40, 0))    # texto de los botones
paleta.setColor(QPalette.ColorRole.Highlight, QColor("darkorange"))  # elemento seleccionado
app.setPalette(paleta)  # se aplica a TODA la aplicación

window = MainWindow()
app.exec()
