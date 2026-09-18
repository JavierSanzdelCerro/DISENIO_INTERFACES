from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("<Mi aplicacion")

        label = QLabel("Hola")        
        formato = label.font()
        formato.setPointSize(30)
        formato.setFamily("Arial")
        formato.setBold(True)
        label.setFont(formato)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)


        self.setCentralWidget(label)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()