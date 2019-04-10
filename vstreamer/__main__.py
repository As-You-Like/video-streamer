import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from vstreamer import gui, client
from vstreamer.gui import list
from vstreamer_utils import model
from vstreamer_utils.model import DirectoryInfo
DEBUG = True


def main():
    app = client.VideoStreamerApplication(sys.argv)

    dir_view = gui.list.DirectoryInfoView()
    if DEBUG:
        dir_view.set_entries(list.FileEntryVM.mock_data())
    else:
        dir_view.set_entries(list.FileEntryVM.from_file_entry(DirectoryInfo("/home/tom/Videos", "/home/tom")))

    main_window_controller = gui.MainWindowController()
    main_window = gui.MainWindow(main_window_controller)
    QtCore.QTimer.singleShot(0, main_window_controller.connect_to_server)

    dir_view.show()
    app.exec_()


if __name__ == "__main__":
    exit(main())
