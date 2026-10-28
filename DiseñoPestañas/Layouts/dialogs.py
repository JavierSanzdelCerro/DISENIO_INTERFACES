# ARCHIVO AUXILIAR - clase CustomDialog (diálogo personalizado con Aceptar/Cancelar)
# No se ejecuta solo: lo usa QDialogButtonBox(dialogoPropioAceptarCancelar).py con  ->  from dialogs import CustomDialog
# (Por eso este archivo NO se renombra: si cambias el nombre, falla el import.)

from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class CustomDialog(QDialog):   # Hereda de QDialog (no de QMainWindow)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cuadro de diálogo")

        # --- Botones estándar: el | junta varios (Ok y Cancel) ---
        botones = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.cajaBotones = QDialogButtonBox(botones)

        # --- Señales ---
        # accept/reject ya vienen en QDialog: cierran el diálogo y hacen que
        # exec() devuelva True (aceptar) o False (cancelar)
        self.cajaBotones.accepted.connect(self.accept)
        self.cajaBotones.rejected.connect(self.reject)

        # --- Layout (un QDialog usa setLayout directamente, no setCentralWidget) ---
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(QLabel("Algo ha sucedido ¿todo Ok?"))
        layoutVertical.addWidget(self.cajaBotones)
        self.setLayout(layoutVertical)
