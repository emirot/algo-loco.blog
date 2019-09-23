class Solution:
    
    def traverse(self, root):
        if not root:
            return False 
        queue = [root]
        val = root.val
        count = 0
        if root.left is None and root.right is None:
            return True
        
        while queue:
            node = queue.pop(0)

            if node and node.val != val:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return True
            
        
    
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        queue = [root]
        count = 0
        while queue:
            node = queue.pop(0)
            count += self.traverse(node)
            if node and  node.left:
                queue.append(node.left)
            if node and node.right:
                queue.append(node.right)
                
        return count 
