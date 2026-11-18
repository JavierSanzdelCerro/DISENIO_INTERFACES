from iconos_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QStyle
from PyQt6.QtCore import QSize

# Iconos estándar más útiles (QStyle.StandardPixmap.SP_...):
#   Diálogos: SP_DialogSaveButton (guardar), SP_DialogOpenButton (abrir), SP_DialogCancelButton (cancelar),
#             SP_DialogApplyButton (aplicar), SP_DialogOkButton, SP_DialogCloseButton,
#             SP_DialogYesButton, SP_DialogNoButton, SP_DialogHelpButton, SP_DialogResetButton
#   Flechas:  SP_ArrowLeft, SP_ArrowRight, SP_ArrowUp, SP_ArrowDown, SP_ArrowBack, SP_ArrowForward
#   Avisos:   SP_MessageBoxWarning (aviso), SP_MessageBoxInformation, SP_MessageBoxCritical, SP_MessageBoxQuestion
#   Archivos: SP_FileIcon, SP_DirIcon, SP_DirOpenIcon, SP_FileDialogNewFolder, SP_TrashIcon (papelera)
#   Otros:    SP_BrowserReload, SP_BrowserStop, SP_MediaPlay, SP_MediaPause, SP_MediaStop, SP_ComputerIcon
#
# DOS formas de poner iconos:
#   1) Desde Designer (btnGuardarPng): propiedad icon -> eliges un .png e iconSize para el tamaño.
#      Solo admite imágenes propias (archivos) y depende de la ruta: pyuic6 escribe
#      QPixmap("icono_guardar.png"), que se busca en la carpeta desde la que ejecutas.
#      Si el .png no está, no da error: el botón sale sin icono.
#   2) Desde código (el resto de botones): iconos estándar QStyle.StandardPixmap.SP_...
#      Designer no los ofrece, solo se ponen así. No necesitan archivos: los trae el propio estilo.

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        estilo = self.style()  # el estilo actual trae sus propios iconos
        self.btnGuardar.setIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton))
        self.btnAbrir.setIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_DialogOpenButton))
        self.btnAplicar.setIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton))
        self.btnCancelar.setIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_DialogCancelButton))
        self.btnAnterior.setIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_ArrowLeft))
        self.btnSiguiente.setIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_ArrowRight))
        self.btnBorrar.setIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_TrashIcon))
        self.btnAviso.setIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_MessageBoxWarning))

        # Tamaño del icono en píxeles (ancho, alto). Por defecto es pequeño (16x16)
        self.btnGuardar.setIconSize(QSize(32, 32))
        self.btnAviso.setIconSize(QSize(48, 48))

        # También sirve para el icono de la ventana
        self.setWindowIcon(estilo.standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))

app = QApplication([])
window = MainWindow()
app.exec()
