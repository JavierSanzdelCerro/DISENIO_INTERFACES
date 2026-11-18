from distribucion_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

# Todo el reparto del espacio está hecho en distribucion.ui (míralo en Designer o en distribucion_ui.py):
#  - layoutStretch "1,3" en hlContenido: el lateral se queda 1 parte y el texto 3 partes del ancho
#  - layoutStretch "0,1,0" en vlPrincipal: solo la fila central crece al agrandar la ventana
#  - sizePolicy Fixed en btnAceptar/btnCancelar: no crecen nunca
#  - sizePolicy Expanding en textContenido: ocupa todo lo que puede
#  - maximumSize 150 de ancho en los botones del lateral: no pasan de ahí
#  - spacer vertical: empuja los botones del lateral hacia arriba
#  - spacer horizontal: empuja Aceptar y Cancelar a la derecha
# Redimensiona la ventana para ver cómo se comporta cada parte.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

app = QApplication([])
window = MainWindow()
app.exec()
