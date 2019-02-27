import unittest

from ..node import Node


class TestNode(unittest.TestCase):
    def test_count_terms(self):
        node = Node("+", 1, 23)
        self.assertEqual(node.count_terms(), 2)
        node = Node("+", 1, Node("-", 102, 193))
        self.assertEqual(node.count_terms(), 3)
        node = Node("+", Node("+", 6, 9), Node("-", 102, 193))
        self.assertEqual(node.count_terms(), 4)
        node = Node("+", Node("+", 6, 9), 10)
        self.assertEqual(node.count_terms(), 3)
        node = Node("+", Node("+", 6, 9),
                    Node("-", 102, Node("/", 2, Node(3))))
        self.assertEqual(node.count_terms(), 5)

    def test_calc(self):
        node = Node("+", 1, 23)
        self.assertEqual(node.calc(), 24)
        node = Node("+", 1, Node("-", 102, 193))
        self.assertEqual(node.calc(), -90)
        node = Node("+", Node("+", 6, 9), 10)
        self.assertEqual(node.calc(), 25)

        node = Node("+", Node("+", 6, 9), Node(15))
        self.assertEqual(node.calc(), 30)
