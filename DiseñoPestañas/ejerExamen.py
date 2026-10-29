from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar, QDateEdit, QCalendarWidget, QTabWidget, QLineEdit, QComboBox, QSpinBox, QDial, QSlider, QListWidget, QCheckBox, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QPushButton, QStackedLayout
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import Qt, QDate
from cuadrado import Color
import os

CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_IMAGEN = os.path.join(CARPETA, "Img", "imagen-aleatoria-destacada.webp")


class datosPersonales(QWidget):

    def __init__(self):
        super().__init__()

        contenedorPrincipal = QHBoxLayout()
        contenedorIzquierda = QVBoxLayout()
        contenedorArribaIzq = QHBoxLayout()
        contenedorFotoIzq = QVBoxLayout()
        contenedorVacio = QVBoxLayout()
        contenedorFotoDer = QVBoxLayout()
        contenedorAbajoIzq = QVBoxLayout()

        contenedorDerecha = QVBoxLayout()

        # MENSAJE CANDIDATO
        etiquetaCandidato = QLabel("FOTO CANDIDATO")
        formato = etiquetaCandidato.font()
        formato.setBold(True)
        formato.setFamily("Arial")
        etiquetaCandidato.setFont(formato)

        # IMAGEN
        etiqueta = QLabel()
        imagen = QPixmap(RUTA_IMAGEN)
        if imagen.isNull():
            etiqueta.setText("No se ha encontrado la imagen")
        else:
            etiqueta.setPixmap(imagen)

        # BOTON ABAJO IZQ
        self.estadoVerificado = QPushButton()
        self.estadoVerificado.clicked.connect(self.cambiarEstado)

        # COLOR ABAJO IZQ
        self.pilaColores = QStackedLayout()
        rojo = Color("red")
        rojo.setFixedHeight(20)
        self.pilaColores.addWidget(rojo)
        verde = Color("green")
        verde.setFixedHeight(20)
        self.pilaColores.addWidget(verde)

        # BARRA DERECHA
        nombreApellidos = QLabel("Nombre y apellidos")
        self.campoNombreApellidos = QLineEdit()
        self.campoNombreApellidos.setPlaceholderText(
            "Introduce tu nombre completo...")
        self.campoNombreApellidos.textChanged.connect(self.nombreCandidato)

        self.textoCanditado = QLabel()

        rol = QLabel("Rol del candidato")
        comboBox = QComboBox()
        comboBox.addItems(["DAM", "SMR", "DAW"])

        tecnologías = QLabel("Tecnologías")
        listaTecnologías = QListWidget()
        listaTecnologías.addItems(["Sprins", "Python", "Moviles"])

        terminos = QCheckBox("Acepto los terminos y condiciones")

        contenedorFotoIzq.addWidget(etiquetaCandidato)
        contenedorFotoIzq.addWidget(etiqueta)
        contenedorArribaIzq.addLayout(contenedorFotoIzq)
        contenedorArribaIzq.addLayout(contenedorVacio)

        contenedorAbajoIzq.addWidget(self.estadoVerificado)
        contenedorAbajoIzq.addLayout(self.pilaColores)
        contenedorIzquierda.addLayout(contenedorArribaIzq)
        contenedorIzquierda.addLayout(contenedorAbajoIzq)

        contenedorDerecha.addWidget(nombreApellidos)
        contenedorDerecha.addWidget(self.campoNombreApellidos)
        contenedorDerecha.addWidget(self.textoCanditado)
        contenedorDerecha.addWidget(rol)
        contenedorDerecha.addWidget(comboBox)
        contenedorDerecha.addWidget(tecnologías)
        contenedorDerecha.addWidget(listaTecnologías)
        contenedorDerecha.addWidget(terminos)

        contenedorPrincipal.addLayout(contenedorIzquierda)
        contenedorPrincipal.addLayout(contenedorDerecha)

        self.setLayout(contenedorPrincipal)

    def cambiarEstado(self, estado):
        self.estadoVerificado.setText(
            ["Estado: Sin verificar", " ", "Estado: Verificado"])
        self.pilaColores.setCurrentIndex(estado)

    def nombreCandidato(self, texto):
        self.textoCanditado.setText(f"CANDIDATO: {texto}")


class nivelMetricas(QWidget):
    def __init__(self):
        super().__init__()

        contenedor1 = QHBoxLayout()
        contenedor2 = QHBoxLayout()
        contenedorVerticales = QVBoxLayout()
        contenedorDial = QVBoxLayout()
        contenedorApoyo = QVBoxLayout()
        contenedorHorizontal = QHBoxLayout()
        contenedorPrincipal = QVBoxLayout()

        texto = QLabel("Ajuste del nuvel de competencia y Dedicación (%)")

        textoSpinbox = QLabel("1. Selector SpinBox:")
        self.spinBox = QSpinBox()
        self.spinBox.setRange(0, 100)
        self.spinBox.setSingleStep(1)
        self.spinBox.setSuffix("%")
        self.spinBox.valueChanged.connect(self.cambioValores)

        contenedor1.addWidget(textoSpinbox)
        contenedor1.addWidget(self.spinBox)

        textoSlider = QLabel("2. Slider Horizontal: ")
        self.barra = QSlider(Qt.Orientation.Horizontal)
        self.barra.setRange(0, 100)
        self.barra.valueChanged.connect(self.cambioValores)

        contenedor2.addWidget(textoSlider)
        contenedor2.addWidget(self.barra)

        contenedorVerticales.addLayout(contenedor1)
        contenedorVerticales.addLayout(contenedor2)

        textoDial = QLabel("3. Dial Giratorio: ")
        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.dial.setRange(0, 100)
        self.dial.valueChanged.connect(self.cambioValores)

        contenedorDial.addWidget(textoDial)
        contenedorDial.addWidget(self.dial)

        textoApoyo = QLabel("Cuadro de apoyo")
        etiqueta = Color("green")
        etiqueta.setFixedHeight(80)
        self.valor = QLabel("Valor actual: ")

        contenedorApoyo.addWidget(textoApoyo)
        contenedorApoyo.addWidget(etiqueta)
        contenedorApoyo.addWidget(self.valor)

        contenedorHorizontal.addLayout(contenedorDial)
        contenedorHorizontal.addLayout(contenedorApoyo)

        contenedorPrincipal.addLayout(contenedorVerticales)
        contenedorPrincipal.addLayout(contenedorHorizontal)

        self.setLayout(contenedorPrincipal)

    def cambioValores(self, valor):
        self.spinBox.setValue(valor)
        self.dial.setValue(valor)
        self.barra.setValue(valor)
        self.valor.setText(f"Valor actual: {valor}%")


class calendarioYFechas(QWidget):
    def __init__(self):
        super().__init__()

        contenedorGlobal = QVBoxLayout()

        fNacimientoAlta = QLabel("Fecha de nacimiento/alta")
        self.fecha = QDateEdit()
        self.fecha.setCalendarPopup(True)
        self.fecha.setDate(QDate.currentDate())
        self.fecha.setMinimumDate(QDate(2006, 1, 1))
        self.fecha.setDisplayFormat("dd/MM/yyyy")
        self.fecha.dateChanged.connect(self.fechaSelec)

        fIncorporacionPrevista = QLabel("Fecha de incorporación prevista")
        self.calendario = QCalendarWidget()
        self.calendario.selectionChanged.connect(self.fechaSelec)

        self.fechaSeleccionada = QLabel("Fecha seleccionada: ")

        contenedorGlobal.addWidget(fNacimientoAlta)
        contenedorGlobal.addWidget(self.fecha)
        contenedorGlobal.addWidget(fIncorporacionPrevista)
        contenedorGlobal.addWidget(self.calendario)
        contenedorGlobal.addWidget(self.fechaSeleccionada)

        self.setLayout(contenedorGlobal)

    def fechaSelec(self):
        self.fechaSeleccionada.setText(
            f"Fecha seleccionada: {self.calendario.selectedDate().toString("dd/MM/yyyy")}")


class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()

        datos = datosPersonales()
        valores = nivelMetricas()
        fechas = calendarioYFechas()

        pestanas = QTabWidget()
        pestanas.setTabPosition(QTabWidget.TabPosition.North)
        pestanas.addTab(datos, "Datos Personales")
        pestanas.addTab(valores, "Valores")
        pestanas.addTab(fechas, "Fechas y calendarios")

        guardar = QLabel("Guardar")
        resume = QLabel("Ver Resumen")
        salir = QLabel("Salir")

        barraAyuda = QToolBar()
        barraAyuda.addWidget(guardar)
        barraAyuda.addWidget(resume)
        barraAyuda.addWidget(salir)

        contenedor = QVBoxLayout()
        contenedor.addWidget(barraAyuda)
        contenedor.addWidget(pestanas)

        padre = QWidget()
        padre.setLayout(contenedor)

        self.setCentralWidget(padre)


app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
