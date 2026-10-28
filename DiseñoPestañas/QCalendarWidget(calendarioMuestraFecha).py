# EJERCICIO - QCalendarWidget: calendario; al elegir un día se escribe la fecha
#   selectionChanged -> avisa de que cambió el día (no envía nada)
#   selectedDate()   -> devuelve el día elegido (un QDate)
#   .toString("dd/MM/yyyy") -> lo pasa a texto. OJO: MM = mes, mm = minutos

from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets (con self para leer la fecha desde la función) ---
        self.calendario = QCalendarWidget()

        # --- Señales ---
        self.calendario.selectionChanged.connect(self.mostrarFecha)

        self.setCentralWidget(self.calendario)

    # --- Funciones (slots) ---
    def mostrarFecha(self):
        print(self.calendario.selectedDate().toString("dd/MM/yyyy"))


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
