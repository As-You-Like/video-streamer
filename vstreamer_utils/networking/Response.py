

class Response:
    pass


class DirectoryInfoResponse(Response):
    def __init__(self, directory_info):
        super().__init__()
        self.directory_info = directory_info
