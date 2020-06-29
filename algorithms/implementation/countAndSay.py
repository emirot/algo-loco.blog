class Solution:
    
    
    
    def countAndSay(self, n: int) -> str:
        s = ""
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        if n > 2:
            s = "11"
        new_s = ""
        l = ""
        for _ in range(2, n):
            i = 0
            new_s = ""
            while i <= len(s) - 1:
                count = 1
                # if i < len(s):
                #     print(s[i])
                if i + 1 <= len(s) - 1 and s[i] == s[i+1]:
                    while i + 1 <= len(s) -1 and s[i] == s[i+1]:
                        l = s[i]
                        count += 1
                        i += 1
                    new_s += str(count) + l
                elif i + 1 <= len(s)-1 and s[i] != s[i+1]:
                    new_s += str(1) + s[i]
                elif i == len(s)-1:
                    new_s += str(1) + s[i]
                i += 1
            s = new_s
        return s
