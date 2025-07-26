def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")


def addition(a, b):
    validate_numbers(a, b)
    return a + b


def subtraction(a, b):
    validate_numbers(a, b)
    return a - b

def multiplication(a, b):
    validate_numbers(a, b)
    return a * b


def division(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя!")
    return a / b


def exponentiation(a, b):
    validate_numbers(a, b)
    return a ** b
