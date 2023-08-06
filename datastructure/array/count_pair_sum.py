"""
    Count pairs with given sum
"""
from array import array


def find_pairs_iter2x(items: array, sm: int):
    count = 0
    for i in range(0, len(items)):
        for j in range(i+1, len(items)):
            if items[i] + items[j] == sm:
                count += 1
    print(f"Count of pair: {count}")


if __name__ == "__main__":
    arr = array('i', [1, 5, 7, -1])
    find_pairs_iter2x(arr, 6)
