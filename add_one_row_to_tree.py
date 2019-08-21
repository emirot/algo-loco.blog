# Definition for a binary tree node.
# https://gist.github.com/146c3c664b7bab8231838d013509bd5a

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        queue = [[root, 1]]
        process_queue = []
    
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        while queue:
            node, depth = queue.pop(0)
            if depth == d - 1:
                process_queue.append(node)
            if node.right:
                queue.append([node.right, depth+1])
            if node.left:
                queue.append([node.left, depth+1])
        
        while process_queue:
            node = process_queue.pop(0)
            left, right = node.left, node.right
            node.left = TreeNode(v)
            node.right = TreeNode(v)
            node.left.left, node.right.right = left, right
        return root