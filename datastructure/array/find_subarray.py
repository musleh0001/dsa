"""Find subarray with given sum"""
from array import array


def using_linear_search(items: array, exp_sum: int) -> list[int]:
    for index1, data1 in enumerate(items):
        current_sum = data1
        for index2 in range(index1+1, len(items)):
            current_sum += items[index2]
            if current_sum == exp_sum:
                return [index1, index2]
            elif current_sum > exp_sum:
                break
    return [-1]


if __name__ == "__main__":
    arr = array('i', [1, 4, 20, 3, 10, 5])
    expected_sum = 33
    print(using_linear_search(arr, expected_sum))
