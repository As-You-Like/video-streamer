from PySide2 import QtWidgets

import vstreamer_utils
from vstreamer.client import login
from vstreamer.client.list import FileEntryVM
from vstreamer.client.login import LoginDialog
from vstreamer_utils.networking import CommunicationService, DirectoryInfoResponse, \
    AdditionalEntryPropertiesResponse, ErrorResponse

DEBUG = False


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("MainWindow.ui", self)

        if DEBUG:
            self.directory_info_view.set_entries(FileEntryVM.mock_data())
        # else:
        # self.directory_info_view.set_entries(
        #     FileEntryVM.from_file_entry(DirectoryInfo("/home/tom/Videos", "/home/tom")))

        self.server = None
        self.communication_socket = None
        self.response_handler = None
        self.communication_service = None
        self.directory_service = None
        self.directory_info_view.play_requested.connect(self.video_player.play_video)

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
        self.directory_info_view.initialize_directory_service(self.communication_service)
    def _receive(self, response):
        if isinstance(response, DirectoryInfoResponse):
            self.receive_directory_info(response)
        elif isinstance(response, AdditionalEntryPropertiesResponse):
            self.receive_additional_info(response)
        elif isinstance(response, ErrorResponse):
            self.receive_error(response)
