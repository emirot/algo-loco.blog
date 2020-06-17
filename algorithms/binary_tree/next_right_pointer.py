 Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    
    def connect(self, root: 'Node') -> 'Node':
        queue = [[root, 0]]
        dic = {0: [root]}
        while queue:
            node, depth = queue.pop(0)
            if depth + 1 not in dic:
                dic[depth+1] = []
            if node and node.left:
                queue.append([node.left, depth+1])
                dic[depth+1].append(node.left)
            if node and node.right:
                queue.append([node.right, depth+1])
                dic[depth+1].append(node.right)
        
        for k, v in dic.items():
            for i, e in enumerate(v):
                if i + 1 < len(v) :
                    v[i].next = v[i+1]
        return root
