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

# Michelle's Version
def count_ones(lst):
    if lst == [] or lst == [0] or lst == [1]:
        return 0
    else:
        return 1 + count_ones(lst[1:-1])

lst = [0, 0, 0, 0, 1, 1, 1]
print(count_ones(lst))

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
        
        return binary_search(nums, target)

    return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(nums, target))