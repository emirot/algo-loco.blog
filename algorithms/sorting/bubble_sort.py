def bubble_sort(arr):
    unsort = True
    while unsort:
        unsort = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                unsort = True
    return arr


if __name__ == "__main__":
    arr = [3, 2, 10, 1, 4, 5]
    res = bubble_sort(arr)
    assert bubble_sort(arr) == [1, 2, 3, 4, 5, 10]
