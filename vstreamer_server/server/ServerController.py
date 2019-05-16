from PySide2 import QtCore
from vstreamer_server import server, config, communication
from vstreamer_utils import model


class ServerController(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        QtCore.QCoreApplication.instance().aboutToQuit.connect(self._on_application_quit)
        self.error_handler = communication.ErrorHandler()
        try:
            app_name = QtCore.QCoreApplication.applicationName()
            self.configuration = config.Configuration(config.get_config_directory(app_name))
            self.configuration.write_config()

            self.directory_tree = model.DirectoryTree(self.configuration.config.base_directory)
            self.communication_server = server.CommunicationServer(self.configuration.config.starting_port,
                                                                   self.directory_tree, self)
            self.video_server = server.VideoServer(self.configuration.config.starting_port + 1,
                                                   self.directory_tree, self)
        except Exception as exc:
            self.error_handler.handle_exception(exc)
            return
        self.communication_server.error_occurred.connect(self.error_handler.handle_error)

    def start(self):
        try:
            self.communication_server.start()
            self.video_server.start()
        except Exception as exc:
            self.error_handler.handle_exception(exc)

    def _on_application_quit(self):
        try:
            self.configuration.write_config()
            self.directory_tree.store_info()
        except Exception as exc:
            self.error_handler.handle_exception(exc)
