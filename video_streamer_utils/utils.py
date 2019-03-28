import pathlib


def is_video_file(file):
    file = pathlib.Path(file)
    return file.is_file() and file.suffix in (".mkv", ".mp4")
