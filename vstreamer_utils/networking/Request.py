

class Request:
    pass


class DirectoryInfoRequest(Request):
    def __init__(self, path):
        super().__init__()
        self.path = path
