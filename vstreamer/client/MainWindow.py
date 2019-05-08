from PySide2 import QtWidgets, QtCore
from vstreamer import client
import vstreamer_utils


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.controller.view = self
        vstreamer_utils.load_ui("MainWindow.ui", self)

