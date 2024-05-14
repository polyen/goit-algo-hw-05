
from utils.kmp import KMP
from utils.boyer_moore import BoyerMoore
from utils.rubin_karp import RabinKarp

if __name__ == "__main__":

    with open('data/text1.txt', 'r') as file:
        text1 = file.read()

    with open('data/text2.txt', 'r') as file:
        text2 = file.read()

    patterns_1 = { 'existed': 'принципи роботи алгоритмів', 'not_existed': 'принципиролгоритмів'}
    patterns_2 = { 'existed': 'розглянутими структурами даних у використанні', 'not_existed': 'принципиробгоритмів'}

    bm_1 = BoyerMoore(text1)
    bm_2 = BoyerMoore(text2)
    rk_1 = RabinKarp(text1)

    kmp_1 = KMP(text1)
    kmp_2 = KMP(text2)
    rk_2 = RabinKarp(text2)

    print('Text 1')
    for pattern in patterns_1.values():
        print(f'Pattern: {pattern}')
        print(f'Boyer-Moore: {bm_1.search_with_time(pattern)}')
        print(f'KMP: {kmp_1.search_with_time(pattern)}')
        print(f'Rabin-Karp: {rk_1.search_with_time(pattern)}')
        print()

    print('Text 2')
    for pattern in patterns_2.values():
        print(f'Pattern: {pattern}')
        print(f'Boyer-Moore: {bm_2.search_with_time(pattern)}')
        print(f'KMP: {kmp_2.search_with_time(pattern)}')
        print(f'Rabin-Karp: {rk_2.search_with_time(pattern)}')
        print()