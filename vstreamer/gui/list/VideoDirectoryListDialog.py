from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QStringListModel

import vstreamer_utils


class VideoDirectoryListDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        vstreamer_utils.load_ui("video_list.ui", self)

        self.model = QStringListModel(self)
        self.model.setStringList(["sysopy","sa","super"])

        self.listView.setModel(self.model)

        self.addButton.clicked.connect(self.on_add_button_click)
        self.deleteButton.clicked.connect(self.on_delete_button_click)

    def on_add_button_click(self):
        rowCount = self.model.rowCount()
        self.model.insertRows(rowCount,1)
        index = self.model.index(rowCount)
        self.listView.setCurrentIndex(index)
        self.listView.edit(index)

    def on_delete_button_click(self):
        self.model.removeRow(self.listView.currentIndex().row())

