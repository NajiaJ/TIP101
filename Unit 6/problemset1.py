# python3 problemset1.py

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
    frequent = {}

    current = head

    while current:
        if current.value in frequent:
            frequent[current.value] += 1
        else:
            frequent[current.value] = 1
    
        current = current.next
    
    for number, count in frequent.items():
        if number == val:
            return count
        

# head = Node(3, Node(1, Node(2, Node(1))))
# print(count_element(head, 1))

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
    while current.next.next: # used to be current.next
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

# head = Node(1, Node(2, Node(3, Node(4))))
# remove_tail(head)
# print_list(head)

def find_middle_element(head):
	pass