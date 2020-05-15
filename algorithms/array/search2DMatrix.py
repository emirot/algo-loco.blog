class Solution:
    
    def find_range(self, arr, target):
        for i, e in enumerate(arr):
            if i != len(arr) -1:
                if i == 0 and target < e:
                    return -1
                if  target >= e and target < arr[i+1]:
                    return i
            if i == len(arr) -1 and e <= target:
                return i
        return -1
    
    def find_candidate_row(self, matrix, target):
        vertical = [matrix[i][0] for i in range(len(matrix))]
        return self.find_range(vertical, target)
    
    def find_column(self, matrix, target, row):
        left = 0
        right = len(matrix[0]) -1
        print(row)
        arr = matrix[row]

        while left <= right:
            mid = (left + right) //2
            if target == arr[mid]:
                return True
            if target < arr[mid]:
                right = mid - 1
            if target > arr[mid]:
                left = mid + 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or matrix == [[]]:
            return False
        r = self.find_candidate_row(matrix, target)
        if r == -1 or r is None:
            return False
        c = self.find_column(matrix, target, r)
        return c
        
        
