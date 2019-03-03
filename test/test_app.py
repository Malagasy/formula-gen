import json
import unittest
import urllib.parse
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def assertEquationSuccess(self, response: str):
        response = json.loads(response)
        self.assertNotIn("error", response)
        self.assertIn("data", response)
        self.assertIsInstance(response["data"], str)

    def assertEquationFailure(self, response: str):
        response = json.loads(response)
        self.assertIn("error", response)
        self.assertNotIn("data", response)
        self.assertIsInstance(response["error"], str)

    def test_get_equation_success(self):
        signs: str = "+,/,-".encode("utf-8")
        response = self.client.get(
            f"/equation/3?signs={urllib.parse.quote(signs)}")
        self.assertEquationSuccess(response.data)

        signs: str = "-".encode("utf-8")
        response = self.client.get(
            f"/equation/5?signs={urllib.parse.quote(signs)}")
        self.assertEquationSuccess(response.data)

    def test_get_equation_failure(self):
        signs: str = "+,/,-".encode("utf-8")
        response = self.client.get(
            f"/equation/1?signs={urllib.parse.quote(signs)}")
        self.assertEquationFailure(response.data)

        response = self.client.get(f"/equation/5")
        self.assertEquationFailure(response.data)

    def test_get_multiple_equation_success(self):
        signs: str = "+,/,-".encode("utf-8")
        rv = self.client.get(
            f"/batch/10/equation/3?signs={urllib.parse.quote(signs)}")
        response = json.loads(rv.data)

        self.assertEqual(len(response["data"]), 10)

    def test_get_multiple_equation_failure(self):
        signs: str = "+,/,-".encode("utf-8")
        response = self.client.get(
            f"/batch/10/equation/1?signs={urllib.parse.quote(signs)}")
        self.assertEquationFailure(response.data)

        response = self.client.get(f"/batch/10/equation/5")
        self.assertEquationFailure(response.data)


if __name__ == '__main__':
    unittest.main()
