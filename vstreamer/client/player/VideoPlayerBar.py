from PySide2 import QtWidgets, QtGui, QtCore

import vstreamer_utils


class VideoPlayerBar(QtWidgets.QWidget):
    video_state = QtCore.Signal()
    video_set_point_in_time = QtCore.Signal(int)
    video_set_volume = QtCore.Signal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("VideoPlayerBar.ui", self)
        self.set_current_video_time(0, 0)
        self.play_pause_toolbutton.clicked.connect(self.video_state)
        self.drag_time = 0
        self.slider.sliderMoved.connect(self._handle_slider_drag_value)
        self.forward_toolbutton.setIcon(QtGui.QIcon(":/icons/FastForward.png"))
        self.rewind_toolbutton.setIcon(QtGui.QIcon(":/icons/FastRewind.png"))
        self.rewind_toolbutton.clicked.connect(self._handle_rewind)
        self.forward_toolbutton.clicked.connect(self._handle_forward)
        self.volume_toolbutton.clicked.connect(self._handle_volume_click)
        self._old_volume = -1
        self.volume_slider.sliderMoved.connect(self.video_set_volume)

    def _handle_volume_click(self):
        if self.volume_slider.value() == 0:
            if self._old_volume != -1:
                self.video_set_volume.emit(self._old_volume)
                self._old_volume = -1
                return
            else:
                return
        self._old_volume = self.volume_slider.value()
        self.video_set_volume.emit(0)
    def _handle_rewind(self):
        cur_val = self.slider.value()
        max_val = self.slider.maximum()
        next_val = cur_val - 0.1 * max_val
        if next_val < 0:
            next_val = 0
        self._handle_slider_drag_value(next_val)

    def _handle_forward(self):
        cur_val = self.slider.value()
        max_val = self.slider.maximum()
        next_val = cur_val + 0.1 * max_val
        if next_val > max_val:
            next_val = max_val
        self._handle_slider_drag_value(next_val)

    def _handle_slider_drag_value(self, value):
        print("slider drag value: " + str(value))
        self.drag_time = value


    def set_current_video_time(self, current_time_ms, total_time_ms):
        self.length_label.setText(
            vstreamer_utils.utils.format_time(
                current_time_ms) + "/" + vstreamer_utils.utils.format_time(total_time_ms))
        self.slider.setRange(0, total_time_ms)
        if not self.slider.isSliderDown():
            self.slider.setValue(current_time_ms)

    def set_playing(self, playing):
        if playing:
            self.play_pause_toolbutton.setIcon(QtGui.QIcon(":/icons/Pause.png"))
        else:
            self.play_pause_toolbutton.setIcon(QtGui.QIcon(":/icons/Play.png"))

    def set_volume(self, volume):
        self.volume_slider.setRange(0, 99)
        self.volume_slider.setValue(volume)
        if volume == 0:
            self.volume_toolbutton.setIcon(QtGui.QIcon(":/icons/VolumeOff.png"))
        else:
            self.volume_toolbutton.setIcon(QtGui.QIcon(":/icons/VolumeDown.png"))
