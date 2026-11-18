from menus_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

# Los menús y las acciones se crean en Designer escribiendo en "Escriba aquí".
# Designer pone el nombre solo: "Salir" -> actionSalir, "Acerca de" -> actionAcerca_de
# (los espacios pasan a "_"). Los atajos (Ctrl+N, Ctrl+Q) también están en el .ui.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Las acciones (QAction) usan la señal triggered, no clicked
        self.actionNuevo.triggered.connect(self.nuevo)
        self.actionSalir.triggered.connect(self.salir)
        self.actionAcerca_de.triggered.connect(self.acerca_de)

        # El mismo método sirve para el botón: menú y botón hacen lo mismo
        self.btnSalir.clicked.connect(self.salir)

    def nuevo(self):
        self.textDocumento.clear()
        self.statusbar.showMessage("Documento nuevo", 3000)

    def salir(self):
        # question devuelve el botón que se ha pulsado
        respuesta = QMessageBox.question(self, "Salir", "¿Seguro que quieres salir?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if respuesta == QMessageBox.StandardButton.Yes:
            self.close()

    def acerca_de(self):
        QMessageBox.about(self, "Acerca de", "Ejemplo de menús hecho con Qt Designer")

app = QApplication([])
window = MainWindow()
app.exec()
