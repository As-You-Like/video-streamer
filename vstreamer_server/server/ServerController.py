from PySide2 import QtCore
from vstreamer_server import server, config
from vstreamer_utils import model


class ServerController(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.configuration = config.Configuration(config.get_config_directory(QtCore.QCoreApplication.applicationName()))
        self.directory_tree = model.DirectoryTree(self.configuration.config.base_directory)
        self.communication_server = server.CommunicationServer(self.configuration.config.starting_port,
                                                               self.directory_tree, self)
        self.video_server = server.VideoServer(self.configuration.config.starting_port + 1,
                                               self.directory_tree, self)

    def start(self):
        self.communication_server.start()
        self.video_server.start()

    def quit(self):
        self.configuration.write_config()
        QtCore.QCoreApplication.quit()
