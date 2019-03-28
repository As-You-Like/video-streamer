from video_streamer_server import server
import gi
gi.require_version("Gst", "1.0")
from gi.repository import GLib, Gst


def main():
    Gst.init(None)
    Gst.debug_set_active(True)
    Gst.debug_set_default_threshold(3)
    loop = GLib.MainLoop()

    video_server = server.VideoServer(4000, "/home/artur")
    video_server.add_media("/home/artur/film.mkv")
    video_server.add_media("/home/artur/film.mp4")

    video_server.start()
    loop.run()
    return 0


if __name__ == "__main__":
    exit(main())
