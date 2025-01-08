# Глобальные переменные
NUMBERS = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14,
    "пятнадцать": 15, "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18,
    "девятнадцать": 19, "двадцать": 20, "тридцать": 30, "сорок": 40,
    "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80,
    "девяносто": 90
}

OPERATIONS = {
    "плюс": lambda x, y: x + y,
    "минус": lambda x, y: x - y,
    "умножить на": lambda x, y: x * y,
    "поделить на": lambda x, y: x // y if y != 0 else ZeroDivisionError("Деление на ноль")
}


def text_to_number(text):
    """Преобразует текстовое представление числа в числовое значение"""
    words = text.split()
    if "минус" in words:  # Если число отрицательное
        words.remove("минус")
        return -sum(NUMBERS[word] for word in words)
    else:
        return sum(NUMBERS[word] for word in words)


def calculate(expression):
    """Разбирает текстовое математическое выражение и вычисляет его результат"""
    # Обработка строки
    tokens = []
    words = expression.split()
    skip_next = False

    for i, word in enumerate(words):
        if skip_next:
            skip_next = False
            continue

        # Проверяем сложные операции
        if word in ["умножить", "поделить"] and i + 1 < len(words) and words[i + 1] == "на":
            tokens.append(f"{word} на")
            skip_next = True
        else:
            tokens.append(word)
    numbers = []
    operations = []

    # Распределяем выражения в operations и в num_tokens
    i = 0
    while i < len(tokens):
        if tokens[i] in OPERATIONS:
            operations.append(tokens[i])
        else:
            num_tokens = []
            while i < len(tokens) and tokens[i] not in OPERATIONS:
                num_tokens.append(tokens[i])
                i += 1
            numbers.append(text_to_number(" ".join(num_tokens)))
            i -= 1  # Возвращаем индекс на нужную позицию
        i += 1

    # Вычисление результата
    if tokens[0] == "минус":
        result = -numbers[0]
        operations.pop(0)
    else:
        result = numbers[0]

    for op, num in zip(operations, numbers[1:]):
        if op == "поделить на" and num == 0:
            raise ZeroDivisionError("Деление на ноль")
        result = OPERATIONS[op](result, num)

    return result


if __name__ == "__main__":
    expression = input("Введите математическое выражение: ")
    try:
        print("Результат:", calculate(expression))
    except ZeroDivisionError as e:
        print("Ошибка:", e)
    except KeyError:
        print("Ошибка: неверный ввод.")
