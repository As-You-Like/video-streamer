import vstreamer_utils
import collections
import pathlib
import abc
import time


class FileEntry(abc.ABC):
    def __new__(cls, file, directory_root):
        # if called from subclass call default implementation
        if cls is not FileEntry:
            return super().__new__(cls)

        # if called from FileEntry class return selected subclass
        if pathlib.Path(file).is_dir():
            return super().__new__(DirectoryEntry)
        return super().__new__(VideoFileEntry)

    def __init__(self, file, directory_root):
        file = pathlib.Path(file)
        directory_root = pathlib.Path(directory_root)
        stat = file.stat()

        self.filename = str(file.name)
        self.path = "/" + str(file.relative_to(directory_root))
        self.size = stat.st_size  # todo nice size
        self.creation_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_ctime))
        self.modification_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime))

        self.properties = collections.OrderedDict()
        self.properties["Filename"] = self.filename
        self.properties["Path"] = self.path
        self.properties["Size"] = str(self.size)
        self.properties["Creation Time"] = self.creation_time
        self.properties["Modification Time"] = self.modification_time

    @abc.abstractmethod
    def is_video(self):
        ...


class DirectoryEntry(FileEntry):
    def __init__(self, file, directory_root):
        super().__init__(file, directory_root)
        if not pathlib.Path(file).is_dir():
            raise ValueError("'%s' is not a directory" % str(file))
        # todo directory info

    def is_video(self):
        return False


class VideoFileEntry(FileEntry):
    def __init__(self, file, directory_root):
        super().__init__(file, directory_root)
        if not vstreamer_utils.is_video_file(file):
            raise ValueError("'%s' is not a video file" % str(file))
        # todo video info

    def is_video(self):
        return True
