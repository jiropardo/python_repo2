# tests/test_module1.py
import unittest
from modules.module1 import function1

class TestModule1(unittest.TestCase):
    def test_function1(self):
        result = function1()
        print(result)
        self.assertEqual(function1(), "Hello from module1!")

if __name__ == "__main__":
    unittest.main()