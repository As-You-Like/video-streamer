from PySide2 import QtWidgets, QtGui, QtCore

import vstreamer_utils


class VideoPlayerBar(QtWidgets.QWidget):
    video_state = QtCore.Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("VideoPlayerBar.ui", self)
        self.set_current_video_time(0, 0)

    def set_current_video_time(self, current_time_ms, total_time_ms):
        self.length_label.setText(
            vstreamer_utils.utils.format_time(
                current_time_ms) + "/" + vstreamer_utils.utils.format_time(total_time_ms))
        self.slider.setRange(0, total_time_ms)
        self.slider.setValue(current_time_ms)

    def set_playing(self, playing):
        if playing:
            self.play_pause_toolbutton.setIcon(QtGui.QIcon(":/icons/Pause.png"))
        else:
            self.play_pause_toolbutton.setIcon(QtGui.QIcon(":/icons/Play.png"))
