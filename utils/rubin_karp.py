from timeit import timeit


def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


class RabinKarp:
    def __init__(self, text):
        self.text = text

    def rabin_karp_search(self, pattern):
        # Довжини основного рядка та підрядка пошуку
        substring_length = len(pattern)
        main_string_length = len(self.text)

        # Базове число для хешування та модуль
        base = 256
        modulus = 101

        # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
        substring_hash = polynomial_hash(pattern, base, modulus)
        current_slice_hash = polynomial_hash(self.text[:substring_length], base, modulus)

        # Попереднє значення для перерахунку хешу
        h_multiplier = pow(base, substring_length - 1) % modulus

        # Проходимо крізь основний рядок
        for i in range(main_string_length - substring_length + 1):
            if substring_hash == current_slice_hash:
                if self.text[i:i + substring_length] == pattern:
                    return i

            if i < main_string_length - substring_length:
                current_slice_hash = (current_slice_hash - ord(self.text[i]) * h_multiplier) % modulus
                current_slice_hash = (current_slice_hash * base + ord(self.text[i + substring_length])) % modulus
                if current_slice_hash < 0:
                    current_slice_hash += modulus

        return -1

    def search_with_time(self, pattern, number=100):
        return timeit(lambda: self.rabin_karp_search(pattern), number=number)
