"""Count number of frequency in a sorted array"""
from array import array
from collections import Counter


def find_number_frequency_builtin(items: array, k: int) -> int:
    return Counter(items).get(k)


def find_number_frequency_iter(items: array, k: int) -> int:
    count = 0

    for item in items:
        if item == k:
            count += 1

    return count


if __name__ == "__main__":
    arr = array('i', [1, 1, 2, 2, 2, 2, 3])
    print(find_number_frequency_iter(arr, 2))
    print(find_number_frequency_builtin(arr, 1))
