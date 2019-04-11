from vstreamer_utils import model


class AdditionalEntryProperties:
    def __init__(self, tile=None, description=None, image=None):
        self.title = tile
        self.description = description
        self.image = image

    @staticmethod
    def from_file_entry(file_entry):
        return AdditionalEntryProperties(file_entry.filename, file_entry.description, file_entry.image)