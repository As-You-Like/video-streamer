from PySide2 import QtCore


class LoginDialogController(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.view = None
        self.server = None

    def accept_server(self):
        self.server = self.view.serverAddressEditText.toPlainText()
        self.view.accept()
