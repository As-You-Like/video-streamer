from vstreamer_utils.model import FileEntry, DirectoryInfo


class FileEntryVM:
    def __init__(self, filename, is_video):
        super().__init__()
        self.filename = filename
        self.is_video = is_video

    @staticmethod
    def from_file_entry(dir_info: DirectoryInfo):
        return list(map(lambda file_entry:
                        FileEntryVM(file_entry.filename, file_entry.is_video),
                        dir_info.entries))

    @staticmethod
    def mock_data():
        return [
            FileEntryVM("testowy folder 1", False),
            FileEntryVM("testowy folder 2", False),
            FileEntryVM("testowy video 1", True)
        ]

