import sys
from PySide2 import QtWidgets
from video_streamer.gui.login import *
def window():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginDialog()
    # window.setGeometry(50,50,500,500)
    # window.setWindowTitle("Video streamer client")
    window.show()
    app.exec_()


window()