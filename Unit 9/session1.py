class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_mirror(left, right):
    if not left and not right:
        return True
    
    if not left or not right:
        return False
    
    if left.val != right.val:
        return False
    
    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

def is_symmetric(root):
    if not root:
        return True
    
    return is_mirror(root.left, root.right)

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(root))

def binary_tree_paths(root):
	pass