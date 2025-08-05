# Problem Set 1

def is_valid(s):
    if s == "":
        return True

    stack = [] # empty stack
    mappings = {'}':'{', ')':'(', ']':'['}

    for char in s:
        if char in mappings:
            top_ele = stack.pop() if stack else '#'
            if mappings[char] != top_ele:
                return False
        else:
            stack.append(char)
    
    return not stack

# s = "(]"
# print(is_valid(s))

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def shuffle_merge(head_a, head_b):
    curr_a = head_a.next
    curr_b = head_b

    merged = head_a
    curr_merge = merged

    toggle = True
    while curr_a and curr_b:
        if toggle:
            curr_merge.next = curr_b
            curr_b = curr_b.next
        else:
            curr_merge.next = curr_a
            curr_a = curr_a.next
        curr_merge = curr_merge.next
        toggle = not toggle

    curr_merge.next = curr_a if curr_a else curr_b

    return merged