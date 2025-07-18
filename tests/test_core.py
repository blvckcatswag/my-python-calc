import unittest
from calculator import core


class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.a = 6
        self.b = 2

    def test_division(self):
        self.assertEqual(core.division(self.a, self.b), 3)

        def test_division_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                core.division(5, 0)

    def test_substraction(self):
        self.assertEqual(core.subtraction(self.a, self.b), 4)

    def test_exponentiation(self):
        self.assertEqual(core.exponentiation(self.a, self.b), 36)

    def test_addition(self):
        self.assertEqual(core.addition(self.a, self.b), 8)

    def test_multiplication(self):
        self.assertEqual(core.multiplication(self.a, self.b), 12)
