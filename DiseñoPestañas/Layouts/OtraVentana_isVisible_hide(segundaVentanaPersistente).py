# EJERCICIO - Ventana persistente: se crea UNA sola vez y el botón la muestra / oculta
# Diferencia con OtraVentana_close(abrirYCerrarSegundaVentana): aquí la ventana NO se destruye, solo se esconde (hide),
# así que conserva lo que tenga dentro.
#   isVisible() -> True si se está viendo     hide() -> ocultar     show() -> mostrar

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton


# ===== Segunda ventana =====
class OtraVentana(QWidget):
    def __init__(self):
        super().__init__()

        layoutVertical = QVBoxLayout()
        self.etiqueta = QLabel("Otra ventana")
        layoutVertical.addWidget(self.etiqueta)
        self.setLayout(layoutVertical)


# ===== Ventana principal =====
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Segunda ventana: se crea aquí, UNA vez (todavía oculta) ---
        self.otraVentana = OtraVentana()

        # --- Widgets + señales ---
        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.mostrarVentana)
        self.setCentralWidget(boton)

    # --- Funciones (slots) ---
    def mostrarVentana(self):
        if self.otraVentana.isVisible():
            self.otraVentana.hide()
        else:
            self.otraVentana.show()


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
