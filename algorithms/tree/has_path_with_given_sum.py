# class Tree():
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


from copy import deepcopy

def check_sum(arr:list, s:int):
    
    if sum(arr) == s:
        return True
    return False


def has_path_with_given_sum(t, s):
    if not t:
        return False
    stack = [[t, [t.value]]]
    res = []
    
    
    while stack:
        node, path = stack.pop(0)
        
        if not node.left and not node.right:
            res.append(check_sum(path, s))
            path.pop()
        if node.left:
            p = []
            tmp_path = path + [node.left.value]
            p[:] = tmp_path
            stack.insert(0, [node.left, p])            
        if node.right:
            p = []
            tmp_path = path + [node.right.value]
            p[:] = tmp_path
            stack.insert(0, [node.right, p])

    if any(res):
        return True
    return False