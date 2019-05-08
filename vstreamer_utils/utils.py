import pathlib
import pkg_resources
import inspect
from PySide2 import QtUiTools


# not imported
from vstreamer.client.list import DirectoryInfoView
from vstreamer.client.player import VideoPlayer


class _SelfUILoader(QtUiTools.QUiLoader):
    def __init__(self, widget):
        QtUiTools.QUiLoader.__init__(self, widget)
        self.widget = widget
        self.customWidgets = dict()
        self.customWidgets[VideoPlayer.__name__] = VideoPlayer
        self.customWidgets[DirectoryInfoView.__name__] = DirectoryInfoView

    def createWidget(self, class_name, parent=None, name=''):
        if parent is None and self.widget:
            return self.widget
        else:
            if class_name in self.availableWidgets():
                widget = QtUiTools.QUiLoader.createWidget(self, class_name, parent, name)
            else:
                try:
                    widget = self.customWidgets[class_name](parent=parent)
                except (TypeError, KeyError) as e:
                    raise Exception(
                        'No custom widget ' + class_name + ' found in customWidgets param of UiLoader __init__.')
            if self.widget:
                setattr(self.widget, name, widget)
            return widget

SERVER_PORT = 5655
SERVER_VIDEO_PORT = 5656


def is_video_file(file):
    file = pathlib.Path(file)
    return file.is_file() and file.suffix in (".mkv", ".mp4")


def load_ui(file, widget):
    frame = inspect.stack()[1]  # get stack frame of the caller
    module_name = inspect.getmodule(frame[0]).__name__  # caller module name
    ui_file_path = pkg_resources.resource_filename(module_name, file)
    _SelfUILoader(widget).load(str(ui_file_path))


def size_to_string(size, suffix="B"):
    if size < 10240:
        return "%d %s" % (size, suffix)
    size >>= 10
    if size < 10240:
        return "%d Ki%s" % (size, suffix)
    size >>= 10
    if size < 10240:
        return "%d Mi%s" % (size, suffix)
    size >>= 10
    return "%d Gi%s" % (size, suffix)
