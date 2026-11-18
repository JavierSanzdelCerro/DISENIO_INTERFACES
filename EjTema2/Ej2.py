from PyQt6.QtWidgets import QMainWindow, QApplication, QStyle, QLineEdit, QMessageBox, QStyleFactory
from PyQt6.QtGui import QPalette, QColor
from Ej2_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.setWindowTitle("Estudio de texto")

        ## ELEMENTOS ENTRAR SISTEMA
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton.clicked.connect(self.comprobacion)
        self.lineEdit.textChanged.connect(self.asignarLabel)

        ## BOTONES PARA CAMBIAR TEXTO
        self.pushButton_2.clicked.connect(lambda: self.label_3.setStyleSheet("color: red;"))
        self.pushButton_3.clicked.connect(lambda: self.label_3.setStyleSheet("color: green;"))
        self.pushButton_4.clicked.connect(lambda: self.label_3.setStyleSheet("color: blue;"))
        self.pushButton_5.clicked.connect(lambda: self.label_3.setStyleSheet("font-family: Arial;"))
        self.pushButton_6.clicked.connect(lambda: self.label_3.setStyleSheet("font-family: Verdana;"))
        self.pushButton_7.clicked.connect(lambda: self.label_3.setStyleSheet("font-family: Tahoma;"))

        self.spinBox.setRange(10, 30)
        self.spinBox.setSingleStep(2)
        self.spinBox.setSuffix("px")
        self.horizontalSlider.setRange(10, 30)

        self.spinBox.valueChanged.connect(self.horizontalSlider.setValue)
        self.horizontalSlider.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.cambiarTamano)

        self.pushButton_8.clicked.connect(self.borrarNotas)
        self.pushButton_9.clicked.connect(self.textEdit.hide)
        self.pushButton_10.clicked.connect(self.textEdit.show)
        self.pushButton_11.clicked.connect(self.contarCaracteres)

        self.pushButton.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight))
        self.pushButton_8.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TrashIcon))
        self.pushButton_12.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton))
        self.pushButton_13.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogCancelButton))
        self.pushButton_12.clicked.connect(self.mensajeGuardado)
        self.pushButton_13.clicked.connect(self.mensajeSalir)
        self.actionSalir.triggered.connect(self.mensajeSalir)

        self.comboBox.addItems(["claro", "oscuro", "verde"])
        self.comboBox.currentTextChanged.connect(self.cambiarTema)

        ## DESPLEGABLE PARA CAMBIAR EL ESTILO DE LA APP
        self.cmbEstilo.addItems(QStyleFactory.keys())        # estilos que hay en este ordenador (Fusion, Windows...)
        self.cmbEstilo.setCurrentText("Fusion")              # que aparezca Fusion, el que ponemos al arrancar
        self.cmbEstilo.currentTextChanged.connect(self.cambiarEstilo)


    ## FUNCIÓN PARA ENTRAR AL SISTEMA
    def comprobacion(self):
        nombre = self.lineEdit.text()
        contrasena = self.lineEdit_2.text()

        if(nombre == "" or contrasena != "1234"):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("ERROR!!!")
            dlg.setText("Error al introducir el nombre o la contraseña")
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
        else:
            self.statusbar.showMessage(f"Bienvenido {nombre}")

    def asignarLabel(self, texto):
        self.label_3.setText(texto)

    def cambiarTamano(self, tamano):
        self.label_3.setStyleSheet(f"font-size: {tamano}px")

    def borrarNotas(self):
        self.textEdit.clear()

    def contarCaracteres(self):
        textoPlano = self.textEdit.toPlainText()
        totalCaracteres = len(textoPlano)
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Información")
        dlg.setText(f"Total de caracteres --> {totalCaracteres}")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.exec()

    def mensajeGuardado(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Información")
        dlg.setText("Guardado con exito")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.exec()

    def mensajeSalir(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Aviso || Apunto de salir del sistema")
        dlg.setText("¿Estás seguro de salir del sistema?")
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if dlg.exec() == QMessageBox.StandardButton.Yes:
            self.close()

    def cambiarEstilo(self, estilo):
        app.setStyle(estilo)

    def cambiarTema(self, tema):
        with open(f"Ej2_{tema}.qss", "r") as f:   # "oscuro" -> Ej2_oscuro.qss
            app.setStyleSheet(f.read())

app = QApplication([])
app.setStyle("Fusion")

with open("Ej2_claro.qss", "r") as f:
    app.setStyleSheet(f.read())

ventana = MainWindow()
app.exec()