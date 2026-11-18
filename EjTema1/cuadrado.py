# ARCHIVO AUXILIAR - clase Color (cuadrado de un color)
# No se ejecuta solo: lo usan otros ejercicios con  ->  from cuadrado import Color
# (Por eso este archivo NO se renombra: si cambias el nombre, fallan los imports.)

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):  # color = texto en inglés: "red", "blue", "green"...
        super().__init__()

        # Sin esto el widget no pinta su fondo y no se vería el color
        self.setAutoFillBackground(True)

        # Cambiar el color: 1) sacar la paleta, 2) cambiar el color de fondo, 3) volver a ponerla
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)
