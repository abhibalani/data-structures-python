# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
#
# data = [1, 8, 3, 90, 34, 18, 23]
#
# print(selection_sort(data))
#
#
# data2 = [44, 12, 122, 90, 34, 18, 23]
#
#
# def selection_sort2(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         print(arr)
#
#     return arr
#
#
# print(selection_sort2(data2))
#
#
#
#
