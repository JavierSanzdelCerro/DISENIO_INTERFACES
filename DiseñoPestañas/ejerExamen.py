from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QToolBar


class toobar(QWidget):
    def __init__(self):
        super().__init__()

        arriba = QToolBar()
        





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()



app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()