# EJERCICIO - QLabel con imagen: una etiqueta puede mostrar una foto en vez de texto
#   QPixmap("ruta")         -> carga la imagen
#   etiqueta.setPixmap(...) -> la pone en la etiqueta
#
# OJO con la ruta: "Img/foto.webp" se busca desde la carpeta DESDE LA QUE EJECUTAS,
# no desde la carpeta del archivo. Por eso se construye a partir de __file__
# (la ruta de este .py), y así funciona lo ejecutes desde donde lo ejecutes.

import os

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_IMAGEN = os.path.join(CARPETA, "Img", "imagen-aleatoria-destacada.webp")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        etiqueta = QLabel()
        imagen = QPixmap(RUTA_IMAGEN)

        # Si no encuentra la imagen, QPixmap no da error: se queda vacío (isNull)
        if imagen.isNull():
            etiqueta.setText("No se ha encontrado la imagen")
        else:
            etiqueta.setPixmap(imagen)

        self.setCentralWidget(etiqueta)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
