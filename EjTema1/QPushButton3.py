# EJERCICIO - Ejercicio de botones: contar cuántas veces se pulsa el botón
#   self.contador     -> variable de la ventana (con self) para que NO se borre entre clics
#   isChecked()       -> True si el botón está hundido (solo con setCheckable(True))
#
# OJO: setCheckable(True) va ANTES que setChecked(True).
#      Si un botón no es "checkable", setChecked no hace nada.

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        self.contador = 0   # Número de pulsaciones

        # --- Widgets ---
        self.boton = QPushButton("Pulsa")
        self.boton.setCheckable(True)   # 1º checkable...
        self.boton.setChecked(True)     # 2º ...y entonces sí se puede marcar

        # --- Señales ---
        self.boton.clicked.connect(self.botonPulsado)

        self.setCentralWidget(self.boton)

    # --- Funciones (slots) ---
    def botonPulsado(self):
        self.contador += 1
        self.boton.setText(f"Pulsado {self.contador} veces")
        print(f"Pulsaciones: {self.contador} - Hundido: {self.boton.isChecked()}")


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
