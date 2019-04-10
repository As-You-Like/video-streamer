from PySide2 import QtWidgets, QtGui


class ImageView(QtWidgets.QLabel):
    def __init__(self, path, text, parent=None):
        super().__init__(parent)
        self.update_data(text, path)

    def update_data(self,text,bmp_path):
        image = QtGui.QImage(str(bmp_path))
        self.setText(text)
        self.setPixmap(QtGui.QPixmap.fromImage(image))

