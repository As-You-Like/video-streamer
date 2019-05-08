from PySide2 import QtWidgets, QtCore

import vstreamer_utils
from vstreamer.client.list import FileEntryVM, PropertiesItemWidget


class PropertiesWidget(QtWidgets.QGroupBox):
    FIXED_SIZE = QtCore.QSize(120, 140)

    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("PropertiesWidget.ui", self)

    def setup_properties(self, fileEntryVM: FileEntryVM):
        # todo clear layout before adding new widget
        # self.properties_widget_layout.remove
        for key, value in fileEntryVM.properties.items():
            line = PropertiesItemWidget()
            line.left_label.setText(key)
            line.right_label.setText(value)
            self.main_layout.addWidget(line)
        # todo not working
        # self.properties_widget_layout.addStretch(1)