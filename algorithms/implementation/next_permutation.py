class Solution:
 
    # 1, 2, 3
    # 1 ,3 ,2
    def get_next_permutation(self, n, len_n):
        i = len_n -1
        x = 0
        while i > 0:
            if n[i-1] < n[i]:
                x = i-1
                break
            i -= 1
        j = len_n -1
        y = 0
        while j > 0:
            if n[x] < n[j]:
                y = j
                break
            j -=1
        n[x], n[y] = n[y], n[x]
        n = n[:x+1] + n[x+1:][::-1]
        return n
    
    def getPermutation(self, n: int, k: int) -> str:
        m = n
        n = [i for i in range(1, n + 1)]
        i = 0
        len_n = len(n)
        # get next permutation
        while i < (k-1):
            n = self.get_next_permutation(n, len_n)
            i += 1
        return "".join([str(e) for e in n])
        
