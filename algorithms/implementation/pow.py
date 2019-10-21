class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            x = 1.0 / x
            n = abs(n)

        while n > 0:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                n -= 1
                res *= x
        return res
