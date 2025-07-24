class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

# A binary tree is uni-valued if every node in the tree has the same value. 
# Given the root of a binary tree, return True if the given tree is uni-valued 
# and False otherwise.        
def is_univalued(root):
    if not root:
        return True

    stack = [root]
    value = root.val

    while stack:
        node = stack.pop()
        if node.val != value:
            return False
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return True

# root = TreeNode(1)
# root.left = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(1)
# root.right = TreeNode(1)
# root.right.right = TreeNode(1)

# print(is_univalued(root))

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right = TreeNode(5)
# print(height(root))

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right

def insert(root, key, value):
    if not root:
        return TreeNode(key, value)

    if key == root.key:
        root.val = value
    elif key < root.key:
        root.left = insert(root.left, key, value)
    else:
        root.right = insert(root.right, key, value)
    
    return root