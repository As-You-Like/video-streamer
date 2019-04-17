from PySide2 import QtCore, QtNetwork


class CommunicationServer(QtCore.QObject):
    def __init__(self, port, directory_tree, parent=None):
        super().__init__(parent)
        self.port = int(port)
        self.directory_tree = directory_tree
        # TODO

    def start(self):
        # TODO
        pass
