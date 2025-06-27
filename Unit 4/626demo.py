# understand step
    # empty str -> True
    # abca -> either b or c can remove but not both
    # a b c a
    # L     R
    # a b c a
    #   L R

def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    deletion = False # to check if we deleted a character
    foundPalindrome = False

    # First loop : Looping through to see if we have from the left
    while left < right:
        if s[left] == s[right]: # if they are the same letter then we can move on
            left += 1
            right -= 1
        elif not deletion: # if we made a choice to delete a character (not equal basically)
            deletion = True
            left += 1 # arbritrarily delete from left
        if left >= right: # if the pointers have crossed over then the palindromes have been found
            foundPalindrome = True
        else:
            break

    left = 0
    right = len(s) - 1
    deletion = False # to check if we deleted a character

    # Second loop: to determine if we're deleting from the right
    while left < right:
        if s[left] == s[right]: # if they are the same letter then we can move on
            left += 1
            right -= 1
        elif not deletion: # if we made a choice to delete a character
            deletion = True
            right -= 1
        if left >= right: # if the pointers have crossed over then the palindromes have been found
            foundPalindrome = True
        else:
            return False
    
    return foundPalindrome

s = "accba"
print(valid_palindrome(s))