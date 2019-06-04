import copy
import pathlib

import vstreamer_utils
from vstreamer_utils import model


class DirectoryInfo:
    def __init__(self, path, directory_root):
        path = pathlib.Path(path)
        directory_root = pathlib.Path(directory_root)
        if not path.is_dir():
            raise ValueError("'%s' is not a directory" % str(path))
        self.name = str(path.name)
        self.path = "/" + str(path.relative_to(directory_root))

        def key(file_entry):
            return file_entry.is_video(), file_entry.filename

        self.entries = sorted([model.FileEntry(x, directory_root) for x in path.iterdir()
                               if x.is_dir() or vstreamer_utils.is_video_file(x)], key=key)
        if path != directory_root:
            backdir = model.FileEntry(path.parent, directory_root)
            backdir.filename = ".."
            self.entries.insert(0, backdir)

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, key):
        return self.entries[key]

    def light_copy(self):
        light = copy.copy(self)
        light.entries = list(map(lambda e: e.light_copy(), self.entries))
        return light

