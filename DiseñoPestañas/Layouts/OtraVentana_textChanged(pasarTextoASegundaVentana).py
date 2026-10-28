# EJERCICIO - Pasar datos a otra ventana: lo que escribes en la principal aparece en la otra
# Truco: se conecta la señal textChanged de la caja de texto DIRECTAMENTE con
# setText de la etiqueta de la otra ventana (no hace falta escribir una función).

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


# ===== Segunda ventana =====
class OtraVentana(QWidget):
    def __init__(self):
        super().__init__()

        layoutVertical = QVBoxLayout()
        self.etiqueta = QLabel("Otra ventana")   # Con self para poder usarla desde MainWindow
        layoutVertical.addWidget(self.etiqueta)
        self.setLayout(layoutVertical)


# ===== Ventana principal =====
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Segunda ventana (persistente, como en OtraVentana_isVisible_hide) ---
        self.otraVentana = OtraVentana()

        # --- Widgets ---
        self.boton = QPushButton("Pulsa aquí")
        self.cajaTexto = QLineEdit()

        # --- Layout ---
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(self.boton)
        layoutVertical.addWidget(self.cajaTexto)

        contenedor = QWidget()
        contenedor.setLayout(layoutVertical)
        self.setCentralWidget(contenedor)

        # --- Señales ---
        self.boton.clicked.connect(self.mostrarVentana)
        # Cada vez que cambia el texto -> se pone en la etiqueta de la otra ventana
        self.cajaTexto.textChanged.connect(self.otraVentana.etiqueta.setText)

    # --- Funciones (slots) ---
    def mostrarVentana(self):
        if self.otraVentana.isVisible():
            self.otraVentana.hide()
        else:
            self.otraVentana.show()


# PENDIENTE (lo pidió la profesora en clase, todavía sin hacer):
#   fecha.setCalendarPopup(True)  y  fecha.setMinimumDate(QDate(2006, 1, 1))

# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
