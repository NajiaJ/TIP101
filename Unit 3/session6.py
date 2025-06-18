# PROBLEM SET 1

# Problem 1
def sum_of_number_strings(nums):
    total = 0
    for num in nums:
        total += int(num)
    
    return total

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
print ('\n')

# Problem 2
def remove_duplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            nums.pop(i+1)
        else:
            i += 1
    return nums

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
print('\n')

# Problem 3
def reverse_only_letters(s):
    new_s = ""
    letters = [c for c in s if c.isalpha()]

    for char in s:
        if char.isalpha():
            new_s += letters.pop()
        else:
            new_s += char
    
    return new_s

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
print('\n')

# Problem 6
def sum_of_unique_elements(lst1, lst2):
    sum_total = 0

    for num in lst1:
        if lst1.count(num) == 1:
            if num not in lst2:
                sum_total += num
    
    return sum_total

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)