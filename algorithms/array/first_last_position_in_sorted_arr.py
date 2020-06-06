class Solution:
    
    def binary_search(self, nums, target): 
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            if target == nums[0]:
                return [0,0]
        r  = self.binary_search(nums, target)
        if r == -1:
            return [-1,-1]
        left = r
        right = r
        while left >= 0:
            if nums[left] != target:
                left += 1
                break
            left -= 1

        while right < len(nums):
            if nums[right] != target:
                right -= 1
                break
            right += 1
        if right == len(nums):
            right -=1
        if left < 0:
            left = 0
        return [left, right]
