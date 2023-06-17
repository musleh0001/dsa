"""
    Linear Search is defined as a sequential search algorithm that starts at one end and goes through each
    element of a list until the desired element is found.

    # Time complexity: O(N)
    # Space complexity: O(1)
"""
import array


def linear_search(li: array, key: int) -> int:
    for idx, value in enumerate(li):
        if value == key:
            return idx
    return -1


if __name__ == "__main__":
    arr = array.array('I', [3, 10, 6, 20, 12, 8, 45, 9])
    x = 12

    index = linear_search(arr, x)
    if index != -1:
        print(f"Key found. Index is: {index}")
    else:
        print("Key not found")
