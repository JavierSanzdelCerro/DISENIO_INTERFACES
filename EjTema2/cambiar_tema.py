from cambiar_tema_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # currentTextChanged envía el texto elegido en el combo
        self.comboTema.currentTextChanged.connect(self.cambiar_tema)
        self.cambiar_tema(self.comboTema.currentText())  # aplica el primer tema al arrancar

    def cambiar_tema(self, tema):
        # Los textos del combo son los nombres de los archivos ("tema_oscuro" -> "tema_oscuro.qss"),
        # así no hace falta ningún if para saber qué hoja cargar
        with open(tema + ".qss", "r") as f:
            app.setStyleSheet(f.read())  # la hoja nueva sustituye a la anterior al momento
        self.statusbar.showMessage("Tema aplicado: " + tema)

app = QApplication([])
window = MainWindow()
app.exec()
