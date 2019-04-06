import pathlib
from vstreamer_utils import model


class DirectoryTree:
    def __init__(self, directory_root):
        directory_root = pathlib.Path(directory_root).absolute()
        if not directory_root.is_dir():
            raise ValueError("'%s' is not a directory" % str(directory_root))
        self.directories = {}

        self.directories["/"] = model.DirectoryInfo(directory_root, directory_root)
        for file in directory_root.glob("**/*"):
            if file.is_dir():
                relative = "/" + str(file.relative_to(directory_root))
                self.directories[relative] = model.DirectoryInfo(file, directory_root)
        print(self.directories)
