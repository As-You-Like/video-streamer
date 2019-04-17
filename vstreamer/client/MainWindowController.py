from PySide2 import QtWidgets, QtCore
from vstreamer.client import login


class MainWindowController(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.view = None
        self.server = None
        self.communication_socket = None

    def connect_to_server(self):
        login_dialog = login.LoginDialog()
        if login_dialog.exec_() == QtWidgets.QDialog.DialogCode.Accepted:
            self.server = login_dialog.server
        else:
            QtWidgets.QApplication.quit()
            return

        connect_dialog = login.ConnectDialog(self.server)
        connect_dialog.connect_to_server()
        if connect_dialog.exec_() == QtWidgets.QDialog.DialogCode.Accepted:
            self.communication_socket = connect_dialog.socket
            self._initialize_communication_socket()
        else:
            QtWidgets.QApplication.quit()
            return
        self.view.show()

    def _initialize_communication_socket(self):
        self.communication_socket.setParent(self)
        # TODO: error handlers etc.


