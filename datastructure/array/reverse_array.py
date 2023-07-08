"""Write a program to reverse an array or string"""
from array import array


def reverse_using_builtin(items: array):
    items.reverse()
    print(f"Builtin reverse: {items}")


def reverse_iter(items: array, start_index: int, end_index: int) -> array:
    while start_index <= end_index:
        items[start_index], items[end_index] = items[end_index], items[start_index]
        start_index += 1
        end_index -= 1
    return items


def reverse_rec(items: array, start_index: int, end_index: int) -> array:
    if start_index >= end_index:
        return items
    items[start_index], items[end_index] = items[end_index], items[start_index]
    reverse_rec(items, start_index + 1, end_index - 1)


if __name__ == "__main__":
    arr = array('i', [1, 2, 3, 4, 5, 6, 7])
    reverse_using_builtin(arr.__copy__())
    print("Iterative reverse: ", reverse_iter(arr.__copy__(), 0, len(arr) - 1))
    reverse_rec(arr, 0, len(arr) - 1)
    print(f"Recursive reverse: {arr}")
