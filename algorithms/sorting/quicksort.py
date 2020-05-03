def partition(array, start, end):
    pivot = array[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= right and array[right] >= pivot:
            right = right - 1

        while left <= right and array[left] <= pivot:
            left = left + 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            print('Elements swapped')
            print(array)
        else:
            break
    print('Right is', right)
    array[start], array[right] = array[right], array[start]
    print(array)
    return right


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


def quicksort2(array, start, end):
    if start >= end:
        return

    p = partition2(array, start, end)
    quicksort2(array, start, p-1)
    quicksort2(array, p+1, end)


def partition2(array, start, end):
    pivot = array[start]
    low = start+1
    high = end

    while low <= high:

        while low <= high and array[high] >= pivot:
            high = high - 1

        while high >= low and array[low] <= pivot:
            low = low + 1

        if high >= low:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


array = [10, 15, 19, 2, 3, 6, 9, 25, 7]
# p = partition(array, 0, len(array)-1)

quicksort2(array, 0, len(array)-1)

print(array)







