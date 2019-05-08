from PySide2 import QtCore, QtNetwork
from vstreamer_server import server
from vstreamer_utils import networking


class CommunicationServer(QtCore.QObject):
    def __init__(self, port, directory_tree, parent=None):
        super().__init__(parent)
        self.port = int(port)
        self.directory_tree = directory_tree
        self.server = QtNetwork.QTcpServer(self)
        self.server.newConnection.connect(self._handle_new_connection)

    def start(self):
        self.server.listen(port=self.port)

    def _handle_new_connection(self):
        socket = self.server.nextPendingConnection()
        communication_service = networking.CommunicationService(socket, self)
        socket.setParent(communication_service)
        request_handler = server.RequestHandler(communication_service, communication_service)
