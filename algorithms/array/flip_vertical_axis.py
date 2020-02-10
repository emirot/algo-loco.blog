def flip_vertical_axis(matrix):
    for row in range(len(matrix)):
        matrix[row] = matrix[row][::-1]
