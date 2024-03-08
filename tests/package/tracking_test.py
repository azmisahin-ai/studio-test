import os
import unittest
from src.package.tracking import Tracking


class TrackingTest(unittest.TestCase):
    def setUp(self):
        # Set up environment variables before each test
        self.original_trace_value = os.environ.get("SWICH_TRACKING_TRACE", "true")
        os.environ["SWICH_TRACKING_TRACE"] = "true"

    def test_trace_method_when_true(self):
        # Test the trace method when the trace is enabled (SWICH_TRACKING_TRACE is 'true')
        trace = Tracking()
        result = trace.trace("Test message")
        self.assertEqual(result, "Test message")

    def test_trace_method_when_false(self):
        # Test the trace method when the trace is disabled (SWICH_TRACKING_TRACE is 'false')
        os.environ["SWICH_TRACKING_TRACE"] = "false"
        trace = Tracking()
        result = trace.trace("Test message")
        self.assertIsNone(result)  # If trace is disabled, None is expected

    def test_verbose_method_when_true(self):
        # Test the verbose method when verbose logging is enabled (SWICH_TRACKING_VERBOSE is 'true')
        trace = Tracking()
        result = trace.verbose("Test message")
        self.assertEqual(result, "Test message")

    def test_verbose_method_when_false(self):
        # Test the verbose method when verbose logging is disabled (SWICH_TRACKING_VERBOSE is 'false')
        os.environ["SWICH_TRACKING_VERBOSE"] = "false"
        trace = Tracking()
        result = trace.verbose("Test message")
        self.assertIsNone(result)

    def test_debug_method_when_true(self):
        # Test the debug method when debug logging is enabled (SWICH_TRACKING_DEBUG is 'true')
        trace = Tracking()
        result = trace.debug("Test message")
        self.assertEqual(result, "Test message")

    def test_debug_method_when_false(self):
        # Test the debug method when debug logging is disabled (SWICH_TRACKING_DEBUG is 'false')
        os.environ["SWICH_TRACKING_DEBUG"] = "false"
        trace = Tracking()
        result = trace.debug("Test message")
        self.assertIsNone(result)

    def test_info_method_when_true(self):
        # Test the info method when info logging is enabled (SWICH_TRACKING_INFO is 'true')
        trace = Tracking()
        result = trace.info("Test message")
        self.assertEqual(result, "Test message")

    def test_info_method_when_false(self):
        # Test the info method when info logging is disabled (SWICH_TRACKING_INFO is 'false')
        os.environ["SWICH_TRACKING_INFO"] = "false"
        trace = Tracking()
        result = trace.info("Test message")
        self.assertIsNone(result)

    def test_warn_method_when_true(self):
        # Test the warn method when warning logging is enabled (SWICH_TRACKING_WARN is 'true')
        trace = Tracking()
        result = trace.warn("Test message")
        self.assertEqual(result, "Test message")

    def test_warn_method_when_false(self):
        # Test the warn method when warning logging is disabled (SWICH_TRACKING_WARN is 'false')
        os.environ["SWICH_TRACKING_WARN"] = "false"
        trace = Tracking()
        result = trace.warn("Test message")
        self.assertIsNone(result)

    def test_error_method_when_true(self):
        # Test the error method when error logging is enabled (SWICH_TRACKING_ERROR is 'true')
        trace = Tracking()
        result = trace.error("Test message")
        self.assertEqual(result, "Test message")

    def test_error_method_when_false(self):
        # Test the error method when error logging is disabled (SWICH_TRACKING_ERROR is 'false')
        os.environ["SWICH_TRACKING_ERROR"] = "false"
        trace = Tracking()
        result = trace.error("Test message")
        self.assertIsNone(result)

    def tearDown(self):
        # Clean up environment variables after each test
        os.environ["SWICH_TRACKING_TRACE"] = self.original_trace_value
        os.environ["SWICH_TRACKING_VERBOSE"] = "true"
        os.environ["SWICH_TRACKING_DEBUG"] = "true"
        os.environ["SWICH_TRACKING_INFO"] = "true"
        os.environ["SWICH_TRACKING_WARN"] = "true"
        os.environ["SWICH_TRACKING_ERROR"] = "true"


if __name__ == "__main__":
    unittest.main()
