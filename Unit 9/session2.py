# Problem Set V1
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    if not root:
    # return an empty list
        return []

    # Create an empty queue using deque
    queue = deque()
    # Create an empty list to store the explored nodes
    explored = []

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    while queue:
    # Pop the next node off the queue (pop from the left side!)
        popped_ele = queue.popleft()
    # Add the popped node to the list of explored nodes
        explored.append(popped_ele.val)
    # Add each of the popped node's children to the end of the queue
        if popped_ele.left is not None:
            queue.append(popped_ele.left)
        if popped_ele.right is not None:
            queue.append(popped_ele.right)

    # Return the list of visited nodes
    return explored

# root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
# print(level_order(root))

def min_depth(root):
    if not root:
        return 0
    
    if root.left is None and root.right is None:
        return 1

    queue = deque()
    queue.append((root,1))

    while queue:
        popped, depth = queue.popleft()

        if popped.left is None and popped.right is None:
            return depth
        
        if popped.left is not None:
            queue.append((popped.left, depth + 1))
        
        if popped.right is not None:
            queue.append((popped.right, depth + 1))
    
    return 0

# root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# print(min_depth(root))

def level_difference(root):
    if not root:
        return []
    
    queue = deque()
    queue.append((root,1))

    odd_sum = 0
    even_sum = 0

    while queue:
        popped, level = queue.popleft()
    
        if level % 2 == 0:
            even_sum += popped.val
        else:
            odd_sum += popped.val
        
        if popped.left is not None:
            queue.append((popped.left, level + 1))
        
        if popped.right is not None:
            queue.append((popped.right, level + 1))
    
    difference = odd_sum - even_sum

    return difference

# root = TreeNode(6, TreeNode(3, TreeNode(5), None), TreeNode(8, TreeNode(4, TreeNode(1), TreeNode(7)), TreeNode(2, None, TreeNode(3))))
# print(level_difference(root))

def level_order(root):
    if not root:
        return []

    queue = deque()
    explored = []

    queue.append(root)

    while queue:
        level_size = len(queue)
        level_nodes = []

        for i in range(level_size):
            popped_ele = queue.popleft()
            level_nodes.append(popped_ele.val)

            if popped_ele.left is not None:
                queue.append(popped_ele.left)
            if popped_ele.right is not None:
                queue.append(popped_ele.right)
        
        explored.append(level_nodes)

    return explored

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order(root))