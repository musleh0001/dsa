"""
    Program to cyclically rotate an array by one.
"""
from array import array


def rotate_array(items: array) -> None:
    last_item = items[-1]
    for item in range(len(items) - 1, 0, -1):
        items[item] = items[item - 1]
    items[0] = last_item

    print(items)


if __name__ == "__main__":
    arr = array('i', [1, 2, 3, 4, 5])
    rotate_array(arr)
