from PySide2 import QtWidgets
from vstreamer.gui import login
import vstreamer_utils


class ConnectDialog(QtWidgets.QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.controller.view = self

    def end_with_error(self, msg):
        QtWidgets.QMessageBox.critical(self, "Video Streamer",
                                       "Could not connect to remote server - " + msg)
        self.reject()

