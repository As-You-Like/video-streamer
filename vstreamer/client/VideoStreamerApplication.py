from PySide2 import QtCore, QtWidgets, QtGui
import pkg_resources


class VideoStreamerApplication(QtWidgets.QApplication):
    def __init__(self, args):
        super().__init__(args)
        rcc_path = str(pkg_resources.resource_filename("vstreamer", "resources/resources.rcc"))
        QtCore.QResource.registerResource(rcc_path)
        self.setWindowIcon(QtGui.QIcon(":/icons/Avatar.png"))
