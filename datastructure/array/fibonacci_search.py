"""
    Same as binary search work on sorted array.
    Difference with binary search:
        - binary search uses a division operator to divide range. Fibonacci search doesn't use divide(/) operator,
          but use plus(+) and minus(-) operator.
        - When the input array is big that can't fid in CPU cache or even in RAM.

    # Time complexity: O(log N)
    # Space complexity: O(1)
"""
from array import array


def fibonacci_search_iter(li: array, key: int) -> int:
    n = len(li)
    fib1, fib2 = 0, 1
    fib3 = fib1 + fib2

    # smallest fibonacci number greater that or equal to n
    while fib3 < n:
        fib1, fib2 = fib2, fib3
        fib3 = fib1 + fib2

    # init variables for the current and previous split point
    offset = -1
    while fib3 > 1:
        i = min(offset + fib2, n - 1)

        # if key is greater that the value at index i, move the split to the right
        if li[i] < key:
            fib3, fib2 = fib2, fib1
            fib1 = fib3 - fib2
            offset = i
        # if key is less than the value at index i, move the split to the left
        elif li[i] > key:
            fib3 = fib1
            fib2 = fib2 - fib1
            fib1 = fib3 - fib2
        # if key is equal to the value at index i, return the index
        else:
            return i

    # if key is not found in the array, return -1
    if fib2 == 1 and li[offset+1] == key:
        return offset + 1
    return -1


if __name__ == "__main__":
    arr = array('I', [10, 22, 35, 40, 46, 51, 72, 89, 99, 102, 321])
    x = 99

    index = fibonacci_search_iter(arr, x)
    if index != -1:
        print(f"Key found at index: {index}")
    else:
        print("Key not found")
