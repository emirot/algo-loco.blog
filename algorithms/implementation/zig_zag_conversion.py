class Solution:
    def get_direction(self, next_dir):
        dirs = [(1, 0), (-1, 1)]
        return dirs[next_dir % 2]

    def out_of_bound(self, r, c, arr):
        if r < 0 or r >= len(arr):
            return True
        if c < 0 or c >= len(arr[0]):
            return True
        return False

    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        arr = [["" for i in range(len(s))] for i in range(numRows)]
        sl = list(s)
        next_dir = 0
        r, c = self.get_direction(next_dir)
        row = -1
        col = 0
        br = 0
        while sl:
            if self.out_of_bound(row + r, col + c, arr):
                next_dir += 1
                r, c = self.get_direction(next_dir)
            row += r
            col += c
            arr[row][col] = sl.pop(0)
            br += 1
        # print(*arr, sep='\n')
        return "".join(["".join(e) for e in arr])
