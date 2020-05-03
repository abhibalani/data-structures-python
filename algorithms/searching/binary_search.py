

def binary_search(value, arr, start, end):
    if end >= start:
        mid = start + (end - 1) // 2
        if arr[mid] == value:
            print('Value found')
            return mid
        elif value > arr[mid]:
            binary_search(value, arr, mid+1, end)
        else:
            binary_search(value, arr, start, mid-1)
    else:
        print('Value not found')
        return -1


def binary_search2(value, arr, start, end):
    """Iterative approach"""
    while start >= end:
        mid = start + end - 1 // 2

        if arr[mid] == value:
            print('Value found')
            return mid
        elif arr[mid] > value:
            end = mid-1
        else:
            start = mid+1

    print('Value not found')
    return -1


arr = [1, 4, 6, 9, 11, 15, 16, 24]

binary_search(24, arr, 0, len(arr))
binary_search2(2, arr, 0, len(arr))
