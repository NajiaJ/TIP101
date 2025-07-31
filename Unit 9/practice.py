# Given the heads of two sorted linked lists,
# merge them into one sorted list by reusing nodes.

# ex: inputs -> list1 = [2, 5, 7], list2 = [1, 3, 6]
# ex: output -> [1, 2, 3, 5, 6, 7]
# Return the head of the merged list.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def print_list(node):
    current = node
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

def merged_list(list1, list2):
    # base case: if 1 list is empty return the other
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # determine what the first value is based on the lists starting values
    if list1.val < list2.val:
        temp_head = list1
        list1 = list1.next
    else:
        temp_head = list2
        list2 = list2.next

    temp_tail = temp_head # assign a tail to the head so we can append

    while list1 and list2:
        # basically do the same thing up there to keep appending
        if list1.val < list2.val:
            temp_tail.next = list1
            list1 = list1.next
        else:
            temp_tail.next = list2
            list2 = list2.next
        
        temp_tail = temp_tail.next # make sure to move the pointer
    
    # if there needs to be anything else to append
    if list1:
        temp_tail.next = list1
    elif list2:
        temp_tail.next = list2
    
    return temp_head # return the head

list1 = Node(2, Node(5, Node(7)))
list2 = Node(1, Node(3, Node(6)))
result = merged_list(list1,list2)
print_list(result)