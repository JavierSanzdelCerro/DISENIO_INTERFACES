# EJERCICIO - QLineEdit: caja de texto de una línea
#   setMaxLength(10)          -> no deja escribir más de 10 caracteres
#   setPlaceholderText("...") -> texto gris de pista que desaparece al escribir
#   textChanged               -> señal que se lanza con CADA letra y envía el texto entero

from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        cajaTexto = QLineEdit()
        cajaTexto.setMaxLength(10)
        cajaTexto.setPlaceholderText("Introduce tu nombre...")

        # --- Señales ---
        cajaTexto.textChanged.connect(self.textoCambiado)

        self.setCentralWidget(cajaTexto)

    # --- Funciones (slots) ---
    def textoCambiado(self, texto):
        print(texto)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
