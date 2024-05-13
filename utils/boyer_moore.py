from timeit import timeit


class BoyerMoore:
    def __init__(self, text):
        self.text = text
        self.shift_table = self.build_shift_table(text)

    @staticmethod
    def build_shift_table(pattern):
        """Створити таблицю зсувів для алгоритму Боєра-Мура."""
        table = {}
        length = len(pattern)
        # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1
        # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
        table.setdefault(pattern[-1], length)
        return table

    def search(self, pattern):
        # Створюємо таблицю зсувів для патерну (підрядка)
        shift_table = self.build_shift_table(pattern)
        i = 0  # Ініціалізуємо початковий індекс для основного тексту

        # Проходимо по основному тексту, порівнюючи з підрядком
        while i <= len(self.text) - len(pattern):
            j = len(pattern) - 1  # Починаємо з кінця підрядка

            # Порівнюємо символи від кінця підрядка до його початку
            while j >= 0 and self.text[i + j] == pattern[j]:
                j -= 1  # Зсуваємось до початку підрядка

            # Якщо весь підрядок збігається, повертаємо його позицію в тексті
            if j < 0:
                return i  # Підрядок знайдено

            # Зсуваємо індекс i на основі таблиці зсувів
            # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
            i += shift_table.get(self.text[i + len(pattern) - 1], len(pattern))

        # Якщо підрядок не знайдено, повертаємо -1
        return -1

    def search_with_time(self, pattern, number=100):
        return timeit(lambda: self.search(pattern), number=number)
