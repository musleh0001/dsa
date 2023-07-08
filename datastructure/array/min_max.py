"""Find maximum and minimum of an array"""
import sys
from array import array


class MaxMinPair:
    def __init__(self, items: array):
        self.items = items
        self.min = sys.float_info.max
        self.max = sys.float_info.min

    def using_builtin(self):
        self.min = min(self.items)
        self.max = max(self.items)

    def using_sorting(self):
        items = sorted(self.items)
        self.min = items[0]
        self.max = items[-1]

    def using_linear_search(self):
        for i in self.items:
            if i > self.max:
                self.max = i
            elif i < self.min:
                self.min = i

    def reset_value(self):
        self.min = sys.float_info.max
        self.max = sys.float_info.min

    def __str__(self):
        return f"Maximum: {self.max}\nMinimum: {self.min}"


if __name__ == "__main__":
    arr = array('i', [23, 34, 12, 76, 1, 90])
    maxmin = MaxMinPair(arr)

    maxmin.using_builtin()
    print(maxmin)
    maxmin.reset_value()

    maxmin.using_sorting()
    print(maxmin)
    maxmin.reset_value()

    maxmin.using_linear_search()
    print(maxmin)
