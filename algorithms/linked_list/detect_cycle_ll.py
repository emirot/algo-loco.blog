class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        tmp = head
        mem = set()
        while tmp:
            if tmp in mem:
                return tmp
            else:
                mem.add(tmp)
            tmp = tmp.next
        return None
