# PROBLEM SET 1

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

def reverse_list(lst):
    pointer1 = 0
    pointer2 = len(lst) - 1

    while pointer1 < pointer2:
        lst[pointer1], lst[pointer2] = lst[pointer2], lst[pointer1]
        pointer1 += 1
        pointer2 -= 1

    return lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

def sort_array_by_parity(nums):
    pointer1 = 0
    pointer2 = len(nums) - 1

    while pointer1 < pointer2:
        if nums[pointer1] % 2 != 0 and nums[pointer2] % 2 == 0:
            nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
        pointer1 += 1
        pointer2 -= 1
    
    return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

def check_palindrome(word):
    pointer1 = 0
    pointer2 = len(word) - 1

    while pointer1 < pointer2:
        if word[pointer1] != word[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
        
    return True

def first_palindrome(words):
    for word in words:
        if check_palindrome(word):
            return word
    
    return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

def remove_duplicates(nums):
    pointer1 = 1
    pointer2 = 0

    while pointer1 < len(nums):
        if nums[pointer1] != nums[pointer2]:
            nums[pointer2 + 1] = nums[pointer1]
            pointer2 += 1
        pointer1 += 1
    
    return pointer2 + 1

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list