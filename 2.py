from random import random


def binary_search(arr, value):
    count = 0
    low = 0
    high = len(arr) - 1
    mid = 0

    if (value - arr[low]) < 0:
        return count, arr[low]

    if (value - arr[high]) > 0:
        return count, None

    while low <= high:
        count += 1
        mid = (high + low) // 2

        if (value - arr[mid]) > 0:
            low = mid + 1
        elif (value - arr[mid]) < 0:
            high = mid - 1
        else:
            return count, arr[mid]

    return count, arr[high + 1]


def rand():
    return random() / random()


def test_binary_search():
    arr = [rand() for _ in range(100)]
    arr.sort()

    for _ in range(10):
        value = rand()
        count, result = binary_search(arr, value)
        print(f'Value: {value}, Count: {count}, Result: {result}')


if __name__ == "__main__":
    # Test cases
    test_binary_search()
