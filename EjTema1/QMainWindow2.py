import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QToolBar, QDateEdit, QCalendarWidget,
    QTabWidget, QLineEdit, QComboBox, QSpinBox, QDial, QSlider, QListWidget,
    QCheckBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedLayout,
    QDialog, QDialogButtonBox, QMessageBox, QStatusBar, QAbstractItemView
)
from PyQt6.QtGui import QAction, QPixmap, QIcon, QColor
from PyQt6.QtCore import Qt, QDate, QSize

# Ruta de la imagen del proyecto
CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_IMAGEN = os.path.join(CARPETA, "Img", "imagen-aleatoria-destacada.webp")

# Clase Color de apoyo (usa la suya si existe 'cuadrado.py')
try:
    from cuadrado import Color
except Exception:
    class Color(QWidget):
        def __init__(self, color):
            super().__init__()
            self.setAutoFillBackground(True)
            paleta = self.palette()
            paleta.setColor(self.backgroundRole(), QColor(color))
            self.setPalette(paleta)


# =====================================================================
# CLASE 1: PESTAÑA 1 - DATOS PERSONALES
# =====================================================================
class datosPersonales(QWidget):
    def __init__(self):
        super().__init__()

        contenedorPrincipal = QHBoxLayout()
        contenedorIzquierda = QVBoxLayout()
        contenedorDerecha = QVBoxLayout()

        # --- LADO IZQUIERDO: FOTO Y ESTADO ---
        etiquetaCandidato = QLabel("FOTO CANDIDATO")
        formato = etiquetaCandidato.font()
        formato.setBold(True)
        formato.setFamily("Arial")
        formato.setPointSize(14)
        etiquetaCandidato.setFont(formato)

        etiquetaFoto = QLabel()
        imagen = QPixmap(RUTA_IMAGEN)
        if imagen.isNull():
            etiquetaFoto.setText("Foto no encontrada")
        else:
            etiquetaFoto.setPixmap(imagen)
        etiquetaFoto.setFixedSize(140, 140)
        etiquetaFoto.setScaledContents(True)

        # Botón checkable de verificación
        self.estadoVerificado = QPushButton("Estado: Sin verificar")
        self.estadoVerificado.setCheckable(True)
        self.estadoVerificado.clicked.connect(self.cambiarEstado)

        # Cuadro de color con QStackedLayout (Rojo = 0, Verde = 1)
        self.pilaColores = QStackedLayout()
        rojo = Color("red")
        rojo.setFixedHeight(25)
        self.pilaColores.addWidget(rojo)    # Índice 0

        verde = Color("green")
        verde.setFixedHeight(25)
        self.pilaColores.addWidget(verde)  # Índice 1

        contenedorIzquierda.addWidget(etiquetaCandidato)
        contenedorIzquierda.addWidget(etiquetaFoto)
        contenedorIzquierda.addWidget(self.estadoVerificado)
        contenedorIzquierda.addLayout(self.pilaColores)

        # --- LADO DERECHO: FORMULARIO ---
        nombreApellidos = QLabel("Nombre y apellidos:")
        self.campoNombreApellidos = QLineEdit()
        self.campoNombreApellidos.setPlaceholderText("Introduce tu nombre completo...")
        self.campoNombreApellidos.textChanged.connect(self.nombreCandidato)

        self.textoCanditado = QLabel("CANDIDATO: ")
        formatoNombre = self.textoCanditado.font()
        formatoNombre.setBold(True)
        formatoNombre.setPointSize(11)
        self.textoCanditado.setFont(formatoNombre)
        self.textoCanditado.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rol = QLabel("Rol del candidato:")
        self.comboBox = QComboBox()
        self.comboBox.addItems(["DAM", "SMR", "DAW"])
        self.comboBox.setEditable(True)

        tecnologias = QLabel("Tecnologías (Ctrl + Clic múltiple):")
        self.listaTecnologias = QListWidget()
        self.listaTecnologias.addItems(["Spring", "Python & PyQt", "Desarrollo Móvil", "Bases de Datos"])
        self.listaTecnologias.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.terminos = QCheckBox("Acepto los términos y condiciones de empresa")

        contenedorDerecha.addWidget(nombreApellidos)
        contenedorDerecha.addWidget(self.campoNombreApellidos)
        contenedorDerecha.addWidget(self.textoCanditado)
        contenedorDerecha.addWidget(rol)
        contenedorDerecha.addWidget(self.comboBox)
        contenedorDerecha.addWidget(tecnologias)
        contenedorDerecha.addWidget(self.listaTecnologias)
        contenedorDerecha.addWidget(self.terminos)

        contenedorPrincipal.addLayout(contenedorIzquierda)
        contenedorPrincipal.addLayout(contenedorDerecha)
        self.setLayout(contenedorPrincipal)

    def cambiarEstado(self, pulsado):
        if pulsado:
            self.estadoVerificado.setText("Estado: Verificado ✓")
            self.pilaColores.setCurrentIndex(1)  # Muestra el verde
        else:
            self.estadoVerificado.setText("Estado: Sin verificar")
            self.pilaColores.setCurrentIndex(0)  # Muestra el rojo

    def nombreCandidato(self, texto):
        self.textoCanditado.setText(f"CANDIDATO: {texto.upper()}")


# =====================================================================
# CLASE 2: PESTAÑA 2 - NIVEL Y MÉTRICAS
# =====================================================================
class nivelMetricas(QWidget):
    def __init__(self):
        super().__init__()

        contenedorPrincipal = QVBoxLayout()
        contenedorVerticales = QVBoxLayout()
        contenedorHorizontal = QHBoxLayout()

        textoTitulo = QLabel("Ajuste de Nivel de Competencia y Dedicación (%)")
        formato = textoTitulo.font()
        formato.setBold(True)
        formato.setPointSize(14)
        textoTitulo.setFont(formato)

        # 1. SpinBox
        textoSpinbox = QLabel("1. Selector SpinBox:")
        self.spinBox = QSpinBox()
        self.spinBox.setRange(0, 100)
        self.spinBox.setSingleStep(1)
        self.spinBox.setSuffix(" %")
        self.spinBox.valueChanged.connect(self.cambioValores)

        fila1 = QHBoxLayout()
        fila1.addWidget(textoSpinbox)
        fila1.addWidget(self.spinBox)

        # 2. Slider
        textoSlider = QLabel("2. Slider Horizontal:")
        self.barra = QSlider(Qt.Orientation.Horizontal)
        self.barra.setRange(0, 100)
        self.barra.valueChanged.connect(self.cambioValores)

        fila2 = QHBoxLayout()
        fila2.addWidget(textoSlider)
        fila2.addWidget(self.barra)

        contenedorVerticales.addLayout(fila1)
        contenedorVerticales.addLayout(fila2)

        # 3. Dial
        contenedorDial = QVBoxLayout()
        textoDial = QLabel("3. Dial Giratorio:")
        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.dial.setRange(0, 100)
        self.dial.valueChanged.connect(self.cambioValores)
        contenedorDial.addWidget(textoDial)
        contenedorDial.addWidget(self.dial)

        # 4. Cuadro de apoyo y texto de valor
        contenedorApoyo = QVBoxLayout()
        textoApoyo = QLabel("Cuadro de apoyo visual")
        cuadroColor = Color("blue")
        cuadroColor.setFixedHeight(70)

        self.valor = QLabel("Valor actual: 0%")
        formatoValor = self.valor.font()
        formatoValor.setBold(True)
        formatoValor.setPointSize(12)
        self.valor.setFont(formatoValor)

        contenedorApoyo.addWidget(textoApoyo)
        contenedorApoyo.addWidget(cuadroColor)
        contenedorApoyo.addWidget(self.valor)

        contenedorHorizontal.addLayout(contenedorDial)
        contenedorHorizontal.addLayout(contenedorApoyo)

        contenedorPrincipal.addWidget(textoTitulo)
        contenedorPrincipal.addLayout(contenedorVerticales)
        contenedorPrincipal.addLayout(contenedorHorizontal)
        self.setLayout(contenedorPrincipal)

    def cambioValores(self, valor):
        self.spinBox.setValue(valor)
        self.barra.setValue(valor)
        self.dial.setValue(valor)
        self.valor.setText(f"Valor actual: {valor}%")


# =====================================================================
# CLASE 3: PESTAÑA 3 - CALENDARIO Y FECHAS
# =====================================================================
class calendarioYFechas(QWidget):
    def __init__(self):
        super().__init__()

        contenedorGlobal = QVBoxLayout()

        fNacimientoAlta = QLabel("Fecha de nacimiento / Alta (Mínimo 01/01/2006):")
        self.fecha = QDateEdit()
        self.fecha.setCalendarPopup(True)
        self.fecha.setDate(QDate.currentDate())
        self.fecha.setMinimumDate(QDate(2006, 1, 1))
        self.fecha.setDisplayFormat("dd/MM/yyyy")

        fIncorporacionPrevista = QLabel("Fecha de incorporación prevista:")
        self.calendario = QCalendarWidget()
        self.calendario.selectionChanged.connect(self.fechaSelec)

        self.fechaSeleccionada = QLabel("Fecha seleccionada: ")
        formatoFecha = self.fechaSeleccionada.font()
        formatoFecha.setBold(True)
        formatoFecha.setPointSize(12)
        self.fechaSeleccionada.setFont(formatoFecha)
        self.fechaSeleccionada.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Inicializamos con la fecha actual
        self.fechaSelec()

        contenedorGlobal.addWidget(fNacimientoAlta)
        contenedorGlobal.addWidget(self.fecha)
        contenedorGlobal.addWidget(fIncorporacionPrevista)
        contenedorGlobal.addWidget(self.calendario)
        contenedorGlobal.addWidget(self.fechaSeleccionada)
        self.setLayout(contenedorGlobal)

    def fechaSelec(self):
        fechaTexto = self.calendario.selectedDate().toString("dd/MM/yyyy")
        self.fechaSeleccionada.setText(f"Fecha seleccionada: {fechaTexto}")


# =====================================================================
# CLASE 4: DIÁLOGO MODAL DE GUARDAR (QDialog)
# =====================================================================
class DialogoGuardar(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Confirmar Guardado")

        layout = QVBoxLayout()
        mensaje = QLabel("¿Estás seguro de que deseas guardar los cambios en la ficha?")

        botones = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.cajaBotones = QDialogButtonBox(botones)
        self.cajaBotones.accepted.connect(self.accept)
        self.cajaBotones.rejected.connect(self.reject)

        layout.addWidget(mensaje)
        layout.addWidget(self.cajaBotones)
        self.setLayout(layout)


# =====================================================================
# CLASE 5: VENTANA SECUNDARIA - RESUMEN DE EXPEDIENTE
# =====================================================================
class VentanaResumen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ficha Resumen del Candidato")
        self.resize(450, 320)

        layout = QVBoxLayout()

        titulo = QLabel("RESUMEN CONSOLIDADO DE EXPEDIENTE")
        formato = titulo.font()
        formato.setBold(True)
        formato.setPointSize(13)
        titulo.setFont(formato)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblNombre = QLabel("Nombre: -")
        self.lblRol = QLabel("Rol / Especialidad: -")
        self.lblNivel = QLabel("Nivel / Dedicación: -")
        self.lblFecha = QLabel("Fecha de Inicio: -")
        self.lblEstado = QLabel("Estado: -")
        self.lblTecnologias = QLabel("Tecnologías: -")

        btnCerrar = QPushButton("Cerrar Ventana de Resumen")
        btnCerrar.clicked.connect(self.hide)

        layout.addWidget(titulo)
        layout.addWidget(self.lblNombre)
        layout.addWidget(self.lblRol)
        layout.addWidget(self.lblNivel)
        layout.addWidget(self.lblFecha)
        layout.addWidget(self.lblEstado)
        layout.addWidget(self.lblTecnologias)
        layout.addWidget(btnCerrar)
        self.setLayout(layout)


# =====================================================================
# CLASE 6: VENTANA PRINCIPAL (QMainWindow con QAction, Menú y ToolBar)
# =====================================================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TalentHub DAM - Gestor Integrador de Perfiles")
        self.resize(850, 600)

        # 0. Instancia persistente de la ventana secundaria
        self.ventanaResumen = VentanaResumen()

        # 1. PESTAÑAS (Con self. para poder leerlas en el resumen)
        self.datos = datosPersonales()
        self.valores = nivelMetricas()
        self.fechas = calendarioYFechas()

        pestanas = QTabWidget()
        pestanas.setTabPosition(QTabWidget.TabPosition.North)
        pestanas.setMovable(True)
        pestanas.addTab(self.datos, "Datos Personales")
        pestanas.addTab(self.valores, "Nivel y Métricas")
        pestanas.addTab(self.fechas, "Fechas y Calendarios")

        # El centro de la ventana son directamente las pestañas
        self.setCentralWidget(pestanas)

        # 2. ACCIONES (QAction)
        accionGuardar = QAction("Guardar", self)
        accionGuardar.setStatusTip("Guardar cambios de la ficha técnica")
        accionGuardar.triggered.connect(self.guardarFicha)

        accionResumen = QAction("Ver Resumen", self)
        accionResumen.setStatusTip("Mostrar resumen consolidado del expediente")
        accionResumen.triggered.connect(self.abrirResumen)

        accionSalir = QAction("Salir", self)
        accionSalir.setStatusTip("Salir de la aplicación")
        accionSalir.triggered.connect(self.salirApp)

        # 3. BARRA DE HERRAMIENTAS (QToolBar)
        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(24, 24))
        self.addToolBar(barra)

        barra.addAction(accionGuardar)
        barra.addSeparator()
        barra.addAction(accionResumen)
        barra.addSeparator()
        barra.addAction(accionSalir)

        # 4. BARRA DE MENÚ (QMenuBar)
        menuArchivo = self.menuBar().addMenu("&Archivo")
        menuArchivo.addAction(accionGuardar)
        menuArchivo.addAction(accionResumen)
        menuArchivo.addSeparator()
        menuArchivo.addAction(accionSalir)

        menuAyuda = self.menuBar().addMenu("&Ayuda")
        accionAcerca = QAction("Acerca de...", self)
        accionAcerca.triggered.connect(self.mostrarAcercaDe)
        menuAyuda.addAction(accionAcerca)

        # 5. BARRA DE ESTADO INFERIOR (QStatusBar)
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Listo.")

    # --- FUNCIONES DE LOS BOTONES ---
    def guardarFicha(self):
        dialogo = DialogoGuardar()
        if dialogo.exec():
            self.statusBar().showMessage("✓ Ficha guardada con éxito en el sistema.")
        else:
            self.statusBar().showMessage("Operación de guardado cancelada.")

    def abrirResumen(self):
        # 1. Leemos datos de Pestaña 1
        nombre = self.datos.campoNombreApellidos.text()
        verificado = self.datos.estadoVerificado.text()
        rol = self.datos.comboBox.currentText()
        tecnologias = [item.text() for item in self.datos.listaTecnologias.selectedItems()]
        textoTecnologias = ", ".join(tecnologias) if tecnologias else "Ninguna seleccionada"

        # 2. Leemos datos de Pestaña 2
        nivel = self.valores.spinBox.value()

        # 3. Leemos datos de Pestaña 3
        fecha = self.fechas.calendario.selectedDate().toString("dd/MM/yyyy")

        # 4. Actualizamos la ventana secundaria
        self.ventanaResumen.lblNombre.setText(f"Nombre: {nombre if nombre else '(Sin nombre)'}")
        self.ventanaResumen.lblRol.setText(f"Rol / Especialidad: {rol}")
        self.ventanaResumen.lblNivel.setText(f"Nivel / Dedicación: {nivel} %")
        self.ventanaResumen.lblFecha.setText(f"Fecha de Inicio: {fecha}")
        self.ventanaResumen.lblEstado.setText(f"Estado de Verificación: {verificado}")
        self.ventanaResumen.lblTecnologias.setText(f"Tecnologías dominadas: {textoTecnologias}")

        # 5. La mostramos
        self.ventanaResumen.show()

    def salirApp(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar Salida",
            "¿Seguro que deseas salir de TalentHub DAM?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if respuesta == QMessageBox.StandardButton.Yes:
            self.ventanaResumen.close()
            self.close()

    def mostrarAcercaDe(self):
        QMessageBox.information(
            self,
            "Acerca de TalentHub DAM",
            "TalentHub DAM v1.0\nAplicación integradora de Diseño de Interfaces (2º DAM)."
        )


# =====================================================================
# ARRANQUE DE LA APLICACIÓN
# =====================================================================
if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()