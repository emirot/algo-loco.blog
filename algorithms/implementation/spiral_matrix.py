class Solution:
    def get_direction(self, n):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return directions[n % 4]

    def out_of_bound(self, row, col, arr):
        if row >= len(arr) or row < 0:
            return True
        if col >= len(arr[0]) or col < 0:
            return True

        return False

    def generate_matrix(self, n):
        arr = [[-1 for e in range(n)] for i in range(n)]
        row = 0
        col = 0
        next_dir = 0
        r, c = self.get_direction(next_dir)
        for i in range(1, (n * n) + 1):
            if self.out_of_bound(row + r, col + c, arr) or arr[row + r][col + c] != -1:
                next_dir += 1
                r, c = self.get_direction(next_dir)
            arr[row][col] = i
            row += r
            col += c
        return arr
