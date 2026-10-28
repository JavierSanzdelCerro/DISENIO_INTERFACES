# EJERCICIO - QComboBox: lista desplegable (solo se ve la opción elegida)
#   addItems([...]) -> añade varias opciones     addItem("...") -> añade una
#   setEditable(True) -> además deja escribir una opción nueva
#
# Dos señales distintas para lo mismo:
#   currentIndexChanged -> envía la POSICIÓN (0, 1, 2...)
#   currentTextChanged  -> envía el TEXTO   ("Uno", "Dos"...)

from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        desplegable = QComboBox()
        desplegable.addItems(["Uno", "Dos", "Tres"])
        desplegable.addItem("Cuatro")
        desplegable.setEditable(True)

        # --- Señales ---
        desplegable.currentIndexChanged.connect(self.indiceCambiado)
        desplegable.currentTextChanged.connect(self.textoCambiado)

        self.setCentralWidget(desplegable)

    # --- Funciones (slots) ---
    def indiceCambiado(self, indice):   # Número: 0, 1, 2...
        print("Posición:", indice)

    def textoCambiado(self, texto):     # Texto de la opción
        print("Texto:", texto)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
