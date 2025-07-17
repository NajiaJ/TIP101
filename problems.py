# Given a string s consisting of lowercase and/or uppercase English letters and digits, 
# return all possible strings that can be formed by changing the case of the letters in s. 
# You may not alter the order of characters in the string, and digits should remain unchanged.

# What I do know: 
    # has digits and will remain as digits, cannot change order of characters, can be lower/upper
# What do I need to find:
    # all possible strings that can be made from changing the case of letters

# lists -> to append all possible strings
# isdigit() -> check for only numbers (edge)
# upper() and lower() to change casing 
# if s is empty -> return the empty (edge)

def conversion(s):
    possibles = [""]

    if s.isdigit():
        possibles.append(s)
        return possibles
    
    if s == "":
        possibles.append(s)
        return possibles
    
    # for char in s:
    #     if char.isalpha():
    #         for str in possibles:
    #             possibles.append(str.lower())
    #             possibles.append(str.upper())
    #     if char.isdigit():
    #         possibles.append(char)

    return possibles


s = "a1b2"
#print(conversion(s))

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# sliding window technique

def needle_haystack(haystack, needle):
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
print(needle_haystack(haystack, needle))