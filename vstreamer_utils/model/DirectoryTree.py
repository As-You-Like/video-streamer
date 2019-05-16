import pathlib
from vstreamer_utils import model


class DirectoryTree:
    def __init__(self, directory_root):
        self.directory_root = pathlib.Path(directory_root).absolute()
        self.directories = {}
        if not self.directory_root.is_dir():
            raise ValueError("'%s' is not a directory" % str(self.directory_root))

        self.directories["/"] = model.DirectoryInfo(self.directory_root, self.directory_root)
        for file in self.directory_root.glob("**/*"):
            if file.is_dir():
                relative = "/" + str(file.relative_to(self.directory_root))
                self.directories[relative] = model.DirectoryInfo(file, self.directory_root)

    def store_info(self):
        pass
