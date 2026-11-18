from fusion_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Muestra el estilo en uso y los que hay instalados
        self.statusbar.showMessage("Estilo: " + self.style().name() + "   |   Disponibles: " + ", ".join(QStyleFactory.keys()))

app = QApplication([])

# Fusion: estilo propio de Qt, se ve IGUAL en Windows, Linux y Mac.
# Comenta esta línea y vuelve a ejecutar: verás el estilo por defecto del sistema
# (en Windows "windows11"/"windowsvista"), que imita al sistema y cambia según el SO.
# Además, Fusion es el que respeta la paleta de colores (QPalette).
app.setStyle("Fusion")

window = MainWindow()
app.exec()
