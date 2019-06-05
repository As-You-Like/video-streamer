from PySide2 import QtCore, QtWidgets
import vstreamer_utils
from vstreamer import directories
from vstreamer.client import login
from vstreamer.client.login import LoginDialog
from vstreamer_utils.networking import CommunicationService


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("MainWindow.ui", self)
        QtCore.QCoreApplication.instance().aboutToQuit.connect(self._on_application_quit)
        self.server = None
        self.communication_socket = None
        self.response_handler = None
        self.communication_service = None
        self.directory_service = None

    def connect_to_server(self):
        login_dialog = LoginDialog()
        if login_dialog.exec_() == QtWidgets.QDialog.DialogCode.Accepted:
            self.server = login_dialog.server
            self.video_player.set_remote_host(self.server, 5656)
        else:
            QtWidgets.QApplication.quit()
            return

        connect_dialog = login.ConnectDialog(self.server)
        connect_dialog.connect_to_server()
        if connect_dialog.exec_() == QtWidgets.QDialog.DialogCode.Accepted:
            self.communication_socket = connect_dialog.socket
            self._initialize_communication_socket()
        else:
            QtWidgets.QApplication.quit()
            return
        self.show()

    def _initialize_communication_socket(self):
        self.communication_socket.setParent(self)
        self.communication_service = CommunicationService(self.communication_socket, self)

        self.directory_service = directories.DirectoryService(self.communication_service, self)
        self.directory_service.directories_ready.connect(self._handle_directories_ready)
        self.directory_service.additional_properties_ready.connect(self._handle_additional_properties_ready)

        self.directory_info_view.play_requested.connect(self.video_player.play_video)
        self.directory_info_view.directory_requested.connect(
            lambda entry: self.directory_service.get_directory_info(entry.path))

        self.directory_service.get_directory_info()

    def _handle_directories_ready(self, directory_info):
        self.directory_info_view.set_entries(directory_info)
        for file in directory_info.entries:
            if file.filename != "..":
                self.directory_service.get_additional_info(file.path)

    def _handle_additional_properties_ready(self, filename, additional_properties):
        self.directory_info_view.set_additional_properties(filename, additional_properties)

    def _on_application_quit(self):
        self.communication_service.socket.disconnectFromHost()
        vstreamer_utils.log_info("Client is closing")
