# EJERCICIO (en clase: Ej32) - QMessageBox: cuadro de mensaje ya hecho, con icono y botones Sí / No
# Diferencia con QDialogButtonBox(dialogoPropioAceptarCancelar): no hace falta crear una clase, QMessageBox ya trae todo.

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets + señales ---
        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.botonPulsado)
        self.setCentralWidget(boton)

    # --- Funciones (slots) ---
    def botonPulsado(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Cuadro de mensaje")
        mensaje.setText("Este es el mensaje de mi cuadro de mensaje")
        mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        mensaje.setIcon(QMessageBox.Icon.Information)   # Otros: Warning, Critical, Question

        # Aquí exec() devuelve QUÉ botón se pulsó, por eso se compara con Yes
        if mensaje.exec() == QMessageBox.StandardButton.Yes:
            print("El usuario ha aceptado")
        else:
            print("El usuario ha rechazado")


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
