import unittest


class Test(unittest.TestCase):
  def __init__(self):
    print("Test runner called")

def load_test(loader, tests, pattern):
  print("Load test called")
