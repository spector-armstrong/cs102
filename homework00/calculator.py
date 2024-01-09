import math
import typing as tp


def calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    if command == "+":
        return num_1 + num_2
    if command == "-":
        return num_1 - num_2
    if command == "/":
        if num_2 == 0:
            return "Нельзя делить на ноль"
        else:
            return round(num_1 / num_2, 1)
    if command == "*":
        return num_1 * num_2
    if command == "^":
        return num_1**num_2
    if command == "^2":
        return num_1**2
    if command == "sin":
        return round(math.sin(math.radians(num_1)), 1)
    if command == "cos":
        return round(math.cos(math.radians(num_1)), 1)
    if command == "tan":
        return round(math.tan(math.radians(num_1)), 1)
    if command == "lg":
        if num_1 < 0:
            return "Не существует логарифма от отрицательного числа"
        else:
            return round(math.log10(num_1), 1)
    if command == "ln":
        if num_1 < 0:
            return "Не существует логарифма от отрицательного числа"
        else:
            return round(math.log1p(num_1), 1)
    else:
        return f"Неизвестный оператор: {command!r}."


if __name__ == "__main__":
    while True:
        COMMAND = input("Введите оперцию > ")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        if COMMAND in {"^2", "sin", "cos", "tan", "ln", "lg"}:
            NUM_1 = float(input("Первое число > "))
            print(calc(NUM_1, 0, COMMAND))
        else:
            NUM_1 = float(input("Первое число > "))
            NUM_2 = float(input("Второе число > "))
            print(calc(NUM_1, NUM_2, COMMAND))
