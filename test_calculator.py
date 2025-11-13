import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add1(self):
        self.assertEqual(self.calc.add(2,3), 5)

    def test_add2(self):
        self.assertEqual(self.calc.add(10,-5), 5)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(10, 20), -10)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(30, 15), 15)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(20, 10), 2)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(21, 6), 3)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(15, 6), 3)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(5, 10), 5)

if __name__ == '__main__':
    unittest.main()