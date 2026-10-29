# EJERCICIO - QDateEdit + QCalendarWidget: dos formas de elegir una fecha
#
#   [ 29/10/2026 |v]                  <- QDateEdit: cajita con calendario desplegable
#   Fecha de la cajita: 29/10/2026    <- QLabel que cambia al cambiar la cajita
#   [  calendario  ]                  <- QCalendarWidget: calendario grande siempre visible
#   Fecha seleccionada: 29/10/2026    <- QLabel que cambia al pulsar un día

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCalendarWidget, QDateEdit, QLabel
from PyQt6.QtCore import QDate


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Widgets (con self para leer la fecha desde las funciones) ---
        self.fecha = QDateEdit()
        self.fecha.setCalendarPopup(True)
        self.fecha.setDate(QDate.currentDate())
        self.fecha.setMinimumDate(QDate(2006, 1, 1))
        self.fecha.setDisplayFormat("dd/MM/yyyy")

        self.textoCajita = QLabel()

        self.calendario = QCalendarWidget()

        self.textoCalendario = QLabel()

        # --- Señales ---
        self.fecha.dateChanged.connect(self.mostrarFechaCajita)
        self.calendario.selectionChanged.connect(self.mostrarFecha)

        # --- Texto inicial (para que al arrancar ya salga la fecha de hoy) ---
        self.mostrarFechaCajita(self.fecha.date())
        self.mostrarFecha()

        # --- Layout: uno encima del otro ---
        layout = QVBoxLayout()
        layout.addWidget(self.fecha)
        layout.addWidget(self.textoCajita)
        layout.addWidget(self.calendario)
        layout.addWidget(self.textoCalendario)

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    # --- Funciones (slots) ---
    def mostrarFechaCajita(self, fecha):   # dateChanged envía la fecha
        self.textoCajita.setText("Fecha de la cajita: " + fecha.toString("dd/MM/yyyy"))

    def mostrarFecha(self):                # selectionChanged no envía nada
        self.textoCalendario.setText("Fecha seleccionada: " + self.calendario.selectedDate().toString("dd/MM/yyyy"))


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()