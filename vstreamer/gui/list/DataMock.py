from vstreamer_utils.model import FileEntry


def mock_data():
    return [
        ("A", hex_to_rgb("#000000")),
        ("B", hex_to_rgb("#123432")),
        ("C", hex_to_rgb("#ffffff")),
        ("D", hex_to_rgb("#888888"))
    ]

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
