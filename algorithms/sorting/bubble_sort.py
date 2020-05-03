

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


data = [1, 8, 3, 90, 34, 18, 23]
data2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(bubble_sort(data))


def bubble_sort2(arr):

    for i in range(len(arr)):
        loop_len = len(arr)-i-1
        print(loop_len)
        for j in range(loop_len):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

    return arr


print(bubble_sort2(data2))
