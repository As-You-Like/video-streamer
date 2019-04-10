from PySide2 import QtNetwork
from vstreamer_server import server
import vstreamer_utils
import gi
gi.require_version("Gst", "1.0")
from gi.repository import GLib, Gst


def main():
    Gst.init(None)
    Gst.debug_set_active(True)
    Gst.debug_set_default_threshold(3)

    loop = GLib.MainLoop()
    video_server = server.VideoServer(vstreamer_utils.SERVER_VIDEO_PORT, "/srv")
    communication_server = QtNetwork.QTcpServer()

    video_server.start()
    communication_server.listen(port=vstreamer_utils.SERVER_PORT)
    loop.run()
    return 0


if __name__ == "__main__":
    exit(main())
