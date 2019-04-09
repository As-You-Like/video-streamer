from PySide2 import QtWidgets, QtGui


class ImageView(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setPixmap(QtGui.QPixmap("/home/tom"))
