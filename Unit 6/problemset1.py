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

# ANOTHER WAY OF DOING IT
def count_element(head, val):
    count = 0

    current = head

    while current:
        if current.value == val:
            count += 1
    
        current = current.next

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
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next # slow pointer moves 1
        fast = fast.next.next # fast pointer moves 2

    return slow.value

# head = Node(1, Node(2, Node(3, Node(4)))) # linked list is even returns 2nd middle node
# head = Node(1, Node(2, Node(3))) # linked list is odd returns middle node
# print(find_middle_element(head))

def is_palindrome(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next # slow pointer moves 1
        fast = fast.next.next # fast pointer moves 2
    
    prev = None
    curr = slow

    while curr:
        new_node = curr.next
        curr.next = prev
        prev = curr
        curr = new_node

    first_half = head
    second_half = prev

    while second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

def reverse(head):
    curr = head
    prev = None

    #basic way to reverse linked lists
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

# head = Node(1, Node(2, Node(3, Node(4))))
# print_list(head)
# head = reverse(head)
# print_list(head)

