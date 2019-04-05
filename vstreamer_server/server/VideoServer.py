import vstreamer_utils
import pathlib
import gi
gi.require_version("GstRtspServer", "1.0")
from gi.repository import GstRtspServer


class VideoServer:
    def __init__(self, port, directory_root):
        self.port = int(port)
        self.directory_root = pathlib.Path(directory_root)
        self.server = GstRtspServer.RTSPServer.new()
        self.server.set_service(str(self.port))

    def add_media(self, file):
        file = pathlib.Path(file)
        if not vstreamer_utils.is_video_file(file):
            raise ValueError("'%s' is not a valid video file" % str(file))
        if not file.is_absolute():
            raise ValueError("'%s' is not an absolute path" % str(file))

        demuxer = VideoServer._corresponding_demuxer(file)
        server_subpath = "/" + str(file.relative_to(self.directory_root))
        pipeline = "filesrc location=%s ! %s name=dmux " \
                   "dmux.video_0 ! queue ! rtph264pay name=pay0 pt=96 " \
                   "dmux.audio_0 ! queue ! rtpmp4apay name=pay1" % (file, demuxer)
        factory = GstRtspServer.RTSPMediaFactory()
        factory.set_launch(pipeline)
        factory.set_shared(True)
        self.server.get_mount_points().add_factory(server_subpath, factory)

    def start(self, context=None):
        self.server.attach(context)

    @staticmethod
    def _corresponding_demuxer(file):
        if file.suffix == ".mkv":
            return "matroskademux"
        if file.suffix == ".mp4":
            return "qtdemux"
        raise ValueError("'%s' is not a valid container" % str(file))
