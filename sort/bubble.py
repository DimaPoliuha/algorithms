
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


sort(array)
print(array)
