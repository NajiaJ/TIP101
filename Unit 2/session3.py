# Unit 2 PROBLEM SET 1

# Problem 1
def is_subsequence(lst, sequence):
    found_num = False
    for num in sequence:
        for found in lst:
            if num == found:
                found_num = True
                return True
    else:
        return False


lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))