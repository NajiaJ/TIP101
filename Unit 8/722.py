class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# create root node
root = TreeNode(13)

# create left subtree
root.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)

# create right subtree
root.right = TreeNode(21)
root.right.left = TreeNode(15)
root.right.right = TreeNode(24)
root.right.right.right = TreeNode(26)

def insertion(root, key):
    # base case -> empty tree, create a new node with key and return
    if root is None:
        return TreeNode(key)
    else:
        # if key is greater than current node value -> insert in right subtree
        if root.value < key:
            root.right = insertion(root.right, key)
        # if key is less than current node value -> insert in left subtree
        else:
            root.left = insertion(root.left, key)
    #return the unchanged root node to maintain the tree structure
    return root

# deletion cases
    # node has no children (leaf) -> can just remove (by setting to null)
    # node has one child -> can replace the deleted node by setting its left/right root val to the node that we want there and set the deleted node to null
    # node has two children -> replace with its in order successor and swap and set to none