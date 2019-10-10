def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if num == arr[mid]:
            return True
        elif num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


if __name__ == "__main__":
    res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 20], 3)
    assert res == True
    res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 20], -1)
    assert res == False
    res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 20], 12)
    assert res == True
    res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 20], 22)
    assert res == False
    res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 20], 2)
    assert res == True
    res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 20], 20)
    assert res == True

