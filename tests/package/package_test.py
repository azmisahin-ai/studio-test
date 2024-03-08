from src.package import Tracking
import unittest


class TestPackage(unittest.TestCase):
    def test_Tracking_initialization(self):
        tracking_instance = Tracking()
        result = tracking_instance.debug
        self.assertTrue(result)  # Check if the result of a specific method is truthy


if __name__ == "__main__":
    unittest.main()
