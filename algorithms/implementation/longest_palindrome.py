from collections import Counter


class Solution:
    def longestPalindrome(s):
        c = Counter(s)
        z = list(c.values())
        even = sum([e for e in z if e % 2 == 0])
        odd = [e for e in z if e % 2 != 0]

        res_odd = 0
        first = True
        for e in sorted(odd, reverse=True):
            if first:
                res_odd += e
                first = False
            else:
                res_odd += e - 1
        return even + res_odd
