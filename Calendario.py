from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("<Mi aplicacion")

        self.calendario = QCalendarWidget()
        self.calendario.selectionChanged.connect(self.mostrarFecha)


        self.setCentralWidget(self.calendario)

    def mostrarFecha(self):
        print(self.calendario.selectedDate().toString("dd/MM/yyyy"))

app = QApplication([])

window = MainWindow()

window.show()

app.exec()