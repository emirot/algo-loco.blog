

def in_square(matrix, row, col):
    if row > len(matrix) or row < 0:
        return False
    if col > len(matrix[0]) or col < 0:
        return False
    return True


def check_all(matrix, row, col, i):

    if in_square(matrix, row + i + 1, col + i+1):
        for i_row in range(row,  row + i + 1):
            for j_col in range(col, col + i + 1):
                print("check", i_row, j_col, matrix[i_row][j_col])
                if matrix[i_row][j_col] != 1:
                    return False
        return True
    return False


def maximal_square(matrix):
    c = 0
    found = False
    for row in range(len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == 1:
                found = True
                for i in range(1, len(matrix)):
                    if check_all(matrix, row, col, i):
                        current_count = i + 1
                        c = max(current_count, c)
                    else:
                        break
    if found:
        return max(1, c * c)
    return c * c


def maximal_square_dp(arr):
    new_arr = []
    tmp = []
    res = 0
    for row in range(0, len(arr)):
        tmp = []
        for col in range(0, len(arr[0])):
        tmp.append(arr[row][col])
        new_arr.append(tmp)

    for row in range(1, len(new_arr)):
        for col in range(1, len(new_arr[0])):
            if arr[row][col] == 1:
                val = min(new_arr[row-1][col], new_arr[row-1][col-1], new_arr[row][col-1])+1
                res = max(res, val)
                new_arr[row][col] = val
    return res * res


if __name__ == "__main__":
    print("start")
    # arr = [
    #     [1, 0, 1, 0, 0],
    #     [1, 0, 1, 1, 1],
    #     [0, 1, 1, 1, 1],
    #     [1, 0, 0, 1, 0]
    # ]
    # arr = [
    #       [1, 1, 1],
    #       [1, 1, 1],
    #       [0, 1, 1]
    # ]
    # maximal_square(arr)
    arr = [
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    # arr = [
    #     [1 , 1],
    #     [1 , 1]
    #     ]
    # arr = [[1, 0, 1, 0, 0],
    #        [1, 0, 1, 1, 1],
    #        [1, 1, 1, 1, 1],
    #        [1, 0, 0, 1, 0]]
    print(arr)
    arr = [[1,  0,  1,  0,  0],
           [1,  0,  1,  1,  1],
           [1,  1,  1,  1,  1], 
           [1,  0,  0,  1,  0]]
    #print('res', maximal_square(arr))
    print(maximal_square_dp(arr))
