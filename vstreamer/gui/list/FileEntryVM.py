from vstreamer_utils.model import FileEntry, DirectoryInfo


class FileEntryVM():
    def __init__(self, filename, is_video) -> None:
        super().__init__()
        self.filename = filename
        self.is_video = is_video

    @staticmethod
    def from_file_entry(dir_info: DirectoryInfo):
        return list(map(lambda file_entry:
                        FileEntryVM(file_entry.filename, file_entry.is_video),
                        dir_info.entries))
