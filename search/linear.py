
array = [9, 5, 4, 2, 7, 6, 1, 3, 8, 0]


def search(x, array):
    for i in range(len(array)):
        if array[i] == x:
            return True
    return False


print(search(input('Input number to search: '), array))
