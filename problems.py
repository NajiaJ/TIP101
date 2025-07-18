# Given a string s consisting of lowercase and/or uppercase English letters and digits, 
# return all possible strings that can be formed by changing the case of the letters in s. 
# You may not alter the order of characters in the string, and digits should remain unchanged.

# empty str -> return empty
# all digits -> return digits
#  upper and lower

def conversion(s):
    possibles = []

    # edge: empty
    if s == "":
        return s

    # edge: all numbers
    if s.isdigit():
        return s
    
    possibles.append(s.upper())
    possibles.append(s.lower())
    # letters and number
    # for loop -> go through s look each letter
    for char in s:
        # if it is a letter -- upper and lower , append to list
        if char.isalpha():
            possibles.append(char.upper())
            possibles.append(char.lower())
        # if it is a number -- add onto the str, append to list

    # return lst
    return possibles

s = "a1b2"
#print(conversion(s))

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# sliding window technique 
# MY VERSION

def haystack_needle(haystack, needle):
    if needle == "": # edge case
        return 0

    if len(needle) > len(haystack): # edge case
        return -1
    
    for i in range(0, len(haystack) - len(needle) + 1):
        slice = haystack[i: i + len(needle)]

        if slice == needle:
            return i
    
    return -1

haystack = "leetcode"
needle = "leeto"
print(haystack_needle(haystack, needle))

def needle_haystack(haystack, needle):
    if needle not in haystack:
        return -1
    
    if len(needle) > len(haystack):
        return -1
    
    i = len(needle)

    for g in range(len(haystack)):
        if haystack[g:i] == needle:
            return g

# haystack = "sadbutsad"
# needle = "sad"
haystack = "leetcode"
needle = "leeto"
print(needle_haystack(haystack, needle))