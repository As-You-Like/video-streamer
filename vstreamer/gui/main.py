import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from vstreamer import gui, client
from vstreamer.gui.list.FileEntryVM import FileEntryVM
from vstreamer_utils import model
from vstreamer_utils.model import DirectoryInfo

DEBUG = True

def window():
    app = client.VideoStreamerApplication(sys.argv)

    dir_view = gui.list.DirectoryInfoView()
    if DEBUG:
        dir_view.set_entries(FileEntryVM.mock_data())
    else:
        dir_view.set_entries(
            FileEntryVM.from_file_entry(DirectoryInfo("/home/tom/Videos", "/home/tom"))
        )
    dir_view.show()

    # QtCore.QTimer.singleShot(1000, lambda: video_dir_list_dialog.set_data(DataMock.mock_data()))
    # window_controller = gui.MainWindowController()
    # main_window = gui.MainWindow(window_controller)
    # main_window.show()

    # run after main loop has started
    # QtCore.QTimer.singleShot(0, window_controller.connect_to_server)

    app.exec_()


window()


