from PySide2 import QtCore, QtNetwork
from vstreamer_server import communication, server
import vstreamer_utils
from vstreamer_utils import networking


class CommunicationServer(QtCore.QObject):
    error_occurred = QtCore.Signal(vstreamer_utils.Error)

    def __init__(self, port, directory_tree, parent=None):
        super().__init__(parent)
        self.port = int(port)
        self.directory_tree = directory_tree
        self.server = QtNetwork.QTcpServer(self)

        self.server.newConnection.connect(self._handle_new_connection)
        self.server.acceptError.connect(self._handle_accept_error)

    def start(self):
        if not self.server.listen(port=self.port):
            raise RuntimeError("Could not start listening for connections on port: %d" % self.port)

    def _handle_accept_error(self):
        self.error_occurred.emit(vstreamer_utils.Error(self.server.errorString(), vstreamer_utils.ErrorLevel.ERROR))

    def _handle_new_connection(self):
        socket = self.server.nextPendingConnection()
        communication_service = networking.CommunicationService(socket, self)
        socket.setParent(communication_service)
        request_handler = communication.RequestHandler(communication_service, self.directory_tree, communication_service)

        request_handler.error_occured.connect(self.error_occurred)
        communication_service.error_occurred.connect(self.error_occurred)
        communication_service.disconnected.connect(self._handle_disconnected)

    def _handle_disconnected(self, socket):
        sender = self.sender()
        # todo log
        sender.deleteLater()
