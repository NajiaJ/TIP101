# def sum_of_number_strings(nums):
#     total = 0
#     for num in nums:
#         total += int(num)
    
#     return total

# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)

# def remove_duplicates(nums):
#     lst = []

#     for num in nums:
#         if num not in lst:
#             lst.append(num)
    
#     return lst

# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))

# def reverse_only_letters(s):
#     lst = []
#     new_s = ""

#     for char in s:
#         if char != '-':
#             lst.append(char)
    
#     for char in s:
#         if char == '-':
#             new_s += '-'
#         else:
#             new_s += lst.pop()

#     return new_s

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)

# def longest_uniform_substring(s):
#     letter_dict = {}
    
#     for char in s:
#         if char in letter_dict:
#             letter_dict[char] += 1
#         else:
#             letter_dict[char] = 1
    
#     return max(letter_dict.values())

# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)

# def sum_of_unique_elements(lst1, lst2):
#     total = 0

#     for num in lst1:
#         if num not in lst2 and lst1.count(num) == 1:
#             total += num
    
#     return total

# lstA = [1, 2 ,3, 4] 
# lstB = [3, 4, 5, 6]
# lstC = [7, 7, 7, 7]

# sum1 = sum_of_unique_elements(lstA, lstB)
# print(sum1)

# sum2 = sum_of_unique_elements(lstC, lstB)
# print(sum2)

# def string_to_integer_mapping(s):
#     lst = []

#     for char in s:
#         lst.append(int(char))

#     return lst

# s="12345"
# print(string_to_integer_mapping(s))

# def delete_minimum_elements(nums):
#     lst = []

#     while nums:
#         min_val = min(nums)
#         lst.append(min_val)
#         nums.remove(min_val)
    
#     return lst

# nums = [5,3,2,8,3,1]
# removed_lst = delete_minimum_elements(nums)
# print(removed_lst)

def count_consecutive_characters(str1):
    letter_dict = {}
    
    for char in str1:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    
    return max(letter_dict.values())

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)
str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)