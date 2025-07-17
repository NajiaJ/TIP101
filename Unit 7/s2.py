# python3 s2.py

def is_nested(paren_s):
    if paren_s == "":
        return True
    elif paren_s == "()":
        return True
    
    if paren_s[0] == "(" and paren_s[-1] == ")":
        return is_nested(paren_s[1:-1])

    return False

paren_s = "(())"
#print(is_nested(paren_s))

def count_ones(lst):
    left = 0
    right = len(lst) - 1
    count = 0

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == 1:
            count += 1
        else:
            if lst[left + 1] == 1:
                left = left + 1
            else:
                right = right + 1
    
    return count

lst = [0, 0, 0, 0, 1, 1, 1]
print(count_ones(lst))