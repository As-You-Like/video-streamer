import platform
import ctypes.util
import sys
import urllib.parse
import vlc
from PySide2 import QtCore, QtWidgets, QtMultimediaWidgets
import vstreamer_utils
from vstreamer.client.player import VideoPlayerBar

# set up vsnprintf
if platform.system() == "Windows":
    vsnprintf = ctypes.cdll.msvcrt.vspnrintf
else:
    libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
    vsnprintf = libc.vsnprintf
vsnprintf.restype = ctypes.c_int
vsnprintf.argtypes = (
    ctypes.c_char_p,
    ctypes.c_size_t,
    ctypes.c_char_p,
    ctypes.c_void_p,)


class VideoPlayer(QtWidgets.QWidget):
    error_occurred = QtCore.Signal(vstreamer_utils.Error)

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

        @vlc.CallbackDecorators.LogCb
        def log_callback(data, level, ctx, fmt, args):
            self._log_callback(level, fmt, args)
        self._callback = log_callback

        self._instance = vlc.Instance()
        self._instance.log_set(log_callback, None)
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
        self.bar.video_set_point_in_time.connect(self.handle_slider_change)

    def handle_slider_change(self, value):
        self._player.set_time(value)

    def handle_video_state_update(self):
        if self._player.is_playing():
            self._player.set_pause(1)
            self.bar.set_playing(False)
        else:
            self._player.set_pause(0)
            self.bar.set_playing(True)
            self._timer.stop()

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

    @staticmethod
    def _make_msg(fmt, args):
        buf_length = 2048
        msg = ctypes.create_string_buffer(buf_length)
        vsnprintf(msg, buf_length, fmt, args)
        return msg.value.decode("utf-8")

    def _log_callback(self, level, fmt, args):
        msg = VideoPlayer._make_msg(fmt, args)
        if level == vlc.LogLevel.WARNING:
            self.error_occurred.emit(vstreamer_utils.Error(msg, vstreamer_utils.ErrorLevel.WARNING))
        elif level == vlc.LogLevel.ERROR:
            self.error_occurred.emit(vstreamer_utils.Error(msg, vstreamer_utils.ErrorLevel.ERROR))
        elif level == vlc.LogLevel.NOTICE:
            vstreamer_utils.log_info(msg)
