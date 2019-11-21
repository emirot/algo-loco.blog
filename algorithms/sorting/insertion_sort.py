
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


if __name__ == '__main__':
    arr = [3, 6, 1, 2]
    assert insertion_sort(arr) == sorted(arr)
    arr = [3, 6, 19, 1]
    assert insertion_sort(arr) == sorted(arr)
