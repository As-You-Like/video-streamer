import sys
import logging
import vstreamer_utils
from PySide2 import QtCore


class ErrorHandler:
    def __init__(self):
        pass

    @staticmethod
    def handle_error(error):
        logger = ErrorHandler._get_logging_function(error)
        logger(str(error))
        if error.level == vstreamer_utils.ErrorLevel.CRITICAL:
            QtCore.QCoreApplication.exit(1)
            sys.exit(1)

    @staticmethod
    def handle_exception(exception):
        ErrorHandler.handle_error(vstreamer_utils.Error("Exception occurred: " + str(exception),
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
