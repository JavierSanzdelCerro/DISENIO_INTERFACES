# EJERCICIO - QGroupBox (marco con título) + QRadioButton (botón de opción)
# Un QGroupBox se usa como un contenedor: se le pone un layout con setLayout().
# Los QRadioButton del mismo grupo son excluyentes: solo uno marcado a la vez.
#
# Resultado:   ┌ Botones ──┐ ┌ Radios ───┐
#              │ Botón 1   │ │ o Radio 1 │
#              │ Botón 2   │ │ o Radio 2 │
#              │ Botón 3   │ │ o Radio 3 │
#              └───────────┘ └───────────┘

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QGroupBox, QRadioButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        layoutPrincipal = QHBoxLayout()   # Padre: los dos grupos uno al lado del otro

        # --- Grupo 1: botones normales ---
        grupoBotones = QGroupBox("Botones")
        layoutBotones = QVBoxLayout()

        boton1 = QPushButton("Botón 1")
        boton2 = QPushButton("Botón 2")
        boton3 = QPushButton("Botón 3")
        layoutBotones.addWidget(boton1)
        layoutBotones.addWidget(boton2)
        layoutBotones.addWidget(boton3)

        grupoBotones.setLayout(layoutBotones)
        layoutPrincipal.addWidget(grupoBotones)

        # --- Grupo 2: radio buttons ---
        grupoRadios = QGroupBox("Radios")
        layoutRadios = QVBoxLayout()

        radio1 = QRadioButton("Radio 1")
        radio2 = QRadioButton("Radio 2")
        radio3 = QRadioButton("Radio 3")
        layoutRadios.addWidget(radio1)
        layoutRadios.addWidget(radio2)
        layoutRadios.addWidget(radio3)

        grupoRadios.setLayout(layoutRadios)
        layoutPrincipal.addWidget(grupoRadios)

        # --- Contenedor -> centro de la ventana ---
        contenedor = QWidget()
        contenedor.setLayout(layoutPrincipal)
        self.setCentralWidget(contenedor)

        # --- Señales (todos a la misma función) ---
        for elemento in [boton1, boton2, boton3, radio1, radio2, radio3]:
            elemento.clicked.connect(self.botonPulsado)

    # --- Funciones (slots) ---
    def botonPulsado(self):
        boton = self.sender()   # El botón/radio que se ha pulsado
        print(f"{boton.text()} pulsado")


# --- Arranque de la aplicación ---
app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
