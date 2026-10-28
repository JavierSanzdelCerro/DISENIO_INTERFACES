# EJERCICIO - Caja de texto conectada a una etiqueta: lo que escribes aparece debajo
# Truco: se conecta textChanged DIRECTAMENTE con setText de la etiqueta
# (no hace falta escribir una función). Es la misma idea que en
# Layouts/OtraVentana_textChanged(pasarTextoASegundaVentana).py
#
# Resultado:   [ caja de texto ]   <- QVBoxLayout (uno debajo de otro)
#              texto copiado

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        # (No se llama "input" porque input() ya es una función de Python)
        cajaTexto = QLineEdit()
        etiqueta = QLabel()

        # --- Señales: texto de la caja -> texto de la etiqueta ---
        cajaTexto.textChanged.connect(etiqueta.setText)

        # --- Layout ---
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(cajaTexto)
        layoutVertical.addWidget(etiqueta)

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layoutVertical)
        self.setCentralWidget(contenedor)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
