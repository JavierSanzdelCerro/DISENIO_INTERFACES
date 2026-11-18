# EJERCICIO (en clase: Ej33) - Abrir una segunda ventana al pulsar un botón
# La segunda ventana es una clase propia que hereda de QWidget.
# OJO: se guarda en self.otraVentana. Si fuese una variable normal, Python la
# borraría al acabar la función y la ventana se cerraría al instante.

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton


# ===== Segunda ventana =====
class OtraVentana(QWidget):
    def __init__(self):
        super().__init__()

        layoutVertical = QVBoxLayout()
        self.etiqueta = QLabel("Otra ventana")
        layoutVertical.addWidget(self.etiqueta)
        self.setLayout(layoutVertical)   # QWidget usa setLayout directamente


# ===== Ventana principal =====
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets + señales ---
        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.mostrarVentana)
        self.setCentralWidget(boton)

    # --- Funciones (slots) ---
    def mostrarVentana(self):
        # Cada clic crea una ventana NUEVA (la anterior se pierde)
        self.otraVentana = OtraVentana()
        self.otraVentana.show()


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
