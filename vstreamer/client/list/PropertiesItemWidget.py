from PySide2 import QtWidgets, QtCore

import vstreamer_utils


class PropertiesItemWidget(QtWidgets.QWidget):
    FIXED_SIZE = QtCore.QSize(120, 140)

    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("PropertiesItemWidget.ui", self)
