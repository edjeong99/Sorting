# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) / 2])
        right = merge_sort(arr[len(arr) / 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, end - start):
        if start >= mid:    # all elements in arrA have been merged
            arr[i], arr[mid+1] = arr[mid+1], arr[i]
            mid += 1
        elif mid+1 >= end:  # all elements in arrB have been merged
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
        elif arr[start] < arr[mid+1]:  # next element in arrA smaller, so add to final array
            arr[i] = arr[start]
            start += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            arr[i] = arr[mid + 1]
            mid += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l < r:
        middle = (l + r) // 2
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)
        merge_in_place(arr, l, middle, r)
    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION


def quick_sort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return (i)


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(quick_sort(arr1, 0, len(arr1)-1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
