# Version 1

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# node1 = TreeNode(10)
# node2 = TreeNode(4)
# node3 = TreeNode(6)

# node1.left = node2
# node1.right = node3

def check_tree(root):
    if not root.left and not root.right:
        return False

    total = root.left.val + root.right.val

    if total == root.val:
        return True
    else:
        return False

# print(check_tree(node1))

def check_tree_2(root):
    if root.left and not root.right:
        if root.left.val == root.val:
            return True
    
    if root.right and not root.left:
        if root.right.val == root.val:
            return True
    
    if root.left and root.right:
        if root.left.val + root.right.val == root.val:
            return True

    return False

# node1 = TreeNode(5)
# node2 = TreeNode(3)
# node3 = TreeNode(2)

# node1.left = node2
# node1.right = node3
# print(check_tree_2(node1))

def left_most(root):
    curr = root

    while curr.left is not None:
        curr = curr.left
    
    return curr.val

# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(5)
# node4 = TreeNode(4)
# node5 = TreeNode(3)

# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node3
# print(left_most(node1))

def left_most_recursively(root):
    if root.left is None:
        return root.val
    
    return left_most_recursively(root.left)

# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(5)
# node4 = TreeNode(4)
# node5 = TreeNode(3)

# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node3
# print(left_most_recursively(node1))

def inorder_traversal(root):
    list = []

    if root is None:
        return list
    
    list.extend(inorder_traversal(root.left))
    list.append(root.val)
    list.extend(inorder_traversal(root.right))

    return list

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
print(inorder_traversal(root))

def size(root):
    nodes = inorder_traversal(root)
    total_nodes = 0

    for node in nodes:
        total_nodes += 1
    
    return total_nodes

#print(size(node1))

def find(root, value):
    # nodes = inorder_traversal(root)

    # for node in nodes:
    #     if node == value:
    #         return True
    
    # return False

    if not root:
        return False
    
    if root.val == value:
        return True

    return find(root.left, value) or find(root.right, value)

#print(find(node1, 10))

def find_bst(root, value):
    if not root:
        return False
    
    if root.val == value:
        return True
    
    if value < root.val:
        return find(root.left, value)
    else:
        return find(root.right, value)

#print(find_bst(node1, 5))

# Version 2

# root = TreeNode(10)
# root.left = TreeNode(2)
# root.right = TreeNode(5)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(4)

def check_tree_product(root):
    if root.left.val * root.right.val == root.val:
        return True
    
    return False

# print(check_tree_product(root))

def check_tree_product_2(root):
    if root == None:
        return False

    if root.left and root.right:
        if root.left.val == root.val or root.right.val == root.val:
            return False
    
    if root.left and root.right:
        if root.left.val * root.right.val == root.val:
            return True
    
    return False

#print(check_tree_product_2(root))

def right_most(root):
    if root == None:
        return curr.val

    curr = root

    while curr.right is not None:
        curr = curr.right
    
    return curr.val

#print(right_most(root))

def postorder_traversal(root):
    list = []

    if root is None: # empty list
        return list

    list.extend(postorder_traversal(root.left))
    list.extend(postorder_traversal(root.right))
    list.append(root.val)

    return list

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(6)
#print(postorder_traversal(root))

def preorder_traversal(root):
    list = []
    if root is None: # empty list
        return list
    
    list.append(root.val)
    list.extend(preorder_traversal(root.left))
    list.extend(preorder_traversal(root.right))
    
    return list

#print(preorder_traversal(root))