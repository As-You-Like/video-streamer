import sys
import logging
import vstreamer_utils
from PySide2 import QtCore


class ErrorHandler:
    def __init__(self):
        app_name = QtCore.QCoreApplication.applicationName()
        self.logger = logging.getLogger(app_name)

    def handle_error(self, error):
        logger = self._get_logging_function(error)
        logger(str(error))
        if error.level == vstreamer_utils.ErrorLevel.CRITICAL:
            QtCore.QCoreApplication.exit(1)
            sys.exit(1)

    def handle_exception(self, exception):
        self.handle_error(vstreamer_utils.Error("Exception occurred: " + str(exception),
                                                vstreamer_utils.ErrorLevel.CRITICAL))

    def _get_logging_function(self, error):
        if error.level == vstreamer_utils.ErrorLevel.WARNING:
            return self.logger.warning
        if error.level == vstreamer_utils.ErrorLevel.ERROR:
            return self.logger.error
        if error.level == vstreamer_utils.ErrorLevel.CRITICAL:
            return self.logger.critical
        raise ValueError("No suitable logger for error object found")
