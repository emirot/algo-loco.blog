

def kadane(arr):
    new_arr = [0 for i in range(len(arr))]
    new_arr[0] = arr[0]
    max_so_far = 0
    for i in range(1, len(arr)):
        max_so_far = max(new_arr[i-1] + arr[i], arr[i])
        new_arr[i] = max_so_far
    print(new_arr)
    print(arr)
    return max(new_arr)


if __name__ == "__main__":
    arr = [5, 7, -3, 2, 9, -14, 10, -28, 12]
    kadane(arr)
    arr = [-2, -3, 4,  -1, -2, 1, 5, -3]
    assert kadane(arr) == 7
