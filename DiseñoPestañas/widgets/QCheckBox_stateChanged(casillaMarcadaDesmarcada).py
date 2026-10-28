# EJERCICIO - QCheckBox: casilla de verificación que cambia su texto al marcarla
#   stateChanged envía un NÚMERO: 0 = desmarcada, 1 = a medias, 2 = marcada
#   Por eso la lista tiene 3 huecos y el del medio está vacío (no se usa).

from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        self.casilla = QCheckBox("Casilla de verificación")

        # Texto en negrita (sacar fuente -> cambiar -> volver a poner)
        fuente = self.casilla.font()
        fuente.setBold(True)
        self.casilla.setFont(fuente)

        # --- Señales ---
        self.casilla.stateChanged.connect(self.estadoCambiado)

        self.setCentralWidget(self.casilla)

    # --- Funciones (slots) ---
    def estadoCambiado(self, estado):   # estado: 0, 1 o 2
        textosEstado = ["Desmarcado", "", "Marcado"]   # Posición 0, 1 y 2
        self.casilla.setText(textosEstado[estado])
        print(textosEstado[estado])


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
