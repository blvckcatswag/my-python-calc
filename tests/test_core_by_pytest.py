from calculator.core import *
import pytest
from contextlib import nullcontext as does_not_raise


class TestCalculatorCore:
    # TODO: Написать тесты на функцию сложения и добавить докстринг
    @pytest.mark.parametrize(
        "num1, num2, result, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (0, 5, 5, does_not_raise()),
            (-5, 5, 0, does_not_raise()),
            (-10, -2.5, -12.5, does_not_raise()),
            (100, '100', 200, pytest.raises(TypeError)),
        ]
    )
    def test_addition(self, num1, num2, result, expectation):
        """
            Тестирует функцию addition:
            - Проверяет корректные случаи сложения чисел (целых и с плавающей точкой).
            - Проверяет вызов TypeError при передаче строки.
        """
        with expectation:
            assert addition(num1, num2) == result

    # TODO: Написать тесты на функцию вычитания и добавить докстринг
    @pytest.mark.parametrize(
        "num1, num2, result, expectation",
        [
            (1, 2, -1, does_not_raise()),
            (0, 5, -5, does_not_raise()),
            (-5.5, 2.5, -8, does_not_raise()),
            (0, 0, 0, does_not_raise()),
            (5, None, 5, pytest.raises(TypeError)),
        ]

    )
    def test_subtraction(self, num1, num2, result, expectation):
        """
            Тестирует функцию subtraction:
            - Проверяет вычитание для целых и вещественных чисел.
            - Проверяет вызов TypeError при недопустимом типе второго аргумента.
        """
        with expectation:
            assert subtraction(num1, num2) == result

    # TODO: Написать тесты на функцию умножения и добавить докстринг
    @pytest.mark.parametrize(
        "num1, num2, result, expectation",
        [
            (1, 1, 1, does_not_raise()),
            (0, '', 5, pytest.raises(TypeError)),
            (-2, 2.5, -5, does_not_raise()),
            (0, 0, 0, does_not_raise()),
        ]
    )
    def test_multiplication(self, num1, num2, result, expectation):
        """
            Тестирует функцию multiplication:
            - Проверяет корректное умножение.
            - Проверяет TypeError при передаче строки.
        """
        with expectation:
            assert multiplication(num1, num2) == result

    # TODO: Написать тесты на функцию деления и добавить докстринг
    @pytest.mark.parametrize(
        "num1, num2, result, expectation",
        [
            (1, 1, 1, does_not_raise()),
            (0, '', 5, pytest.raises(TypeError)),
            (-2, 2, -1, does_not_raise()),
            (10, 0, 0, pytest.raises(ZeroDivisionError)),
            (10, 2.5, 4, does_not_raise()),
        ]
    )
    def test_division(self, num1, num2, result, expectation):
        """
            Тестирует функцию division:
            - Проверяет деление для чисел.
            - Проверяет деление на ноль (ZeroDivisionError).
            - Проверяет TypeError при строке.
        """
        with expectation:
            assert division(num1, num2) == result

    # TODO: Написать тесты на функцию возведения в степень и добавить докстринг
    @pytest.mark.parametrize(
        "num1, num2, result, expectation",
        [
            (1, 1, 1, does_not_raise()),
            (0, '', 5, pytest.raises(TypeError)),
            (-2, 2, 4, does_not_raise()),
            (10, 0, 1, does_not_raise()),
            (10, 10, 10000000000, does_not_raise()),
        ]
    )
    def test_exponentiation(self, num1, num2, result, expectation):
        """
           Тестирует функцию exponentiation:
           - Проверяет возведение в степень с положительными и отрицательными числами.
           - Проверяет TypeError при передаче строки.
        """
        with expectation:
            assert exponentiation(num1, num2) == result

    # TODO: Написать тесты на функцию валидации и добавить докстринг
    @pytest.mark.parametrize(
        "num1, num2,  expectation",
        [
            (1, 1, does_not_raise()),
            (0, '', pytest.raises(TypeError)),
            (-2, 2, does_not_raise()),
            (10, 0, does_not_raise()),
            (10, 10, does_not_raise()),
            (0.5, None, pytest.raises(TypeError)),
            (1, [1, 2, 3], pytest.raises(TypeError)),
        ]
    )
    def test_validate_numbers(self, num1, num2, expectation):
        """
           Тестирует функцию validate_numbers:
           - Проверяет, что функция не вызывает исключения при передаче чисел.
           - Проверяет TypeError при передаче недопустимых типов.
        """
        with expectation:
            validate_numbers(num1, num2)
