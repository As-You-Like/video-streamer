from PySide2 import QtCore, QtNetwork
import vstreamer_utils


class ConnectDialogController(QtCore.QObject):
    def __init__(self, server, parent=None):
        super().__init__(parent)
        self.view = None
        self.server = server
        self.socket = None

    def connect_to_server(self):
        self.socket = QtNetwork.QTcpSocket()
        self.socket.connected.connect(self._handle_connected)
        self.socket.error.connect(self._handle_error)
        self.socket.connectToHost(self.server, vstreamer_utils.SERVER_PORT)

    def _disconnect_signals(self):
        self.socket.connected.disconnect()
        self.socket.error.disconnect()

    def _handle_connected(self):
        self._disconnect_signals()
        self.view.accept()

    def _handle_error(self, code):
        self._disconnect_signals()
        self.view.end_with_error(self.socket.errorString())
