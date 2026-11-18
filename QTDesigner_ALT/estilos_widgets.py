# Estilo Fusion + .qss por tipo de widget (QPushButton, QLineEdit, QSpinBox) y por objectName (#label_4)

from estilos_widgets_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([]) # Hago un objeto QApplication
app.setStyle("Fusion") # Cambia el estilo de la interfaz en clase hemos visto "Fusion" y "Windows"

with open("estilos_widgets.qss","r") as f:
    app.setStyleSheet(f.read())

window = MainWindow() # Hago un objeto QMainWindow que es una ventana
app.exec() # Para que se quede la ventana ablierta