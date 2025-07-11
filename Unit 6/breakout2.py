class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    curr = head
    first_node = head

    while curr and curr.next:
        curr = curr.next

        if first_node.value == curr.value:
            return True

    return False

# node1 = Node(4, Node(2, Node(3, Node(1))))
# print(is_circular(node1))

def find_last_node_in_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return fast.value
    
    return None

# node1 = Node(1, Node(2, Node(3, Node(4, Node(2)))))
# print(find_last_node_in_cycle(node1))

# node1 = Node("num1")
# node2 = Node("num2")
# node3 = Node("num3")
# node4 = Node("num4")

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node3
# print(find_last_node_in_cycle(node1))

def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def partition(head, val):
    curr = head

    temp1 = Node(0) # less than val
    temp2 = Node(0) # greater or equal val

    less = temp1 # tails
    greater = temp2

    while curr:
        next_node = curr.next
        curr.next = None
        if curr.value < val:
            less.next = curr
            less = less.next
        else:
            greater.next = curr
            greater = greater.next
        
        curr = next_node

    less.next = temp2.next
    print_list(temp1.next)

node1 = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
partition(node1, 3)

def add_two_numbers(head_a, head_b):
    curr_a = head_a
    str_a = ""

    while curr_a:
        str_a = str.join(curr_a.value)
    
    