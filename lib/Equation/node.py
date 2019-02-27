

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value
        self.left = left    # Left child
        self.right = right  # Right child

    def __str__(self):
        leftSide = str(self.left) if isinstance(
            self.left, int) else f"({str(self.left)})"
        rightSide = str(self.right) if isinstance(
            self.right, int) else f"({str(self.right)})"
        return f"{leftSide}{self.value}{rightSide}"

    def count_terms(self):
        count = 0
        if isinstance(self.value, int) is True:
            return 1
        count += 1 if isinstance(self.left, int) else self.left.count_terms()

        count += 1 if isinstance(self.right, int) else self.right.count_terms()
        return count

    def calc(self):
        if isinstance(self.value, int) is True:
            return self.value

        leftCalc = self.left if isinstance(
            self.left, int) else self.left.calc()
        rightCalc = self.right if isinstance(
            self.right, int) else self.right.calc()

        if self.value == "+":
            return leftCalc+rightCalc
        if self.value == "-":
            return leftCalc-rightCalc
        if self.value == "*":
            return leftCalc*rightCalc
        if self.value == "/":
            return int(leftCalc/rightCalc)
