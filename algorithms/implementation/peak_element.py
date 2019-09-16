class Solution:
    def find_peak_element(self, arr) -> int:

        if len(arr) == 2:
            if arr[1] > arr[0]:
                return 1
            else:
                return 0

        for i in range(1, len(arr) - 1):

            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i
        if len(arr) > 2:
            if arr[-1] > arr[-2]:
                return len(arr) - 1
        return 0
