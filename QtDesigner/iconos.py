from PyQt6.QtWidgets import QApplication, QPushButton, QStyle
from PyQt6.QtCore import QSize


app = QApplication([])

boton = QPushButton()

estilo = boton.style()
icono = estilo.standardIcon(QStyle.StandardPixmap.SP_ArrowRight)
boton.setIcon(icono)
boton.setIconSize(QSize(40,40))
boton.show()

app.exec()