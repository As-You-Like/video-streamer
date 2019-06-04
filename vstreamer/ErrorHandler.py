import sys
import logging
import vstreamer_utils
from PySide2 import QtCore, QtWidgets


class ErrorHandler(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        pass

    def handle_error(self, error):
        logger = ErrorHandler._get_logging_function(error)
        logger(str(error))
        QtWidgets.QMessageBox.critical(self.parent(), QtCore.QCoreApplication.applicationName(), "Critical error: " + str(error))
        if error.level in (vstreamer_utils.ErrorLevel.ERROR, vstreamer_utils.ErrorLevel.CRITICAL):
            QtCore.QCoreApplication.exit(1)
            sys.exit(1)

    def handle_exception(self, exception):
        self.handle_error(vstreamer_utils.Error("Exception occurred: " + str(exception),
                          vstreamer_utils.ErrorLevel.CRITICAL))

    @staticmethod
    def _get_logging_function(error):
        if error.level == vstreamer_utils.ErrorLevel.WARNING:
            return QtCore.QCoreApplication.instance().logger.warning
        if error.level == vstreamer_utils.ErrorLevel.ERROR:
            return QtCore.QCoreApplication.instance().logger.error
        if error.level == vstreamer_utils.ErrorLevel.CRITICAL:
            return QtCore.QCoreApplication.instance().logger.critical
        raise ValueError("No suitable logger for error object found")
