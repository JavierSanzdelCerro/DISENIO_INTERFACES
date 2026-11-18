# EJERCICIO - QPushButton + señal clicked: al pulsar el botón se escribe un mensaje en la consola
#
# Esquema de las señales (se repite en todos):
#   widget.señal.connect(self.funcion)   -> cuando pase "señal", se ejecuta "funcion"

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        boton = QPushButton("Pulsa")

        # --- Señales ---
        boton.clicked.connect(self.botonPulsado)

        self.setCentralWidget(boton)

    # --- Funciones (slots) ---
    def botonPulsado(self):
        print("Botón pulsado")


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
