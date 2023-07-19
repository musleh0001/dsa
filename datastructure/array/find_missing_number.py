"""
    Find the Missing Number
"""
from array import array


def find_missing(items: array, size: int) -> None:
    lookup = array('i', [0] * size)
    for item in items:
        lookup[item - 1] = 1

    for index, value in enumerate(lookup):
        if value == 0:
            print(f'Missing Number: {index + 1}')
            return
    print("No missing number")


def find_missing_another(items: array, size: int) -> None:
    for i in range(1, size+1):
        if i not in items:
            print(f"Missing Number: {i}")
            return
    print("No missing number")


def find_missing_sum(items: array, size: int) -> None:
    """
        Time complexity: O(N)
        Space complexity: O(1)
    """
    total = size * (size + 1) // 2
    sum_of_array = sum(items)
    print(f"Missing Number: {total - sum_of_array}")


if __name__ == "__main__":
    arr = array('I', [1, 2, 4, 6, 3, 7, 8])
    N = 8
    find_missing_sum(arr, N)
