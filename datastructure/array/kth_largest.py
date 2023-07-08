"""K'th Smallest/Largest Element in Unsorted Array"""
from array import array


def find_kth_element(items: array, n: int, how: str) -> int:
    """Return the kth smallest element"""
    if how == 'smallest':
        sorted_items = sorted(items)
    else:
        sorted_items = sorted(items, reverse=True)
    return sorted_items[n]


if __name__ == "__main__":
    arr = array('i', [7, 10, 4, 3, 20, 15])
    print(find_kth_element(arr, 3, 'smallest'))  # output: 10
    print(find_kth_element(arr, 1, 'largest'))  # output: 15
