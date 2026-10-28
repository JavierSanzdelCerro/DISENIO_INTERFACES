# EJERCICIO (en clase: Ej34) - El mismo botón abre y cierra la segunda ventana
# Se usa None para saber si la ventana existe:
#   None  -> no hay ventana -> se crea y se muestra
#   otra cosa -> ya hay ventana -> se cierra y se vuelve a poner None
# (Cada vez que se abre es una ventana NUEVA: lo escrito en ella se pierde.)

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

        # --- Datos ---
        self.otraVentana = None   # Al empezar no hay segunda ventana

        # --- Widgets + señales ---
        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.mostrarVentana)
        self.setCentralWidget(boton)

    # --- Funciones (slots) ---
    def mostrarVentana(self):
        if self.otraVentana is None:
            self.otraVentana = OtraVentana()
            self.otraVentana.show()
        else:
            self.otraVentana.close()
            self.otraVentana = None


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
