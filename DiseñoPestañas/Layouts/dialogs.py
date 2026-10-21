from PyQt6.QtWidgets import QDialog, QApplication, QDialogButtonBox, QLabel, QVBoxLayout


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cuadro de diálogo")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.dialogBox = QDialogButtonBox(QBtn)
        self.dialogBox.accepted.connect(self.accept) # rol de aceptar
        self.dialogBox.rejected.connect(self.reject) # rol de cancelar

        self.plantilla = QVBoxLayout()
        mensaje = QLabel("Algo ha sucedido ¿todo Ok?")
        self.plantilla.addWidget(mensaje)
        self.plantilla.addWidget(self.dialogBox)
        self.setLayout(self.plantilla)