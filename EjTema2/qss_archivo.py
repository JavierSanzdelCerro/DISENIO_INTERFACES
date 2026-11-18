from qss_archivo_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])

# Abre la hoja de estilos, lee todo su texto y lo aplica a TODA la aplicación.
# La ruta es relativa: el .qss se busca en la carpeta desde la que ejecutas (abre EjTema2 en VS Code).
# "with" cierra el archivo solo al terminar.
with open("qss_archivo.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
app.exec()
