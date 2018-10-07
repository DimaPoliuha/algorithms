
array = [9, 8, 7, 0, 4, 3, 6, 5, 1, 2, 3]


def sort(array):
    swap = True
    while swap:
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                swap = True


def search(x, array):
    if len(array):
        print(array)
        mid = int(len(array) / 2)
        if x == array[mid]:
            return True
        elif x < array[mid]:
            search(x, array[:mid])
        elif x > array[mid]:
            search(x, array[mid:])
        else:
            return False
    else:
        return False


sort(array)
print(search(9, array))
