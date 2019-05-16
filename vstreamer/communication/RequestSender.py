from PySide2.QtCore import QObject
from vstreamer_utils.networking import DirectoryInfoRequest, AdditionalEntryPropertiesRequest


class RequestSender(QObject):
    def __init__(self, communication_service, parent):
        super().__init__(parent)
        self.communication_service = communication_service

    def get_directory_info(self, path="/"):
        self.communication_service.write_message(DirectoryInfoRequest(path))

    def get_additional_info(self, filepath):
        self.communication_service.write_message(AdditionalEntryPropertiesRequest(filepath))
