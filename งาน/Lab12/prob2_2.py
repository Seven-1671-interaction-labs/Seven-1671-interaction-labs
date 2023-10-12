import unittest
from prob2 import fibonacci, fact


class TestFibonacciFactorial(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)

    def test_fact(self):
        self.assertEqual(fact(0), 1)
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(2), 2)
        self.assertEqual(fact(5), 120)


if __name__ == "__main__":
    unittest.main()