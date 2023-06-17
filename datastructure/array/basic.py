import array

if __name__ == "__main__":
    arr = array.array('i', [1, 2, 3])

    for i in arr:
        print(i, end=" ")
    print("\r")

    # append new value
    arr.append(4)
    # insert(position, value)
    arr.insert(2, 5)

    # after append
    for i in arr:
        print(i, end=" ")
    print("\r")

    # remove
    # pop(position) return pop element
    arr.pop(2)

    # remove(value)
    arr.remove(1)

    # after remove
    for i in arr:
        print(i, end=" ")
    print("\r")

    # index(value)
    print(arr.index(2))

    arr.reverse()

    # after reverse
    for i in arr:
        print(i, end=" ")
    print("\r")
