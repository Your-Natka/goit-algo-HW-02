from collections import deque


def is_palindrome(text: str) -> bool:
    """Перевіряє, чи є рядок паліндромом (без пробілів і регістру)"""
    # прибираємо пробіли та робимо нижній регістр
    cleaned_text = "".join(ch.lower() for ch in text if ch.isalnum())

    d = deque(cleaned_text)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


if __name__ == "__main__":
    test_strings = [
        "А роза упала на лапу Азора",
        "Дім міД",
        "Привіт",
        "12321",
        "123321",
    ]

    for s in test_strings:
        print(f"'{s}' -> {is_palindrome(s)}")
