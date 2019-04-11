from PySide2 import QtWidgets, QtCore
import vstreamer_utils


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("LoginDialog.ui", self)
        self.server=None
        self.button.clicked.connect(self.on_click_ok)

    def on_click_ok(self):
        self.server = self.host_edit.text()
        self.accept()


