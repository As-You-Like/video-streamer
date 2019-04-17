from PySide2 import QtCore
from vstreamer_utils import libraries


class VideoStreamerServerApplication(QtCore.QCoreApplication):
    def __init__(self, argv):
        super().__init__(argv)
        libraries.init_libraries()
        self.setApplicationName("video_streamer_server")