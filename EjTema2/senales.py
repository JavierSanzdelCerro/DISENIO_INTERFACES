from senales_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Los widgets del .ui se usan con self.<objectName> (el nombre que pusiste en Designer)
        self.comboCiudad.addItems(["Madrid", "Barcelona", "Sevilla", "Valencia"])

        # señal.connect(método) -> sin paréntesis: se pasa el método, no se ejecuta
        self.editNombre.textChanged.connect(self.nombre_cambiado)  # cada vez que cambia el texto
        self.btnSaludar.clicked.connect(self.saludar)
        self.btnLimpiar.clicked.connect(self.limpiar)

    def nombre_cambiado(self, texto):
        # textChanged envía el texto nuevo como parámetro
        self.statusbar.showMessage("Escribiendo: " + texto)

    def saludar(self):
        nombre = self.editNombre.text()
        ciudad = self.comboCiudad.currentText()
        self.lblSaludo.setText("Hola " + nombre + " de " + ciudad)
        self.statusbar.showMessage("Saludo enviado", 3000)  # 3000 ms y desaparece

    def limpiar(self):
        self.editNombre.setText("")
        self.lblSaludo.setText("Hola...")
        self.statusbar.showMessage("Formulario limpio", 3000)

app = QApplication([])
window = MainWindow()
app.exec()
