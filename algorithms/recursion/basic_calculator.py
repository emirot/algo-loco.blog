class Solution:
    
    def calc(self, s):
        s = s.strip()
        s = s.replace(' ', '')
        s = s.replace('--', '+')
        try: 
            int(s)
            return str(s)
        except:
            pass
    #        print('')
        res = 0
        queue = []
        i = 0
        while i < len(s):
            tmp = ""
            while i < len(s) and s[i] in ['0','1','2','3','4','5','6','7','8','9']:
                tmp += s[i]
                i += 1
            else:
#                print("[{}]".format(tmp))
                if tmp:
                    queue.append(int(tmp))
            if i < len(s) and s[i] in ['+', '-']:
                queue.append(s[i])
            else:
                i += 1
            i += 1
        #print('q', queue)
        first = True
        add = True
        sub = False
        while queue:
            n = queue.pop(0)
            #print(n)
            if first:
                res = n
                first = False
                continue
            if str(n) == '+':
                add = True
                sub = False
                continue
            elif str(n) == '-':
                add = False
                sub = True
                continue
            if n and add:
                res += n
            if n and sub:
                res -= n
        #print("res", res)
        return str(res)
    
    def calculate(self, s: str) -> int:

        if not '(' in s:
            return self.calc(s)
        else:
            i_l = s.rfind('(')
            tmp_s = s[i_l:]
            i_r = tmp_s.find(')')
            new_s = tmp_s[:i_r+1]
            new_s = new_s[1:]
            new_s = new_s[:-1]
            s = s[:i_l] + self.calculate(new_s) + s[ i_l + i_r +1:]
            return self.calculate(s)
            
        
        
