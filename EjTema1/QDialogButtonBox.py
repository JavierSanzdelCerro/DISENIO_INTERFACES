# EJERCICIO (en clase: Ej31) - Diálogo personalizado con botones Aceptar / Cancelar
# El diálogo está en el archivo auxiliar dialogs.py (clase CustomDialog).

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from dialogs import CustomDialog


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
        dialogo = CustomDialog()
        # exec() espera a que el usuario pulse y devuelve True (Ok) o False (Cancel)
        if dialogo.exec():
            print("El usuario ha aceptado")
        else:
            print("El usuario ha rechazado")


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
