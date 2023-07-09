"""Sort an array of 0s, 1s and 2s | Dutch National Flag problem"""
from array import array


if __name__ == "__main__":
    arr = array('i', [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
    print(sorted(arr))

