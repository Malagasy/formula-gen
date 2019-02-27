import unittest

from ..node import Node
from ..parser import Parser


class Test(unittest.TestCase):
    parser = Parser()

    def assertNode(self, equation: str, node: Node):
        result = Test.parser.parse(equation)
        self.assertEqual(result.value, node.value)
        if isinstance(node.left, int) is True:
            self.assertEqual(result.left, node.left)
        else:
            self.assertNode(result.left, node.left)

        if isinstance(node.right, int) is True:
            self.assertEqual(result.right, node.right)
        else:
            self.assertNode(result.right, node.right)

    def test_parse_string_to_npr_success(self):
        result = Test.parser._parse_string_to_npr("3+4*(2/(1-5))")
        self.assertEqual(result, [3, 4, 2, 1, 5, '-', '/', '*', '+'])

        result = Test.parser._parse_string_to_npr("3+4*2/(1-5)")
        self.assertEqual(result, [3, 4, 2, '*', 1, 5, '-', '/', '+'])

        result = Test.parser._parse_string_to_npr("(3+4)*2/(1-5)")
        self.assertEqual(result, [3, 4, '+', 2, '*', 1, 5, '-', '/'])

    def test_parse_npr_to_node_success(self):
        self.assertNode("1+2", Node("+", 1, 2))
        self.assertNode("12*501", Node("*", 12, 501))
        self.assertNode("12+51", Node("+", 12, 51))
        self.assertNode("12/51", Node("/", 12, 51))

    def test_parser_node_simple_error(self):
        with self.assertRaises(Exception) as error:
            result = Test.parser.parse("12*k")

        with self.assertRaises(Exception) as error:
            result = Test.parser.parse("12=5")

        with self.assertRaises(Exception) as error:
            result = Test.parser.parse("(12+4")


if __name__ == '__main__':
    unittest.main()
