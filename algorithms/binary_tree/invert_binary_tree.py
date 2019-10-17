class Solution:
    def invertTree(self, root):

        if not root:
            return

        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root