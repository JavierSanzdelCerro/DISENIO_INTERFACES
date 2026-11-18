from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QStyle
from PyQt6.QtCore import QTime, QDate
from rodaje_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        ## VALORES INICIALES
        self.comboCamara.addItems(["Cámara A", "Cámara B", "Cámara C"])
        self.timeHora.setTime(QTime.currentTime())          # hora de ahora
        self.timeHora.setDisplayFormat("HH:mm")
        self.calendario.setSelectedDate(QDate.currentDate())  # fecha de hoy
        self.btnAnadir.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton))
        self.btnBorrarToma.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TrashIcon))

        ## DURACIÓN: dial y slider se mueven juntos y el LCD enseña los segundos
        self.dialDuracion.valueChanged.connect(self.sliderDuracion.setValue)
        self.sliderDuracion.valueChanged.connect(self.dialDuracion.setValue)
        self.dialDuracion.valueChanged.connect(self.lcdDuracion.display)

        ## TOMAS PREVISTAS: el slider vertical marca cuántas tomas hay que grabar
        self.sliderPrevistas.valueChanged.connect(self.cambiarPrevistas)

        ## RESUMEN DE LA SIGUIENTE TOMA: se actualiza al cambiar cualquier dato
        self.editEscena.textChanged.connect(self.actualizarResumen)
        self.spinToma.valueChanged.connect(self.actualizarResumen)
        self.comboCamara.currentTextChanged.connect(self.actualizarResumen)
        self.dialDuracion.valueChanged.connect(self.actualizarResumen)

        ## BOTONES
        self.btnAnadir.clicked.connect(self.anadirToma)
        self.btnBorrarToma.clicked.connect(self.borrarToma)

        ## NOTAS: contador de caracteres
        self.textNotas.textChanged.connect(self.contarCaracteres)

        ## MENÚ
        self.actionSalir.triggered.connect(self.salir)

        self.actualizarResumen()
        self.actualizarProgreso()

    def cambiarPrevistas(self, valor):
        self.lblNumPrevistas.setText(str(valor))
        self.actualizarProgreso()

    def actualizarResumen(self):
        escena = self.editEscena.text() or "—"
        self.lblResumen.setText(f"Siguiente: escena {escena} · toma {self.spinToma.value()} · "
                                f"{self.comboCamara.currentText()} · {self.dialDuracion.value()} s")

    def anadirToma(self):
        if self.editEscena.text() == "":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Falta la escena")
            dlg.setText("Escribe el nombre de la escena antes de añadir la toma")
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
            return

        fecha = self.calendario.selectedDate().toString("dd/MM/yyyy")
        hora = self.timeHora.time().toString("HH:mm")
        toma = (f"{fecha} {hora} | Escena {self.editEscena.text()} · Toma {self.spinToma.value()} · "
                f"{self.comboCamara.currentText()} · {self.dialDuracion.value()} s")
        self.listaTomas.addItem(toma)

        self.spinToma.setValue(self.spinToma.value() + 1)   # la siguiente toma
        self.actualizarProgreso()
        self.statusbar.showMessage("Toma añadida", 3000)

    def borrarToma(self):
        fila = self.listaTomas.currentRow()                  # -1 si no hay ninguna seleccionada
        if fila >= 0:
            self.listaTomas.takeItem(fila)
            self.actualizarProgreso()
            self.statusbar.showMessage("Toma borrada", 3000)

    def actualizarProgreso(self):
        hechas = self.listaTomas.count()
        previstas = self.sliderPrevistas.value()
        self.barraProgreso.setValue(min(100, hechas * 100 // previstas))
        if hechas >= previstas:
            self.statusbar.showMessage("¡Rodaje completo!")

    def contarCaracteres(self):
        self.lblCaracteres.setText(f"{len(self.textNotas.toPlainText())} caracteres")

    def salir(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Salir")
        dlg.setText("¿Seguro que quieres salir?")
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if dlg.exec() == QMessageBox.StandardButton.Yes:
            self.close()


app = QApplication([])
app.setStyle("Fusion")
window = MainWindow()
app.exec()