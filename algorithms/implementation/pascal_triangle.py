def pascal_triangle(arr, current, num_rows):
    if current == num_rows:
        return arr
    if current < 2:
        pass
    else:
        new = [
                arr[current - 1][i - 1] + arr[current - 1][i]
                for i in range(1, len(arr[current - 1]))
            ]
        print("new", new)
        arr.append([1] + new + [1])
    return pascal_triangle(arr, current + 1, num_rows)


if __name__ == "__main__":
    arr = [[1], [1, 1]]
    arr = pascal_triangle(arr, 0, 1-1)
    print('a', arr)
