# EJERCICIO - QSpinBox: caja de número con flechas arriba / abajo
#   setRange(-10, 10)  -> mínimo y máximo
#   setSingleStep(2)   -> cuánto sube o baja con cada flecha
#   setSuffix(" €")    -> texto que se pone detrás del número
#
# Dos señales distintas:
#   valueChanged -> envía el NÚMERO           (ej: 4)
#   textChanged  -> envía el TEXTO que se ve  (ej: "4 €")

from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        cajaNumero = QSpinBox()
        cajaNumero.setRange(-10, 10)
        cajaNumero.setSingleStep(2)
        cajaNumero.setSuffix(" €")

        # --- Señales (cada una a su función para ver la diferencia) ---
        cajaNumero.valueChanged.connect(self.valorCambiado)
        cajaNumero.textChanged.connect(self.textoCambiado)

        self.setCentralWidget(cajaNumero)

    # --- Funciones (slots) ---
    def valorCambiado(self, valor):
        print("Valor:", valor)

    def textoCambiado(self, texto):
        print("Texto:", texto)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
