# src/package/tracking.py
import logging
import os


class Tracking:
    """
    The Tracking class provides a simple logging mechanism with configurable options based on environment variables.

    Attributes:
    - No public attributes.

    Methods:
    - __init__: Initializes the Tracking class.
    - emit: Logs a message with the specified message type.
    - report: Logs a report if the SWICH_TRACKING_REPORT environment variable is set to "true".
    - trace: Logs a trace message if the SWICH_TRACKING_TRACE environment variable is set to "true".
    - verbose: Logs a verbose message if the SWICH_TRACKING_VERBOSE environment variable is set to "true".
    - debug: Logs a debug message if the SWICH_TRACKING_DEBUG environment variable is set to "true".
    - info: Logs an info message if the SWICH_TRACKING_INFO environment variable is set to "true".
    - warn: Logs a warning message if the SWICH_TRACKING_WARN environment variable is set to "true".
    - error: Logs an error message if the SWICH_TRACKING_ERROR environment variable is set to "true".
    """

    def __init__(self):  # noqa: E999
        """
        Initializes the Tracking class.
        """
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.INFO,
        )

    def emit(self, message_type, message, data=None):
        """
        Logs a message with the specified type.

        Args:
        - message_type (str): The type of the message (e.g., "trace", "debug", "info").
        - message (str): The content of the message.
        - data (Optional): Additional data to be included in the log.

        Returns:
        - Timestamp (str): The timestamp when the message was logged.
        """
        timestamp = logging.info(f"[{message_type[0]}] {message}", extra=data)
        return timestamp or message

    def report(self, data):
        """
        Logs a report if the SWICH_TRACKING_REPORT environment variable is set to "true".

        Args:
        - data (str): The report data to be logged.

        Returns:
        - None
        """
        if (
            "SWICH_TRACKING_REPORT" in os.environ
            and os.environ["SWICH_TRACKING_REPORT"].lower() == "true"
        ):
            logging.info(data)
        return None

    def trace(self, message, data=None):
        """
        Logs a trace message if the SWICH_TRACKING_TRACE environment variable is set to "true".

        Args:
        - message (str): The content of the trace message.
        - data (Optional): Additional data to be included in the log.

        Returns:
        - None
        """
        if (
            "SWICH_TRACKING_TRACE" in os.environ
            and os.environ["SWICH_TRACKING_TRACE"].lower() == "true"
        ):
            return self.emit("trace", message, data)
        return None

    def verbose(self, message, data=None):
        """
        Logs a verbose message if the SWICH_TRACKING_VERBOSE environment variable is set to "true".

        Args:
        - message (str): The content of the verbose message.
        - data (Optional): Additional data to be included in the log.

        Returns:
        - None
        """
        if (
            "SWICH_TRACKING_VERBOSE" in os.environ
            and os.environ["SWICH_TRACKING_VERBOSE"].lower() == "true"
        ):
            return self.emit("log", message, data)
        return None

    def debug(self, message, data=None):
        """
        Logs a debug message if the SWICH_TRACKING_DEBUG environment variable is set to "true".

        Args:
        - message (str): The content of the debug message.
        - data (Optional): Additional data to be included in the log.

        Returns:
        - None
        """
        if (
            "SWICH_TRACKING_DEBUG" in os.environ
            and os.environ["SWICH_TRACKING_DEBUG"].lower() == "true"
        ):
            return self.emit("debug", message, data)
        return None

    def info(self, message, data=None):
        """
        Logs an info message if the SWICH_TRACKING_INFO environment variable is set to "true".

        Args:
        - message (str): The content of the info message.
        - data (Optional): Additional data to be included in the log.

        Returns:
        - None
        """
        if (
            "SWICH_TRACKING_INFO" in os.environ
            and os.environ["SWICH_TRACKING_INFO"].lower() == "true"
        ):
            return self.emit("info", message, data)
        return None

    def warn(self, message, data=None):
        """
        Logs a warning message if the SWICH_TRACKING_WARN environment variable is set to "true".

        Args:
        - message (str): The content of the warning message.
        - data (Optional): Additional data to be included in the log.

        Returns:
        - None
        """
        if (
            "SWICH_TRACKING_WARN" in os.environ
            and os.environ["SWICH_TRACKING_WARN"].lower() == "true"
        ):
            return self.emit("warn", message, data)
        return None

    def error(self, message, data=None):
        """
        Logs an error message if the SWICH_TRACKING_ERROR environment variable is set to "true".

        Args:
        - message (str): The content of the error message.
        - data (Optional): Additional data to be included in the log.

        Returns:
        - None
        """
        if (
            "SWICH_TRACKING_ERROR" in os.environ
            and os.environ["SWICH_TRACKING_ERROR"].lower() == "true"
        ):
            return self.emit("error", message, data)
        return None
