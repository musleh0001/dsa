"""
    Binary search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search
    interval in half.

    # Time complexity: O(log N)
    # Space complexity: O(1)
"""
import array


def binary_search_iter(li: array, left: int, right: int, key: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2

        if li[mid] == key:
            return mid
        elif li[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_rec(li: array, left: int, right: int, key: int) -> int:
    # base case
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if li[mid] == key:
        return mid
    elif li[mid] < key:
        return binary_search_rec(li, mid + 1, right, key)
    else:
        return binary_search_rec(li, left, mid - 1, key)


if __name__ == "__main__":
    arr = array.array('I', [2, 3, 6, 7, 12, 65, 87])
    x = 7

    index = binary_search_rec(arr, 0, len(arr), x)
    if index != -1:
        print(f"Key found at index: {index}")
    else:
        print("Key not found")
