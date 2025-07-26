from unittest import TestCase
from unittest.mock import patch
from calculator import interactive


class TestUserInput(TestCase):
    @patch("builtins.input", side_effect=["5", "+", "3"])
    def test_valid_input(self, mock_input):
        num1, op, num2 = interactive.get_user_input()
        self.assertEqual(num1, 5.0)
        self.assertEqual(op, "+")
        self.assertEqual(num2, 3.0)

    @patch("builtins.input", side_effect=["q", "y"])
    def test_exit_input(self, mock_input):
        num1, op, num2 = interactive.get_user_input()
        self.assertIsNone(num1)
        self.assertIsNone(op)
        self.assertIsNone(num2)
