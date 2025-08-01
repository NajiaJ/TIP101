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
        popped = queue.popleft()
    # Add the popped node to the list of explored nodes
        explored.append(popped.val)
    # Add each of the popped node's children to the end of the queue
        if popped.left is not None:
            queue.append(popped.left)
        if popped.right is not None:
            queue.append(popped.right)

    # Return the list of visited nodes
    return explored

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_order(root))