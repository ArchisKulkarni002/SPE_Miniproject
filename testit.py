import unittest
import math
from calculator import calculateSquareRoot, calculateFactorial, calculateNaturalLog, calculatePower, add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-2, 4), 2)
        self.assertEqual(add(-999999999, 999999999), 0)
        self.assertEqual(add(1.5, 2.3), 3.8)
    
    def testSubtraction(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-100, -50), -50)
        self.assertEqual(subtract(1e10, 1e5), 9999900000)
    
    def testMultiplication(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 6), -12)
        self.assertEqual(multiply(0, 999), 0)
        self.assertEqual(multiply(1.5, 2), 3.0)
    
    def testDivision(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(5, 0), "Error: Division by zero is not allowed.")
        self.assertEqual(divide(-10, 2), -5)
        self.assertAlmostEqual(divide(7, 3), 2.33333, places=5)
    
    def testSquareRoot(self):
        self.assertEqual(calculateSquareRoot(9), 3)
        self.assertEqual(calculateSquareRoot(16), 4)
        self.assertAlmostEqual(calculateSquareRoot(2), 1.41421, places=5)
    
    def testFactorial(self):
        self.assertEqual(calculateFactorial(5), 120)
        self.assertEqual(calculateFactorial(0), 1)
        self.assertEqual(calculateFactorial(10), 3628800)
    
    def testNaturalLog(self):
        self.assertAlmostEqual(calculateNaturalLog(1), 0, places=5)
        self.assertAlmostEqual(calculateNaturalLog(math.e), 1, places=5)
        self.assertAlmostEqual(calculateNaturalLog(100), 4.60517, places=5)
    
    def testPowerFunction(self):
        self.assertEqual(calculatePower(2, 3), 8)
        self.assertEqual(calculatePower(5, 0), 1)
        self.assertEqual(calculatePower(-2, 3), -8)
        self.assertAlmostEqual(calculatePower(2, 0.5), 1.41421, places=5)
        self.assertEqual(calculatePower(10, -1), 0.1)

if __name__ == "__main__":
    unittest.main()
