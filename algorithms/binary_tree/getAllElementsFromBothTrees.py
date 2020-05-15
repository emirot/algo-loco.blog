class Solution:
    
    def get_all_elements(self, root, arr):
        
        if root is not None:
            self.get_all_elements(root.left, arr)
            arr.append(root.val)
            self.get_all_elements(root.right, arr)
        return arr
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr = []
        a1 = self.get_all_elements(root1, arr)
        arr2 = []
        a2 = self.get_all_elements(root2, arr2)
        return sorted(sorted(a1) + sorted(a2))
