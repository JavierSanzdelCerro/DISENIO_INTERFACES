# EJERCICIO - QListWidget: lista con TODAS las opciones a la vista (no se despliega)
# Con MultiSelection se pueden elegir varias a la vez (cada clic marca/desmarca).
#
#   currentTextChanged    -> texto del ÚLTIMO elemento pulsado (solo uno)
#   itemSelectionChanged  -> avisa de que cambió la selección (no envía nada);
#                            luego selectedItems() da TODOS los elegidos

from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QAbstractItemView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets ---
        self.lista = QListWidget()
        self.lista.addItems(["Uno", "Dos", "Tres"])

        # Permitir elegir varios elementos
        self.lista.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        # --- Señales ---
        self.lista.currentTextChanged.connect(self.textoCambiado)
        self.lista.itemSelectionChanged.connect(self.seleccionCambiada)

        self.setCentralWidget(self.lista)

    # --- Funciones (slots) ---
    def textoCambiado(self, texto):
        print("Último pulsado:", texto)

    def seleccionCambiada(self):
        elegidos = [elemento.text() for elemento in self.lista.selectedItems()]
        print("Seleccionados:", elegidos)


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
