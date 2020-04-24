ass Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        print(len(mat))
        for col in range(len(mat[0])):
            r = 0
            c = col
            arr = []
            while r < len(mat) and c < len(mat[0]):
                arr.append(mat[r][c])
                r += 1
                c += 1
            r = 0
            c = col
            arr.sort()
            print(arr)
            while r < len(mat) and c < len(mat[0]):
                if len(arr):
                    mat[r][c] = arr.pop(0)
                    r += 1
                    c += 1
                    
        for row in range(1, len(mat)):
            r = row
            c = 0
            arr = []
            while r < len(mat) and c < len(mat[0]):
                arr.append(mat[r][c])
                r += 1
                c += 1
            r = row
            c = 0
            arr.sort()

            while r < len(mat) and c < len(mat[0]):
                if len(arr):
                    mat[r][c] = arr.pop(0)
                r += 1
                c += 1
               
        return mat
