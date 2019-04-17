import sys
from vstreamer_server import application, server
import gi
gi.require_version("Gst", "1.0")
from gi.repository import GLib, Gst


def main():
    Gst.init(None)
    Gst.debug_set_active(True)
    Gst.debug_set_default_threshold(3)
    loop = GLib.MainLoop()
    app = application.VideoStreamerServerApplication(sys.argv)
    server_controller = server.ServerController()

    server_controller.start()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
