import sys
from PySide2 import QtWidgets
from vstreamer.gui.login import *


def window():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginDialog(LoginController())
    # window.setGeometry(50,50,500,500)
    # window.setWindowTitle("Video streamer client")
    window.show()
    app.exec_()


window()