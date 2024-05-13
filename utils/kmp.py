from timeit import timeit


class KMP:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def compute_lps(pattern=''):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def search(self, pattern):
        M = len(pattern)
        N = len(self.text)
        lps = self.compute_lps(pattern)

        i = j = 0

        while i < N:
            if pattern[j] == self.text[i]:
                i += 1
                j += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1

            if j == M:
                return i - j

        return -1  # якщо підрядок не знайдено

    def search_with_time(self, pattern, number=100):
        return timeit(lambda: self.search(pattern), number=number)