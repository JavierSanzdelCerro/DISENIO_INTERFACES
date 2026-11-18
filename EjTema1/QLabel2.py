# EJERCICIO - QLabel con formato: texto grande, en negrita y centrado
# Cambiar la letra: 1) sacar la fuente, 2) cambiarla, 3) volver a ponerla
#   (es el mismo truco que con la paleta de colores en cuadrado.py)
#
# setAlignment(...) -> dónde se coloca el texto. El | junta horizontal y vertical.

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        etiqueta = QLabel("Hola")

        # --- Formato del texto ---
        fuente = etiqueta.font()      # 1. Sacar la fuente
        fuente.setPointSize(30)       # 2. Cambiar tamaño, tipo de letra y negrita
        fuente.setFamily("Arial")
        fuente.setBold(True)
        etiqueta.setFont(fuente)      # 3. Volver a ponerla

        # --- Centrado (horizontal Y vertical) ---
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(etiqueta)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
