from collections import OrderedDict

from vstreamer_utils.model import FileEntry, DirectoryInfo


class FileEntryVM:
    def __init__(self, filename, is_video, properties=None):
        super().__init__()
        if properties is None:
            properties = OrderedDict()
        self.filename = filename
        self.is_video = is_video
        self.properties = properties

    @staticmethod
    def from_file_entry(dir_info: DirectoryInfo):
        return list(map(lambda file_entry:
                        FileEntryVM(file_entry.filename, file_entry.is_video),
                        dir_info.entries))

    @staticmethod
    def mock_data():
        return [
            FileEntryVM("testowy folder 1", False, dict(
                prop1="test1",
                prop2="test2"
            )),
            FileEntryVM("testowy folder 2", False),
            FileEntryVM("testowy video 1", True,dict(last="test"))
        ]
