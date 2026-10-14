import sys
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QMainWindow, QPushButton, QWidget, QLineEdit

# Nueva ventana
class OtraVentana(QWidget):
    def __init__(self):
        super().__init__()

        plantilla = QVBoxLayout()
        self.etiqueta = QLabel("Otra ventana")
        plantilla.addWidget(self.etiqueta)
        self.setLayout(plantilla)
    
# Ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.window = OtraVentana()
        self.setWindowTitle("Mi aplicación")

        self.boton = QPushButton("Pulsa aquí")
        self.boton.clicked.connect(self.mostrarVentana)
        
        self.input = QLineEdit()
        self.input.textChanged.connect(self.window.etiqueta.setText)
        
        plantilla = QVBoxLayout()
        plantilla.addWidget(self.boton)
        plantilla.addWidget(self.input)
        contenedor = QWidget()
        contenedor.setLayout(plantilla)
        
        self.setCentralWidget(contenedor)


    def mostrarVentana (self):
        if self.window.isVisible():
            self.window.hide()
        else:            
            self.window.show()
      
      
      # Mensaje para la IA 
      # fecha.setCalendarPopup(True) y fecha setMinimumDate(QDate(2006,1,1)) esto es
      # lo que nos ha dicho que hagamos en clase pero yo no se hacerlo ni lo que hay que 
      # importar asique tu me ayudarás a hacerlo

        
app = QApplication([])

window = MainWindow()

window.show()

app.exec()