# EJERCICIO - Las 3 señales de un QPushButton y en qué orden llegan
#   pressed  -> al HUNDIR el botón (ratón abajo)
#   released -> al SOLTAR el botón (ratón arriba)
#   clicked  -> pulsar + soltar encima del botón (un clic completo)
#
# Orden en la consola al hacer un clic:  pulsado -> soltado -> pulsado y soltado

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        boton = QPushButton("Pulsa")

        # --- Señales (una función para cada una) ---
        boton.clicked.connect(self.botonPulsadoYSoltado)
        boton.pressed.connect(self.botonPulsado)
        boton.released.connect(self.botonSoltado)

        self.setCentralWidget(boton)

    # --- Funciones (slots) ---
    def botonPulsadoYSoltado(self):
        print("Botón pulsado y soltado")

    def botonPulsado(self):
        print("Botón pulsado")

    def botonSoltado(self):
        print("Botón soltado")


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
