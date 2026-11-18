from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(QLabel("Hola"))

        accionGuardar = QAction(QIcon("icons/bug.png"), "Guardar", self)
        accionGuardar.setStatusTip("Guarda el archivo")
        accionGuardar.triggered.connect(self.guardar)

        accionNuevo = QAction(QIcon("icons/bug.png"), "Nuevo", self)
        accionNuevo.setStatusTip("Crea un archivo nuevo")
        accionNuevo.triggered.connect(self.nuevo)

        menu = self.menuBar()
        menuArchivo = menu.addMenu("&Archivo")
        menuArchivo.addAction(accionGuardar)
        menuArchivo.addAction(accionNuevo)

        barra = QToolBar("Mi barra")
        barra.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(barra)
        barra.addAction(accionGuardar)
        barra.addAction(accionNuevo)

        self.setStatusBar(QStatusBar(self))

    def guardar(self):
        print("Guardado")

    def nuevo(self):
        print("Nuevo archivo")

app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()