import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from vstreamer import gui
from vstreamer.gui.list import DataMock


def window():
    app = QtWidgets.QApplication(sys.argv)

    video_dir_list_dialog = gui.list.VideoDirectoryListView()
    video_dir_list_dialog.show()

    # QtCore.QTimer.singleShot(1000, lambda: video_dir_list_dialog.set_data(DataMock.mock_data()))
    # window_controller = gui.MainWindowController()
    # main_window = gui.MainWindow(window_controller)
    # main_window.show()

    # run after main loop has started
    # QtCore.QTimer.singleShot(0, window_controller.connect_to_server)

    app.exec_()


window()
