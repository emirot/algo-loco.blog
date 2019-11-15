class BinaryTreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def merge_binary_trees(t1, t2):
    if t1 is None and t2 is None:
        return None
    if t1 is not None and t2 is None:
        return t1
    if t2 is not None and t1 is None:
        return t2
    if t1 is not None and t2 is not None:
        t1.val += t2.val
    t1.left = merge_binary_trees(t1.left, t2.left)
    t1.right = merge_binary_trees(t1.right, t2.right)
    return t1

def pre_order_tree(t1, arr):
    if t1 is None:
        return None
    arr.append(t1.val)
    pre_order_tree(t1.left, arr)
    pre_order_tree(t1.right, arr)
    return arr

if __name__ == '__main__':
    t1 = BinaryTreeNode(4)
    t1.left = BinaryTreeNode(5)
    t1.right = BinaryTreeNode(6)
    t1.left.left = BinaryTreeNode(1)
    t2 = BinaryTreeNode(6)
    t2.left = BinaryTreeNode(2)
    t2.right = BinaryTreeNode(3)
    t2.right.left = BinaryTreeNode(1)
    t2.right.right = BinaryTreeNode(9)
    t3 = merge_binary_trees(t1, t2)
    r = pre_order_tree(t3, [])
    assert r == [10, 7, 1, 9, 1, 9]

