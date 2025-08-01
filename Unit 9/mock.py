class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next

def merge(list1, list2):
    # base: if 1 is empty return the other
    if not list1:
        return list2
    if not list2:
        return list1
    # base? : both are empty
    if not list1 and not list2:
        return []

    # make an empty list
    new_lst = []
    # append the head of whichever list is smaller
    if list1.val < list2.val:
        new_lst.append(list1.val)
        list1 = list1.next
    else:
        new_lst.append(list2.val)
        list2 = list2.next
    # move the pointers 

    #go through lists
    while list1 and list2:
        #compare whichever comes first append and moves its pointer
        if list1.val < list2.val:
            new_lst.append(list1.val)
            list1 = list1.next
        else:
            new_lst.append(list2.val)
            list2 = list2.next
        # else will be opposite
    
    #append whatever
    if list1:
        new_lst.append(list1.val)
    elif list2:
        new_lst.append(list2.val)

    #return list
    return new_lst

list1 = Node(2, Node(5, Node(7)))
list2 = Node(1, Node(3, Node(6)))
print(merge(list1, list2))