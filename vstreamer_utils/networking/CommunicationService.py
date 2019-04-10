import pickle
import struct
from PySide2 import QtCore, QtNetwork
from vstreamer_utils import networking


class CommunicationService(QtCore.QObject):
    received_request = QtCore.Signal(networking.Request)
    received_response = QtCore.Signal(networking.Response)
    error_occurred = QtCore.Signal(str)

    def __init__(self, socket, parent=None):
        super().__init__(parent)
        if socket.state() != QtNetwork.QAbstractSocket.SocketState.ConnectedState:
            raise ValueError("socket is not connected")

        self.socket = socket
        self.data = bytearray()
        self.size_left = 0

        self._connect_signals()

    def write_message(self, message):
        if not isinstance(message, networking.Request) and not isinstance(message, networking.Response):
            raise ValueError("message is not a Request or a Response")
        data = pickle.dumps(message, pickle.DEFAULT_PROTOCOL, fix_imports=False)
        data_length = len(data)
        data = struct.pack("!Q", data_length) + data
        self.socket.write(data)

    def _connect_signals(self):
        self.socket.disconnected.connect(self._handle_disconnected)
        self.socket.error.connect(self._handle_error)
        self.socket.readyRead.connect(self._handle_data_ready)

    def _handle_disconnected(self):
        self.socket.setErrorString("Connection lost")
        self._handle_error()

    def _handle_error(self):
        CommunicationService.error_occurred.emit(self.socket.errorString())
        pass

    def _handle_data_ready(self):
        # TODO
        pass

