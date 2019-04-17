from PySide2 import QtCore
from vstreamer_utils import networking


class RequestHandler(QtCore.QObject):
    def __init__(self, communication_service, parent=None):
        super().__init__(parent)
        self.communication_service = communication_service
        # TODO
