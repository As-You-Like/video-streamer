from PySide2 import QtWidgets

import vstreamer_utils
from vstreamer_utils.utils import format_time


class VideoPlayerBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("VideoPlayerBar.ui", self)
        self.set_current_video_time(0, 0)

    def set_current_video_time(self, current_time_ms, total_time_ms):
        self.length_label(format_time(current_time_ms) + "/" + format_time(total_time_ms))
        # todo slider
