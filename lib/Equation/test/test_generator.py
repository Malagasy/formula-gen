import unittest

from ..node import Node

from ..generator import Generator


class TestGenerator(unittest.TestCase):
    def __init__(self, method):
        self.generator = Generator()
        self.generate = self.generator.generate

        return super().__init__(method)

    def test_generate_basic_success(self):
        signs = ["+", "-"]
        result = self.generate(2, signs)
        self.assertIsInstance(result, Node)
        self.assertIn(result.value, signs)

    def test_generate_basic_error(self):
        with self.assertRaises(Exception) as error:
            result = self.generate(0, ["+"])

        with self.assertRaises(Exception) as error:
            result = self.generate(3, ["+", "k"])

    def test_get_divisors(self):
        result = self.generator.get_divisors(7)
        self.assertEqual(result, [1])
        result = self.generator.get_divisors(10)
        self.assertEqual(result, [1, 2, 5])
        result = self.generator.get_divisors(16)
        self.assertEqual(result, [1, 2, 4, 8])

    def test_generate_equation_success(self):
        signs = ["+", "/"]
        result = self.generate(2, signs)
        self.assertEqual(result.count_terms(), 2)
        result = self.generate(5, signs)
        self.assertEqual(result.count_terms(), 5)
        result = self.generate(10, signs)
        self.assertEqual(result.count_terms(), 10)
