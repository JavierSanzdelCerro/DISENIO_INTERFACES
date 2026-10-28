# EJERCICIO - Formulario: etiqueta + caja de texto + 3 casillas
# Las 3 casillas usan LA MISMA función. Para saber cuál se pulsó: self.sender()
#
# Resultado:   [ Texto ][ caja de texto ]   <- fila (QHBoxLayout)
#              [ ] Opción 1                 <- columna (QVBoxLayout)
#              [ ] Opción 2
#              [ ] Opción 3

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # --- Layouts ---
        layoutPrincipal = QVBoxLayout()   # Padre
        filaTexto = QHBoxLayout()         # Etiqueta + caja de texto
        columnaCasillas = QVBoxLayout()   # Las 3 casillas

        # --- Widgets ---
        etiqueta = QLabel("Texto")
        cajaTexto = QLineEdit()
        casilla1 = QCheckBox("Opción 1")
        casilla2 = QCheckBox("Opción 2")
        casilla3 = QCheckBox("Opción 3")

        # --- Colocar widgets en sus layouts ---
        filaTexto.addWidget(etiqueta)
        filaTexto.addWidget(cajaTexto)

        columnaCasillas.addWidget(casilla1)
        columnaCasillas.addWidget(casilla2)
        columnaCasillas.addWidget(casilla3)

        layoutPrincipal.addLayout(filaTexto)
        layoutPrincipal.addLayout(columnaCasillas)

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layoutPrincipal)
        self.setCentralWidget(contenedor)

        # --- Señales (las 3 a la misma función) ---
        casilla1.stateChanged.connect(self.casillaCambiada)
        casilla2.stateChanged.connect(self.casillaCambiada)
        casilla3.stateChanged.connect(self.casillaCambiada)

    # --- Funciones (slots) ---
    def casillaCambiada(self, estado):  # estado: 0 = desmarcada, 2 = marcada
        casilla = self.sender()                         # La casilla que lanzó la señal
        textosEstado = ["Desmarcado", "", "Marcado"]    # Posición 0, 1 y 2
        print(f"{casilla.text()} - {textosEstado[estado]}")


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
