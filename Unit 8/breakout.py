class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

list = []
def inorder_traversal(root):

    # base: if tree empty return None
    if not root:
        return []
    

    # base: if left node is None or 
        #else:
            #return

    inorder_traversal(root.left)
    list.append(root.val)
    inorder_traversal(root.right)

    return list

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(inorder_traversal(root))