class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printInOrder(root):
    result = []

    # Left -> Root -> Right
    def inOrderHelper(node):
        nonlocal result
        if not node:
            return
    
        inOrderHelper(node.left)
        result.append(node.val)
        inOrderHelper(node.right)
    
    inOrderHelper(root)
    print(result)

print("InOrder Traversal")
tree = TreeNode(5, TreeNode(4, TreeNode(3)), TreeNode(8, TreeNode(7), TreeNode(9)))
printInOrder(tree) # [3, 4, 5, 7, 8, 9]

classTree = TreeNode(13, TreeNode(6, TreeNode(4), TreeNode(8)), TreeNode(21, TreeNode(15), TreeNode(24, None, TreeNode(26))))
printInOrder(classTree) # [4, 6, 8, 13, 15, 21, 24, 26]

def printPreOrder(root):
    result = []

    # Root -> Left -> Right
    def preOrderHelper(node):
        nonlocal result
        if not node:
            return

        result.append(node.val)
        preOrderHelper(node.left)
        preOrderHelper(node.right)
    
    preOrderHelper(root)
    print(result)

print("PreOrder Traversal")
tree = TreeNode(5, TreeNode(4, TreeNode(3)), TreeNode(8, TreeNode(7), TreeNode(9)))
printPreOrder(tree) # [5, 4, 3, 8, 7, 9]

classTree = TreeNode(13, TreeNode(6, TreeNode(4), TreeNode(8)), TreeNode(21, TreeNode(15), TreeNode(24, None, TreeNode(26))))
printPreOrder(classTree) # [13, 6, 4, 8, 21, 15, 24, 26]

def printPostOrder(root):
    result = []

    # Left -> Right -> Root
    def postOrderHelper(node):
        nonlocal result
        if not node:
            return

        postOrderHelper(node.left)
        postOrderHelper(node.right)
        result.append(node.val)
    
    postOrderHelper(root)
    print(result)

print("PostOrder Traversal")
tree = TreeNode(5, TreeNode(4, TreeNode(3)), TreeNode(8, TreeNode(7), TreeNode(9)))
printPostOrder(tree) # [3, 4, 7, 9, 8, 5]

classTree = TreeNode(13, TreeNode(6, TreeNode(4), TreeNode(8)), TreeNode(21, TreeNode(15), TreeNode(24, None, TreeNode(26))))
printPostOrder(classTree) # [4, 8, 6, 15, 26, 24, 21, 13]

# returns True if there is node that has this value in the tree
def findNode(root, value):
    if not root:
        return False
    
    if root.val == value:
        return True
    elif root.val < value:
        return findNode(root.right, value)
    else:
        return findNode(root.left, value)

print(findNode(classTree, 21))
print(findNode(classTree, 20))