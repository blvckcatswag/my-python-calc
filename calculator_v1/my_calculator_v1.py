try:
    digit_1 = float(input("Введите первое число:"))
    operation = input("Выберите мaтематическую операцию: +, -, *, /, **").strip()
    digit_2 = float(input("Введите второе число:"))

    def addition (digit_1, digit_2):
         return digit_1 + digit_2


    def subtraction (digit_1, digit_2):
        return  digit_1 - digit_2


    def multiplication (digit_1, digit_2):
        return digit_1 * digit_2


    def division (digit_1, digit_2):
       return digit_1 / digit_2

    def exponentiation (digit_1, digit_2):
        return digit_1 ** digit_2


    if operation == "+" :
        result = addition(digit_1, digit_2)
        print(f"Результат сложения равен: {result}")
    elif operation == "-" :
        result = subtraction(digit_1, digit_2)
        print(f"Результат вычитания равен: {result}")
    elif operation == "*" :
        result = multiplication(digit_1, digit_2)
        print(f"Произведение равно: {result}")
    elif operation == "/" :
        result = division(digit_1, digit_2)
        print(f"Результат деления равен: {result}")
    elif operation == "**" :
        result = exponentiation(digit_1, digit_2)
        print(f"Результат возведения в степень равен: {result}")
    else:
        print("Такой математической операции нет")

except ZeroDivisionError:
    print("❌ Нельзя делить на ноль!")
except ValueError:
    print("❌ Нужно вводить именно числа!")
except Exception as error:
    print("❌ Что-то пошло не так:", error)

