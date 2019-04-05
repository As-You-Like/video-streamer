from PySide2 import QtWidgets
import vstreamer_utils


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("LoginDialog.ui", self)
