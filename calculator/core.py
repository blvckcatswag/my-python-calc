def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя!")
    return a / b

def exponentiation(a, b):
    return a ** b
