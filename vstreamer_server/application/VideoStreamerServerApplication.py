import logging
import signal
from PySide2 import QtCore
import vstreamer_utils
from vstreamer_utils import libraries


class VideoStreamerServerApplication(QtCore.QCoreApplication):
    def __init__(self, argv):
        super().__init__(argv)
        libraries.init_libraries()
        self.setApplicationName("video_streamer_server")
        self.logger = vstreamer_utils.make_logger()
        vstreamer_utils.set_signal_handlers(self)

        self.logger.info("Started server application")

