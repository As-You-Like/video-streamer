import sys
from vstreamer import application, client
from vstreamer.client import list, player
from vstreamer_utils.model import DirectoryInfo
DEBUG = True


def main():
    app = application.VideoStreamerApplication(sys.argv)

    dir_view = client.list.DirectoryInfoView()
    if DEBUG:
        dir_view.set_entries(list.FileEntryVM.mock_data())
    else:
        dir_view.set_entries(list.FileEntryVM.from_file_entry(DirectoryInfo("/home/tom/Videos", "/home/tom")))
    dir_view.show()

    video_player = player.VideoPlayer()
    video_player.set_remote_host("localhost", 5656)
    class Dummy:
        def __init__(self):
            self.path = None
    dummy = Dummy()
    dummy.path = "/film.mp4"
    video_player.play_video(dummy)
    video_player.show()

    main_window_controller = client.MainWindowController()
    main_window = client.MainWindow(main_window_controller)
    #QtCore.QTimer.singleShot(0, main_window_controller.connect_to_server)
    main_window.show()

    app.exec_()


if __name__ == "__main__":
    sys.exit(main())
