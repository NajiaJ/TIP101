class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# create linked list: 2 -> 4 -> 8 -> 1 -> 3
head = Node(2, Node(4, Node(8, Node(1, Node(3)))))

# MULTIPLE PASS TECHNIQUE

# first pass: get the length
def get_length(head):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length

# second pass: get middle value
def find_middle(head):
    length = get_length(head)
    mid_index = length // 2
    curr = head
    for _ in range(mid_index):
        curr = curr.next
    
    return curr.value

print("length of list: ", get_length(head))
print("find middle value: ", find_middle(head))

# TEMPORARY HEAD TECHNIQUE

def remove_duplicates(head):
    # creation of temp and set it's next value to the head
    temp = Node(0)
    temp.next = head

    curr = head

    while curr and curr.next: # both need to exist
        if curr.value == curr.next.value:
            # skip duplicate node
            curr.next = curr.next.next
        else:
            curr = curr.next # moves to next unique element
    
    return temp.next

# Slow - Fast Pointer Technique

# create linked list: 1 -> 2 -> 2 -> 1
head = Node(1, Node(2, Node(2, Node(1))))

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
