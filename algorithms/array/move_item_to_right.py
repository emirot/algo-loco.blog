
def move_item_to_right(arr, val):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == val:
            for j in range(i, len(arr)-1):
                if arr[j + 1] != val:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    a = [9, 12, 3, 2, 3]
    assert move_item_to_right(a, 3) == [9, 12, 2, 3, 3]
    a = [1, 2, 3, 2, 5, 2, 6]
    assert move_item_to_right(a, 2) == [1, 3, 5, 6, 2, 2, 2]
    a = [2, 2, 1, 2, 3, 2, 5, 2, 6]
    assert move_item_to_right(a, 2) == [1, 3, 5, 6, 2, 2, 2, 2, 2]
