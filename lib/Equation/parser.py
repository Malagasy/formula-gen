import re
from enum import Enum
from typing import List

from .node import Node


class Sign(Enum):
    ADDITION = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

    def list():
        return list(map(lambda x: x.value, list(Sign)))


class Parser:

    def parse(self, equation: str):
        self.validate_equation(equation)

        equation = equation.replace(" ", "")

        rpn_equation = self._parse_string_to_npr(equation)
        node_equation = self._parse_npr_to_node(rpn_equation)
        return node_equation
        # return self._parse_string(equation)

    def validate_equation(self, equation: str) -> bool:
        if equation is None:
            raise Exception("Empty equation")
        if equation.count("(") != equation.count(")"):
            raise Exception("Parenthesis are not consistent in this equation.")
        return True

    def _operator_has_lower_precedence(self, operator_stack: List, operator):
        if len(operator_stack) == 0:
            return False
        if operator in [Sign.ADDITION.value, Sign.SUBTRACT.value] and operator_stack[-1] in [Sign.MULTIPLY.value, Sign.DIVIDE.value]:
            return True
        return False

    def _operator_has_same_precedence(self, operator_stack, operator):
        if len(operator_stack) == 0:
            return False
        if (operator in [Sign.ADDITION.value, Sign.SUBTRACT.value] and operator_stack[-1] in [Sign.ADDITION.value, Sign.SUBTRACT.value]) or (operator in [Sign.MULTIPLY.value, Sign.DIVIDE.value] and operator_stack[-1] in [Sign.MULTIPLY.value, Sign.DIVIDE.value]):
            return True
        return False

    def _parse_string_to_npr(self, string_node: str) -> List[str]:
        output_stack = []
        operator_stack = []

        previous_token_was_numeric = False

        for token in string_node:
            if token.isnumeric() is True:
                if previous_token_was_numeric is True:
                    output_stack[-1] = int(f"{output_stack[-1]}{token}")
                else:
                    output_stack.append(int(token))
                previous_token_was_numeric = True
            elif token in Sign.list():
                while self._operator_has_lower_precedence(operator_stack, token) or self._operator_has_same_precedence(operator_stack, token):
                    output_stack.append(operator_stack.pop())
                operator_stack.append(token)
                previous_token_was_numeric = False
            elif token == "(":
                operator_stack.append(token)
                previous_token_was_numeric = False
            elif token == ")":
                while len(operator_stack) > 0 and operator_stack[-1] != "(":
                    output_stack.append(operator_stack.pop())
                while len(operator_stack) > 0 and operator_stack[-1] == "(":
                    operator_stack.pop()
                previous_token_was_numeric = False
            else:
                raise Exception(f"This character can't be parsed : {token}")

        while len(operator_stack) != 0:
            output_stack.append(operator_stack.pop())

        return output_stack

    def _parse_npr_to_node(self, rpn_equation: List[str]) -> Node:

        if len(rpn_equation) == 0:
            return None

        while len(rpn_equation) > 1:
            index = 0
            for token in rpn_equation:
                if token in Sign.list():
                    node = Node(
                        token, left=rpn_equation[index-2], right=rpn_equation[index-1])
                    del rpn_equation[index-2:index]
                    rpn_equation[index-2] = node
                    break
                index += 1

        return rpn_equation[0]
