def get_user_input():
    """
    Принимает на входе число или q для завершения. После запрашивает у пользователя математическую операцию.
    Затем запрашивает у пользователя число 2 или q для завершения работы.
    Обрабатывает ошибки, если пользователь ввел НЕ число
    """
    try:
        choice_num1 = input("Введите первое число (или 'q' для выхода): ")
        if choice_num1.lower() in ("q", "exit"):
            user_answer = input("Вы уверены, что хотите выйти? (y/no): ")
            if user_answer.lower() in ("y", "yes"):
                print("Штош... Вы завершили работу калькулятора")
                return None, None, None
            else:
                choice_num1 = input("Введите первое число заново: ")

        num1 = float(choice_num1)

        math_op = input("Выберите операцию (+, -, *, /, **): ").strip()

        choice_num2 = input("Введите второе число (или 'q' для выхода): ")
        if choice_num2.lower() in ("q", "exit"):
            print("Вы завершили работу калькулятора.")
            return None, None, None

        num2 = float(choice_num2)

        return num1, math_op, num2

    except ValueError:
        print("Ошибка: введено не число.")
        return None, None, None


def main():
    get_user_input()


if __name__ == "__main__":
    main()
