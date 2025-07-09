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


def find_max(head):
    curr = head
    max_node = head.value

    while curr:
        if curr.value > max_node:
            max_node = curr.value
        
        curr = curr.next
    
    return max_node

# head = Node(6, Node(8, Node(5, Node(7))))
# print(find_max(head))

def remove_by_value(head, val):
    # Check if the list is empty
    if head is None:
        return head

    # If the node to be removed is the head of the list
    if head.value == val:
        return head.next

    # Initialize pointers
    current = head.next
    previous = head

    # Traverse the list to find the node to remove
    while current.next:
        if current.value == val:
            previous.next = current.next
            return head
        previous = current
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

# head = Node(1, Node(2, Node(3, Node(4))))
# print_list(head)
# remove_by_value(head, 3)
# print_list(head)

def middle_match(head, val):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if slow.value == val:
        return True

    return False

# head = Node(1, Node(2, Node(3)))
# print(middle_match(head, 2))
# head2 = Node(1, Node(2, Node(3, Node(4))))
# print(middle_match(head2, 2))

def get_loop_start(head):
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow.value

    return None

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create cycle: point node4.next back to node2
node4.next = node2

head = node1

print(get_loop_start(head))

def count_critical_points(head):
    curr = head.next
    prev = head
    crits = 0

    while curr and curr.next:
        next = curr.next
        if curr.value < next.value and curr.value < prev.value:
            crits += 1
        elif curr.value > next.value and curr.value > prev.value:
            crits += 1
        
        prev = curr
        curr = next

    return crits

# head = Node(1, Node(2, Node(3, Node(3, Node(3, Node(5, Node(1, Node(3))))))))
# print(count_critical_points(head))