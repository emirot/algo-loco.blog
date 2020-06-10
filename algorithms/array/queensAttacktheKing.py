class Solution:
    
    def queensAttacktheKing(self, queens, king):
        row = 8
        col = 8
        
        arr = []
        res = []
        
        for i in range(8):
            arr.append([0 for i in range(8)])
        for q in queens:
            arr[q[0]][q[1]] = 1

        # up left
        row = king[0]
        col = king[1]
        while row >= 0 and col >=0:
            if arr[row][col] == 1:
                res.append([row,col])
                break
            row -= 1
            col -=1 
        # up
        row = king[0]
        col = king[1]
        while row >= 0:
            if arr[row][col] == 1:
                res.append([row,col])
                break
            row -=1
        
        # up right
        row = king[0]
        col = king[1]
        while col < 8 and row >= 0:

            if arr[row][col] == 1:
                res.append([row,col])
                break
            row -=1
            col += 1
        
        # right
        row = king[0]
        col = king[1]
        while col < 8:
            if arr[row][col] == 1:
                res.append([row, col])
                break
            col +=1

        # Down right
        row = king[0]
        col = king[1]
        while row < 8 and col < 8:
            if arr[row][col] == 1:
                res.append([row,col])
                break
            row += 1
            col += 1
        # Down
        row = king[0]
        col = king[1]
        while row < 8:
            if arr[row][col] == 1:
                res.append([row,col])
                break
            row +=1
        
        # Down left
        row = king[0]
        col = king[1]
        while row < 8 and col >= 0:
            if arr[row][col] == 1:
                res.append([row, col])
                break
            row += 1
            col -= 1
        # left
        i = king[1]
        while i >= 0:
            if arr[king[0]][i] == 1:
                res.append([king[0], i])
                break
            i -= 1
        return sorted(res)
