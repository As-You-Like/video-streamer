from PySide2 import QtWidgets
import pkg_resources
from video_streamer.gui import SelfUILoader


class LoginDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file_path = pkg_resources.resource_filename(__name__, "logindialog.ui")
        SelfUILoader(self).load(str(ui_file_path))
