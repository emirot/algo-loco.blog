class Solution:
    def max_level_sum(self, root) -> int:
        d = {}
        queue = [[root, 0]]

        while queue:
            node, depth = queue.pop(0)
            if node and depth not in d:
                d[depth] = node.val
            elif node:
                d[depth] += node.val
            if node.left:
                queue.append([node.left, depth + 1])

            if node.right:
                queue.append([node.right, depth + 1])

        level = max(d, key=d.get)

        return level + 1
