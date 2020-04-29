
def merge_sorted_arr(left, right):
    i = 0
    j = 0
    new_arr = []
    while j < len(right) and i < len(left):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        elif right[j] <= left[i]:
            new_arr.append(right[j])
            j += 1
    while i < len(left):
        new_arr.append(left[i])
        i += 1
    while j < len(right):
        new_arr.append(right[j])
        j += 1
    return new_arr


def merge_sort(arr):
    if len(arr) <= 2:
        return arr
    pivot = len(arr) // 2
    left = merge_sort(arr[:pivot])
    right = merge_sort(arr[pivot:])

    return merge_sorted_arr(left, right)


if __name__ == "__main__":
    assert merge_sorted_arr([1, 3, 5], [2, 4, 12]) == [1, 2, 3, 4, 5, 12]
    assert merge_sort([1, 3, 4, 5, 0, 2, 19, 6, 29]) == sorted([1, 3, 4, 5, 0, 2, 19, 6, 29])
