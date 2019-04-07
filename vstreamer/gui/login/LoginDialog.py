from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import SIGNAL, QObject
import vstreamer_utils


def func():
    print("test func called")


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        controller.set_view(self)
        vstreamer_utils.load_ui("LoginDialog.ui", self)
        self.button.clicked.connect(lambda: self.controller.select_server(
            self.serverAddressEditText.toPlainText()
        ))
