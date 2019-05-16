import logging
import signal
from PySide2 import QtCore
from vstreamer_utils import libraries


class VideoStreamerServerApplication(QtCore.QCoreApplication):
    def __init__(self, argv):
        super().__init__(argv)
        libraries.init_libraries()
        self.setApplicationName("video_streamer_server")

        self.logger = self._make_logger()
        self.logger.info("Started server application")
        self._set_signal_handlers()

    def _make_logger(self):
        logging.basicConfig(datefmt="%Y.%m.%d %H:%M:%S", format="[%(asctime)s] %(name)s[%(levelname)s]: %(message)s")
        app_name = QtCore.QCoreApplication.applicationName()
        logger = logging.getLogger(app_name)
        logger.setLevel(logging.INFO)
        logger = logging.getLogger(self.applicationName())
        return logger

    def _set_signal_handlers(self):
        def handle(signum, frame):
            QtCore.QCoreApplication.quit()

        signal_timer = QtCore.QTimer(self)
        signal_timer.start(50)
        signal_timer.timeout.connect(lambda: None)

        signal.signal(signal.SIGINT, handle)
        signal.signal(signal.SIGTERM, handle)
