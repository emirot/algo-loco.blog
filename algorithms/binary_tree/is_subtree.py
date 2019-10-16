class Solution:
    def isSame(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None and t2 is not None:
            return False
        if t2 is None and t1 is not None:
            return False
        if t1.val != t2.val:
            return False

        return self.isSame(t1.left, t2.left) and self.isSame(t1.right, t2.right)

    def isSubtree(self, s, t):
        queue = [s]
        while queue:
            s = queue.pop(0)
            if self.isSame(s, t):
                return True
            if s.left:
                queue.append(s.left)
            if s.right:
                queue.append(s.right)

        return False

