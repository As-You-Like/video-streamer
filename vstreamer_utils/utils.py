import pathlib
import pkg_resources
import inspect
from PySide2 import QtUiTools


# not imported
class _SelfUILoader(QtUiTools.QUiLoader):
    def __init__(self, widget):
        QtUiTools.QUiLoader.__init__(self, widget)
        self.widget = widget

    def createWidget(self, class_name, parent=None, name=''):
        if parent is None and self.widget:
            return self.widget
        else:
            widget = QtUiTools.QUiLoader.createWidget(self, class_name, parent, name)
            if self.widget:
                setattr(self.widget, name, widget)
            return widget


def is_video_file(file):
    file = pathlib.Path(file)
    return file.is_file() and file.suffix in (".mkv", ".mp4")


def load_ui(file, widget):
    frame = inspect.stack()[1]  # get stack frame of the caller
    module_name = inspect.getmodule(frame[0]).__name__  # caller module name
    ui_file_path = pkg_resources.resource_filename(module_name, file)
    _SelfUILoader(widget).load(str(ui_file_path))
