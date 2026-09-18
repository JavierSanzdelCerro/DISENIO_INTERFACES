from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.contador = 0
        self.setWindowTitle("<Mi aplicacion")

        label = QLabel()
        input = QLineEdit()

        input.textChanged.connect(label.setText)

        layout = QVBoxLayout()
        layout.addWidget(input)
        layout.addWidget(label)

        contenedor = QWidget()
        contenedor.setLayout(layout)

        self.setCentralWidget(contenedor)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()