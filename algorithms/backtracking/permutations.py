
def permutation(arr, index):

    if index == len(arr):
        print(arr)
        return

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        permutation(arr, index + 1)
        arr[i], arr[index] = arr[index], arr[i]


if __name__ == "__main__":
    permutation(['a', 'b', 'c'], 0) 