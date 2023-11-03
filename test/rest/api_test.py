import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

#    def test_api_add(self):
#        url = f"{BASE_URL}/calc/add/2/2"
#        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
#        self.assertEqual(
#            response.status, http.client.OK, f"Error en la petición API a {url}"
#        )
    def test_api_add(self):
        self._test_api_operation("add", 2, 2, 4)

    def test_api_substract(self):
        self._test_api_operation("substract", 5, 3, 2)

    def test_api_multiply(self):
        self._test_api_operation("multiply", 4, 3, 12)

    def test_api_divide(self):
        self._test_api_operation("divide", 10, 2, 5)

    def test_api_power(self):
        self._test_api_operation("power", 2, 3, 8)

    def test_api_square_root(self):
        self._test_api_operation("square_root", 9, 3)

    def test_api_logarithm(self):
        self._test_api_operation("logarithm", 100, 2.0)

    def _test_api_operation(self, operation, operand1, operand2, expected_result=None):
        if operation in ["square_root", "logarithm"]:
            url = f"{BASE_URL}/calc/{operation}/{operand1}"
        else:
            url = f"{BASE_URL}/calc/{operation}/{operand1}/{operand2}"
        
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        if expected_result is not None:
            response_data = response.read().decode("utf-8")
            self.assertEqual(
                float(response_data), expected_result, "Resultado incorrecto de la operación"
            )

if __name__ == "__main__":
    unittest.main()