class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

# head = Node(1, Node(2, Node(3, Node(4))))
# print_list(head)
# remove_tail(head)
# print_list(head)

def is_palindrome(head):
    slow = head
    fast = head

    # find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # reverse second half
    prev = None
    curr = slow
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # compare first and reversed second half
    first_half = head
    second_half = prev

    while second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

head = Node(1, Node(2, Node(1)))
print(is_palindrome(head))