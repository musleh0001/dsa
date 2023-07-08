"""Find a peak element"""
from array import array


class FindPeak:
    def __init__(self, items: array):
        self.items = items

    def using_linear_search(self) -> int:
        for index, value in enumerate(self.items):
            if index == 0 and value > self.items[index+1]:
                return value
            if index == len(self.items) - 1 and value > self.items[index-1]:
                return value
            if self.items[index - 1] < value > self.items[index + 1]:
                return value


if __name__ == "__main__":
    arr = array('i', [10, 11, 15, 22, 23, 90, 97])

    find_peak = FindPeak(arr)
    print(find_peak.using_linear_search())
