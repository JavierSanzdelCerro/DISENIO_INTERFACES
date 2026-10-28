# EJERCICIO - QTabWidget: pestañas (cada pestaña muestra un widget)
# Es parecido al QStackedLayout, pero el propio QTabWidget ya trae las pestañas
# para cambiar, así que NO hace falta layout ni contenedor: va directo al centro.

from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from cuadrado import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widget de pestañas ---
        pestanas = QTabWidget()
        pestanas.setTabPosition(QTabWidget.TabPosition.North)  # Pestañas arriba (North/South/East/West)
        pestanas.setMovable(True)                               # Se pueden arrastrar para reordenar

        # addTab(widget, "texto de la pestaña")
        pestanas.addTab(Color("red"), "rojo")
        pestanas.addTab(Color("green"), "verde")
        pestanas.addTab(Color("blue"), "azul")
        pestanas.addTab(Color("yellow"), "amarillo")

        self.setCentralWidget(pestanas)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
