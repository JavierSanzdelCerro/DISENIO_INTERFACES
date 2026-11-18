from paleta_oscura_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Desactivar el grupo desactiva también todo lo que tiene dentro
        self.grpDesactivados.setEnabled(False)

app = QApplication([])
app.setStyle("Fusion")  # sin Fusion la paleta no se aplica

gris_oscuro = QColor(45, 45, 45)
gris_medio = QColor(60, 60, 60)
azul = QColor(42, 130, 218)

paleta = QPalette()
# Colores normales (grupo activo). Qt.GlobalColor son colores ya definidos (white, black, red...)
paleta.setColor(QPalette.ColorRole.Window, gris_oscuro)                    # fondo de la ventana
paleta.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)       # textos de la ventana
paleta.setColor(QPalette.ColorRole.Base, QColor(30, 30, 30))               # fondo de campos y listas
paleta.setColor(QPalette.ColorRole.AlternateBase, gris_medio)              # filas alternas (alternatingRowColors)
paleta.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)             # texto de campos y listas
paleta.setColor(QPalette.ColorRole.PlaceholderText, Qt.GlobalColor.gray)   # texto de ayuda de los campos
paleta.setColor(QPalette.ColorRole.Button, gris_medio)                     # fondo de botones
paleta.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)       # texto de botones
paleta.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)         # texto que debe resaltar mucho
paleta.setColor(QPalette.ColorRole.Link, azul)                             # enlaces
paleta.setColor(QPalette.ColorRole.Highlight, azul)                        # fondo de lo seleccionado
paleta.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)  # texto de lo seleccionado
paleta.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)      # fondo del tooltip
paleta.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.black)      # texto del tooltip

# Colores SOLO para widgets desactivados: setColor(grupo, rol, color)
paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, Qt.GlobalColor.darkGray)
paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, Qt.GlobalColor.darkGray)
paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, Qt.GlobalColor.darkGray)
paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, gris_oscuro)
app.setPalette(paleta)

window = MainWindow()
app.exec()
