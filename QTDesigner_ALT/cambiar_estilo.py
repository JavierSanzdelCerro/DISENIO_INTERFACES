# Cambia la hoja .qss de toda la app al elegir una opción del QComboBox (rojo, azul o verde)

from cambiar_estilo_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.comboBox.currentIndexChanged.connect(self.cambiar)

    def cambiar(self, e):
        with open(f"cambiar_estilo_{["rojo","azul","verde"][e]}.qss","r") as f:
           app.setStyleSheet(f.read())

app = QApplication([]) # Hago un objeto QApplication
#app.setStyle("Fusion") # Cambia el estilo de la interfaz en clase hemos visto "Fusion" y "Windows"

with open("cambiar_estilo_rojo.qss","r") as f:
    app.setStyleSheet(f.read())

#paleta = QPalette()
#paleta.setColor(QPalette.ColorRole.Window, QColor("#777777"))
#app.setPalette(paleta)


window = MainWindow() # Hago un objeto QMainWindow que es una ventana
app.exec() # Para que se quede la ventana ablierta