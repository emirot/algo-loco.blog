class Solution:
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def is_balanced(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            lh = rh = 0
            if node and node.left:
                lh = self.height(node.left)
                queue.append(node.left)
            if node and node.right:
                rh = self.height(node.right)
                queue.append(node.right)
            if abs(lh - rh) > 1:
                return False

        return True
