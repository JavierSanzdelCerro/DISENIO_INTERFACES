# EJERCICIO (en clase: Ej30) - QDialog: abrir un cuadro de diálogo vacío al pulsar un botón
# dialogo.exec() abre el diálogo y BLOQUEA la ventana principal hasta que se cierre.

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets + señales ---
        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.botonPulsado)
        self.setCentralWidget(boton)

    # --- Funciones (slots) ---
    def botonPulsado(self):
        dialogo = QDialog(self)   # self = la ventana principal es su "padre" (sale encima de ella)
        dialogo.setWindowTitle("Cuadro de diálogo")
        dialogo.exec()


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
