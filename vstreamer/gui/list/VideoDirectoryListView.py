import operator
from math import floor, ceil
from random import random, randint

import PySide2
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QTableView, QVBoxLayout, QStyledItemDelegate, QHeaderView, QStyle

from vstreamer.gui.list import DataMock


class VideoDirectoryListView(QtWidgets.QWidget):

    def __init__(self, data_list=DataMock.mock_data(), parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 800, 800)
        self.setWindowTitle("Wybierz plik wideo")
        table_model = ItemModel(self, data_list)

        table_view = QTableView()
        table_view.setModel(table_model)
        table_view.setItemDelegate(ImageDelegate(table_view))
        table_view.resizeColumnsToContents()
        table_view.setShowGrid(False)
        table_view.horizontalHeader().setVisible(False)
        table_view.verticalHeader().setVisible(False)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table_view.horizontalHeader().setMinimumSectionSize(0)
        table_view.horizontalHeader().setDefaultSectionSize(120)
        table_view.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table_view.verticalHeader().setMinimumSectionSize(0)
        table_view.verticalHeader().setDefaultSectionSize(120)




        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)


class ItemModel(QAbstractTableModel):
    def __init__(self, parent, list, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.list = list

    def rowCount(self, parent):
        return ceil(len(self.list) / 3)

    def columnCount(self, parent):
        return 3

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        row = index.row()
        col = index.column()
        index = row*3+col
        if(index >= len(self.list)):
            return None
        return self.list[index][0]


class ImageDelegate(QStyledItemDelegate):

    def __init__(self, parent):
        QStyledItemDelegate.__init__(self, parent)
        self.padding =10

    def paint(self, painter, option, index):
        # option.rect.translate(self.padding,self.padding)
        rect = QStyle.alignedRect(
            Qt.LayoutDirectionAuto,
            Qt.AlignCenter,
            QSize(10,10),
            option.rect
        )
        painter.fillRect(rect, QtGui.QColor(randint(0,255), randint(0,255), randint(0,255)))

        # path = "/home/tom/Templates/test/mini.bmp"


        # image = QtGui.QImage(str(path))
        # pixmap = QtGui.QPixmap.fromImage(image)
        # pixmap.scaled(90, 90,QtCore.Qt.IgnoreAspectRatio)
        # painter.drawPixmap(option.rect, pixmap)
        # painter.drawText(0, 20, "TEST")

    # def createEditor(self, parent: PySide2.QtWidgets.QWidget,
    #                  option: PySide2.QtWidgets.QStyleOptionViewItem,
    #                  index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QWidget:
    #     widget =


class ItemWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

