class BinaryTree:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def serialize_binary_tree(root, st):
    if root is None:
        st.append(-1)
        return None
    st.append(root.val)
    serialize_binary_tree(root.left, st)
    serialize_binary_tree(root.right, st)
    return st


def deserialize_binary_tree(arr):
    if len(arr) < 1 or arr[0] == -1:
        arr.pop(0)
        return None
    val = arr.pop(0)
    root = BinaryTree(val)
    root.left = deserialize_binary_tree(arr)
    root.right = deserialize_binary_tree(arr)
    return root


if __name__ == "__main__":
    bt = BinaryTree(2)
    bt.right = BinaryTree(3)
    bt.left = BinaryTree(5)
    bt.right.right = BinaryTree(4)
    bt.left.left = BinaryTree(1)
    bt.left.right = BinaryTree(0)
    arr = serialize_binary_tree(bt, [])
    print(arr)
    bt = deserialize_binary_tree(arr)

