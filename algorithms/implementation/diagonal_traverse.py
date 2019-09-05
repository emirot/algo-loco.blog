from itertools import chain

def diagonal_traverse(arr):
    res = []
    for i in range(0, len(arr)):
        tmp = []
        j = 0
        z = i
        while z >= 0 and j < len(arr[0]):
            tmp.append(arr[z][j])
            z -= 1
            j += 1
        res.append(tmp)

    for j in range(1, len(arr[0])):
        tmp = []
        z = len(arr) - 1
        i = j
        while z >= 0 and i < len(arr[0]):
            tmp.append(arr[z][i])
            z -= 1
            i += 1
        res.append(tmp)

    diagonal_res = []
    for i, a in enumerate(res):
        if i % 2 != 0:
            diagonal_res.append(a[::-1])
        else:
            diagonal_res.append(a)
    return list(chain(*diagonal_res))


if __name__ == "__main__":
    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    r = diagonal_traverse(arr)
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    r = diagonal_traverse(arr)
    print(r)
