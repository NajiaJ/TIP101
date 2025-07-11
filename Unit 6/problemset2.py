# python3 problemset2.py

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    if not head:
        return False

    curr = head.next

    while curr is not None and curr != head:
        curr = curr.next
    
    return curr == head

# node1 = Node("num1")
# node2 = Node("num2")
# node3 = Node("num3")

# node1.next = node2
# node2.next = node3
# node3.next = node1
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

# node1 = Node("num1")
# node2 = Node("num2")
# node3 = Node("num3")
# node4 = Node("num4")

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2
# print(find_last_node_in_cycle(node1))

def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def partition(head, val):
    before_list = Node(0)
    after_list = Node(0)

    before = before_list
    after = after_list
    curr = head

    while curr:
        if curr.value >= val:
            after.next = curr
            after = after.next
        else:
            before.next = curr
            before = before.next
        
        curr = curr.next
    
    after.next = None
    before.next = after_list.next

    return before_list.next

# head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
# print_list(head)
# head = partition(head, 3)
# print_list(head)

def traverse_list(head):
    curr = head
    lst = []
    number = ""

    while curr:
        lst.append(curr.value)
        curr = curr.next
    
    for i in range(len(lst) -1, -1, -1):
        number += str(lst[i])
    
    return int(number)

def add_two_numbers(head_a, head_b):
    lst_a = traverse_list(head_a)
    lst_b = traverse_list(head_b)

    total = str(lst_a + lst_b)
    reverse = total[::-1]
    
    temp_head = Node(0)
    curr = temp_head

    for char in reverse:
        curr.next = Node(int(char))
        curr = curr.next

    return temp_head.next

# head = Node(2, Node(4, Node(3)))
# head_2 = Node(5, Node(6, Node(4)))
# result = add_two_numbers(head, head_2)
# print_list(result)

def make_circular(head):
    curr = head

    while curr.next:
        curr = curr.next
    
    curr.next = head
    
    return head

# head = Node(1, Node(4, Node(3)))
# print_list(head)
# make_circular(head)

def collect_cycle_nodes(head):
    lst = []

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            meeting_point = slow.next
            curr = meeting_point
            while True:
                lst.append(curr.value)
                curr = curr.next

                if curr == meeting_point:
                    break

            break

    return lst

# node1 = Node("num1")
# node2 = Node("num2")
# node3 = Node("num3")
# node4 = Node("num4")

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2
# lst = collect_cycle_nodes(node1)
# print(lst)

def delete_dupes(head):
    curr = head

    temp = Node(0)
    temp.next = head

    # this gets rid of dupes but not the actual instance
    while curr and curr.next:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return temp.next

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
print_list(head)
result = delete_dupes(head)
print_list(result)