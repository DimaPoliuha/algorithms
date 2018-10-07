
array = [9, 8, 7, 0, 4, 3, 6, 5, 1, 2, 3]


def sort(array):
    for i in range(1, len(array)):
        t = array[i]
        index = i
        for j in range(i):
            if array[index] < array[j]:
                index = j
        k = i
        while k > index + 1:
            array[k] = array[k - 1]
            k -= 1
        array[index] = t



    # for i in range(1, len(array)):
    #     index = i
    #     for j in range(i):
    #         if array[i] < array[j]:
    #             index = j
    #     temp = array[index]
    #     array[index] = array[i]
    #     for k in range(index + 2, i):
    #         array[k - 1] = temp
    #         temp = array[k]


sort(array)
print(array)