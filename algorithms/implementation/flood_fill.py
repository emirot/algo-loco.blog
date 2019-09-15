def floodFill(image, r, c, new_color):
    get_val = image[r][c]
    lr = len(image)
    lc = len(image[0])
    queue = [[r, c]]
    saved = set()
    while queue:
        row, col = queue.pop(0)
        image[row][col] = new_color
        saved.add((row, col))
        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if (
                row + r < lr
                and row + r >= 0
                and col + c < lc
                and col + c >= 0
                and (row + r, col + c) not in saved
                and image[row + r][col + c] == get_val
            ):
                queue.append([row + r, col + c])

    return image