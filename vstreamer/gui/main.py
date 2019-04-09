import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from vstreamer import gui


def window():
    app = QtWidgets.QApplication(sys.argv)

    video_dir_list_dialog = gui.list.VideoDirectoryListView()
    video_dir_list_dialog.show()
    # window_controller = gui.MainWindowController()
    # main_window = gui.MainWindow(window_controller)
    # main_window.show()

    # run after main loop has started
    # QtCore.QTimer.singleShot(0, window_controller.connect_to_server)

    app.exec_()


window()







