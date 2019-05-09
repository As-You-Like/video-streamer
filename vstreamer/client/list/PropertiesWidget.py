from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QLabel

import vstreamer_utils


class PropertiesWidget(QtWidgets.QGroupBox):
    FIXED_SIZE = QtCore.QSize(120, 140)

    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("PropertiesWidget.ui", self)

    def set_properties(self, file_entry):
        self.clear()
        if file_entry is None:
            return

        self._add_lines_to_layout(self.properties_layout, file_entry.properties)
        self._add_lines_to_layout(self.other_properties_layout, file_entry.other_properties)
        self.title_label.setText(file_entry.filename)
        if len(file_entry.properties) > 0:
            self.properties_info_label.setText("Properties")
        if len(file_entry.other_properties) > 0:
            self.other_properties_info_label.setText("Other properties")

    def _add_lines_to_layout(self, layout, properties):
        for key, value in properties.items():
            left_label = QLabel(key + ":")
            right_label = QLabel(value)
            layout.addRow(left_label, right_label)

    def clear(self):
        self._clear_layout(self.properties_layout)
        self._clear_layout(self.other_properties_layout)
        self.properties_info_label.setText("")
        self.other_properties_info_label.setText("")
        self.title_label.setText("")

    def _clear_layout(self, layout):
        while layout.count() > 0:
            item = layout.takeAt(0)
            item.widget().deleteLater()
