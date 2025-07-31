from calculator.interactive import get_user_input
from calculator.core import addition, subtraction, multiplication, division, exponentiation

def main():
    num1, op, num2 = get_user_input()
    if None in (num1, op, num2):
        return None

    match op:
        case "+":
            return addition(num1, num2)
        case "-":
            return subtraction(num1, num2)
        case "*":
            return multiplication(num1, num2)
        case "/":
            return division(num1, num2)
        case "**":
            return exponentiation(num1, num2)
        case _:
            print("Неизвестная операция")
            return None

if __name__ == "__main__":
    result = main()
    print("Результат:", result)
