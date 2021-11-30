import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.calc = Calculator()
        result = self.calc.add(5,7)
        self.assertEqual(result, 12)
    
    def test_substraction(self):
        self.calc = Calculator()
        result = self.calc.subtract(12,3)
        self.assertEqual(result, 9)
    
    def test_multiply(self):
        self.calc = Calculator()
        result = self.calc.multiply(9,7)
        self.assertEqual(result, 63)

    def test_division(self):
        self.calc = Calculator()
        result = self.calc.divide(21,3)
        self.assertEqual(result, 7)

if __name__=="__main__":
    unittest.main()