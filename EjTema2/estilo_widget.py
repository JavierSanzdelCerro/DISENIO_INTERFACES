from estilo_widget_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # setStyleSheet sobre UN widget: solo cambia ese widget (lblPreview), no toda la app.
        # lambda hace falta porque connect necesita una función, y setStyleSheet lleva un argumento.
        self.btnRojo.clicked.connect(lambda: self.lblPreview.setStyleSheet("color: red;"))
        self.btnAzul.clicked.connect(lambda: self.lblPreview.setStyleSheet("color: blue;"))
        self.btnFondo.clicked.connect(lambda: self.lblPreview.setStyleSheet("background-color: yellow;"))
        self.btnCourier.clicked.connect(lambda: self.lblPreview.setStyleSheet("font-family: 'Courier New';"))
        self.btnPequeno.clicked.connect(lambda: self.lblPreview.setStyleSheet("font-size: 10px;"))
        self.btnGrande.clicked.connect(lambda: self.lblPreview.setStyleSheet("font-size: 32px;"))

        # OJO: cada setStyleSheet SUSTITUYE al anterior.
        # Pulsa "Rojo" y luego "Grande": el texto se hace grande pero deja de ser rojo.

        # Forma 1 de mantener varias propiedades: escribirlas todas juntas en la misma cadena
        self.btnTodo.clicked.connect(lambda: self.lblPreview.setStyleSheet(
            "color: white; background-color: navy; font-family: 'Courier New'; font-size: 24px;"))

        # Forma 2: añadir a lo que ya tiene (styleSheet() devuelve el estilo actual)
        self.btnNegrita.clicked.connect(lambda: self.lblPreview.setStyleSheet(
            self.lblPreview.styleSheet() + " font-weight: bold;"))

        # Cadena vacía = quitar el estilo y volver al aspecto normal
        self.btnQuitar.clicked.connect(lambda: self.lblPreview.setStyleSheet(""))

app = QApplication([])
window = MainWindow()
app.exec()
