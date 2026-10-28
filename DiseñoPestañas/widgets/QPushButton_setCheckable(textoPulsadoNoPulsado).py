# EJERCICIO - Botón "interruptor": se queda hundido o no, y su texto lo dice
#   setCheckable(True) -> el botón tiene 2 estados (como un interruptor de la luz)
#   clicked envía ese estado a la función: True = hundido, False = no hundido
#
# Truco: ["No pulsado", "Pulsado"][pulsado]
#   False vale 0 -> "No pulsado"      True vale 1 -> "Pulsado"

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets (con self para poder cambiar su texto desde la función) ---
        self.boton = QPushButton("Pulsa")
        self.boton.setCheckable(True)

        # --- Señales ---
        self.boton.clicked.connect(self.botonPulsado)

        self.setCentralWidget(self.boton)

    # --- Funciones (slots) ---
    def botonPulsado(self, pulsado):   # pulsado: True / False
        self.boton.setText(["No pulsado", "Pulsado"][pulsado])


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
