import re
from typing import Callable


def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку дійсних чисел
    # \b - межа слова, \d+ - одна або більше цифр, \.\d+ - крапка та цифри після неї
    # Шаблон знаходить числа, які відокремлені пробілами
    pattern = r'\b\d+\.\d+\b'

    # Знаходимо всі числа у тексті
    matches = re.findall(pattern, text)

    # Повертаємо кожне число як float через yield
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable):
    # Використовуємо генератор для отримання всіх чисел
    # Підсумовуємо їх за допомогою функції sum()
    total = sum(func(text))
    return total


# Приклад використання:
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
