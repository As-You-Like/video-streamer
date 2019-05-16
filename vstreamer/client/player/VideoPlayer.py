import platform
import urllib.parse

import vlc
from PySide2 import QtCore, QtWidgets, QtMultimediaWidgets

from vstreamer.client.player import VideoPlayerBar


class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.remote_host = None
        self.port = None

        self.layout = QtWidgets.QVBoxLayout(self)
        self.player_widget = QtMultimediaWidgets.QVideoWidget(self)
        self.layout.addWidget(self.player_widget)
        self.setLayout(self.layout)
        self.bar = VideoPlayerBar(self)
        self.layout.addWidget(self.bar)
        self.setMinimumSize(500, 500)

        self._instance = vlc.Instance()
        self._player = self._instance.media_player_new()
        if platform.system() == "Linux":  # for Linux using the X Server
            self._player.set_xwindow(int(self.player_widget.winId()))
        elif platform.system() == "Windows":  # for Windows
            self._player.set_hwnd(int(self.player_widget.winId()))
        elif platform.system() == "Darwin":  # for MacOS
            self._player.set_nsobject(int(self.player_widget.winId()))
        else:
            raise RuntimeError("Multimedia is not supported on this platform")

        self._timer = QtCore.QTimer(self)
        self._timer.setSingleShot(False)
        self._timer.setInterval(100)
        self._timer.timeout.connect(self._update_ui)
        self._update_ui()
        self.bar.video_state.connect(self.handle_video_state_update)

    def handle_video_state_update(self):
        if self._player.is_playing():
            self._player.set_pause(1)
            self.bar.set_playing(False)
        else:
            self._player.set_pause(0)
            self.bar.set_playing(True)

    def set_remote_host(self, remote_host, port):
        self.remote_host = remote_host
        self.port = port

    def play_video(self, video_file_entry):
        encoded = urllib.parse.quote(video_file_entry.path)
        url = "rtsp://%s:%d%s" % (self.remote_host, self.port, encoded)
        media = self._instance.media_new(url)
        media.parse()
        self._player.set_media(media)
        self._player.play()
        self.bar.set_playing(True)
        self._timer.start()

    def _update_ui(self):
        curr_time = self._player.get_time()
        full_length = self._player.get_length()
        if curr_time == full_length:
            self._timer.stop()
            self.bar.set_playing(False)
        self.bar.set_current_video_time(curr_time, full_length)
