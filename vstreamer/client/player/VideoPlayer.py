import this

from PySide2 import QtCore, QtWidgets, QtMultimediaWidgets
import platform
import vlc


class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.remote_host = None
        self.port = None

        self.layout = QtWidgets.QHBoxLayout(self)
        self.player_widget = QtMultimediaWidgets.QVideoWidget(self)
        self.layout.addWidget(self.player_widget)
        self.setLayout(self.layout)
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
        self._timer.setSingleShot(True)
        self._timer.setInterval(100)
        self._timer.timeout.connect(self._update_ui)
        self._update_ui()

    def set_remote_host(self, remote_host, port):
        self.remote_host = remote_host
        self.port = port

    def play_video(self, video_file_entry):
        url = "rtsp://%s:%d/%s" % (self.remote_host, self.port, video_file_entry.path.replace(' ', '_'))
        media = self._instance.media_new(url)
        media.parse()
        self._player.set_media(media)
        self._player.play()

    def _update_ui(self):
        # TODO
        pass
