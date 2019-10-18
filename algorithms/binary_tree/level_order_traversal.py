class Solution:
    def level_order(self, root):
        queue = [[root, 0]]
        res = []
        if not root:
            return []
        while queue:
            node, depth = queue.pop(0)
            res.append([node.val, depth])
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])

        max_val = max([e[1] for e in res])
        arr = [[] for i in range(0, max_val + 1)]
        for e in res:
            arr[e[1]].append(e[0])
        return arr
