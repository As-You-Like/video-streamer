import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from vstreamer import gui


def window():
    app = QtWidgets.QApplication(sys.argv)

    window_controller = gui.MainWindowController()
    main_window = gui.MainWindow(window_controller)

    # run after main loop has started
    QtCore.QTimer.singleShot(0, window_controller.connect_to_server)

    app.exec_()


window()