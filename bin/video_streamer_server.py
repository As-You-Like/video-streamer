from vstreamer_server import server
from vstreamer_utils import model
import gi
gi.require_version("Gst", "1.0")
from gi.repository import GLib, Gst


def main():
    Gst.init(None)
    Gst.debug_set_active(True)
    Gst.debug_set_default_threshold(3)
    from vstreamer_utils import networking
    from vstreamer_utils import request
    comm = networking.CommunicationService(None)
    comm.write_message(request.Request())
    loop = GLib.MainLoop()
    video_server = server.VideoServer(4000, "/srv")

    video_server.start()
    loop.run()
    return 0


if __name__ == "__main__":
    exit(main())
