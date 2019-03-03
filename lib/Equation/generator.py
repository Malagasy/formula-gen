import random
from typing import List

from .parser import Sign
from .node import Node


class Generator:

    def _should_generate_number(self) -> bool:
        if self._number_of_signs > 0:
            return False
        return True

    def generate(self, number_of_terms: int, signs: List[str]) -> Node:

        for sign in signs:
            if sign not in Sign.list():
                raise Exception(f"Unknown sign : ${sign}")
        if number_of_terms <= 1:
            raise Exception("Number of terms can not be zero or one.")

        self.signs = signs
        self._number_of_signs = number_of_terms-2

        rootNode = None
        while True:
            try:
                rootNode = self._generate_node(Node(self.get_random_sign()))
                break
            except ZeroDivisionError:
                pass

        return rootNode

    def get_random_sign(self):
        return random.choice(self.signs)

    def get_divisors(self, number: int):
        divisors = []
        i = 1
        while i < number:
            if number % i == 0:
                divisors.append(i)
            i = i + 1
        return divisors

    def _generate_node(self, node: Node, target_value=None) -> Node:

        rightSide = None
        if self._should_generate_number() is True:
            if target_value is not None:
                if node.value == Sign.MULTIPLY.value:
                    rightSide = random.choice(self.get_divisors(target_value))
                if node.value == Sign.DIVIDE.value:
                    rightSide = target_value*random.randint(1, 5)
            else:
                rightSide = random.randint(1, 15)
        else:
            self._number_of_signs -= 1
            if target_value is not None:
                if node.value == Sign.MULTIPLY.value:
                    rightSide = random.choice(self.get_divisors(target_value))
                if node.value == Sign.DIVIDE.value:
                    rightSide = target_value*random.randint(1, 5)
                self._generate_node(
                    Node(self.get_random_sign()), rightSide)
            else:
                rightSide = self._generate_node(
                    Node(self.get_random_sign()))
        node.right = rightSide

        leftSide = None
        node_right_value = node.right if isinstance(
            node.right, int) else node.right.calc()
        if target_value is not None:
            if node.value == Sign.ADDITION.value:
                leftSide = target_value-node_right_value
            if node.value == Sign.SUBTRACT.value:
                leftSide = target_value+node_right_value
            if node.value == Sign.MULTIPLY.value:
                leftSide = int(target_value/node_right_value)
            if node.value == Sign.DIVIDE.value:
                leftSide = target_value*node_right_value
        else:
            leftSide = random.randint(
                1, 15) if node.value != Sign.DIVIDE.value else random.randint(1, 5)*node_right_value
        if self._should_generate_number() is False:
            leftSide = self._generate_node(Node(self.get_random_sign(
            )), leftSide if node.value != Sign.DIVIDE.value else random.randint(1, 5)*node_right_value)
        node.left = leftSide
        return node

        pass
