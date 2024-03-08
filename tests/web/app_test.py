# tests/web/app_test.py
import unittest
from src.web.app import create_app


class AppTest(unittest.TestCase):

    def test_home_endpoint(self):
        tester = create_app().test_client(self)
        response = tester.get("/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", data)
        self.assertIn("application", data)
        self.assertIn("environment", data)


if __name__ == "__main__":
    unittest.main()
