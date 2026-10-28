# EJERCICIO - Ejercicio de botones: el botón se desactiva al pulsarlo (solo se puede pulsar 1 vez)
#   setEnabled(False) -> el botón se pone gris y ya no responde a los clics
#   setEnabled(True)  -> lo vuelve a activar

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        self.boton = QPushButton("Pulsa")

        # --- Señales ---
        self.boton.clicked.connect(self.botonPulsado)

        self.setCentralWidget(self.boton)

    # --- Funciones (slots) ---
    def botonPulsado(self):
        self.boton.setText("Ya no puedes pulsar")
        self.boton.setEnabled(False)   # Este es el cambio: desactivar el botón


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
