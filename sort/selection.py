
array = [9, 8, 7, 0, 4, 3, 6, 5, 1, 2, 3]


def sort(array):
    swap = False
    for i in range(len(array)):
        index = i
        for j in range(i, len(array)):
            if array[j] < array[index]:
                index = j
                swap = True
        if swap:
            temp = array[i]
            array[i] = array[index]
            array[index] = temp
            swap = False


sort(array)
print(array)
