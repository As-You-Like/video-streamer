from PySide2 import QtCore
from PySide2.QtCore import QObject

from vstreamer_utils.model import DirectoryInfo, AdditionalEntryProperties
from vstreamer_utils.networking import DirectoryInfoResponse


class ResponseHandler(QObject):
    directories_ready = QtCore.Signal(DirectoryInfo)
    additional_properties_ready = QtCore.Signal(str, AdditionalEntryProperties)

    def __init__(self, communication_service, parent: QObject = None) -> None:
        super().__init__(parent)
        self.communication_service = communication_service
        self.communication_service.received_response.connect(self.handle_response)

    def handle_response(self, response):
        if isinstance(response, DirectoryInfoResponse):
            self.directories_ready.emit(response.directory_info)
        elif isinstance(response, AdditionalEntryProperties):
            self.additional_properties_ready.emit(response.filepath,
                                                             response.additional_properties)
        # ErrorHandler.Error.UNKNOWN_RESPONSE
