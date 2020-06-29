"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    
    def print_list(self, l):
        tmp = l
        while tmp:
            print(tmp.val,  tmp.random.val if tmp.random else None, end=",")
            tmp = tmp.next
        print("")
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        tmp = head
        n = Node(0)
        t = n
        d = {}
        while tmp:
            n.next = Node(tmp.val)
            d[tmp] = n.next
            tmp = tmp.next
            n = n.next
        tmp = head
        n = t.next
        while tmp:
            if tmp.random:
                n.random = d[tmp.random]
            tmp = tmp.next
            n = n.next

        return t.next
        
