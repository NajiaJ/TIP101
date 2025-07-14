# Version 1 - python3 s1.py

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)
print(" ")

def repeat_hello_iterative(n):
    for _ in range(n):
        print("Hello")

repeat_hello_iterative(5)
print(' ')

def factorial(n):
    total = n
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(' ')

def sum_list(lst):
    if not lst:
        return 0
    
    return lst[0] + sum_list(lst[1:])

lst = [1,2,3,4,5]
print(sum_list(lst))
print(' ')

def is_power_of_two(n):
    def increment_x(x):
        if 2**x == n:
            return True
        elif 2**x > n:
            return False
        else:
            return increment_x(x+1)

    return increment_x(0)
    
print(is_power_of_two(8))
print(" ")

def binary_search(lst, target):
    # Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst) - 1
	
	# While left pointer is less than right pointer:
    while left <= right:
		# Find the middle index of the array
        middle = (left + right) // 2
		
		# If the value at the middle index is the target value:
        if lst[middle] == target:
			# Return the middle index
            return middle
		# Else if the value at the middle index is less than our target value:
        elif lst[middle] < target:
			# Update pointer(s) to only search right half of the list in next loop iteration
            left = middle + 1
		# Else
        else:
			# Update pointer(s) to only search left half of the list in next loop iteration
            right = middle - 1
	
	# If we search whole list and haven't found target value, return -1
    return -1 

lst = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(lst, 11))
print(" ")

def find_last(lst, target):
    # Initialize a possible index
    last_possible = -1
	# Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst) - 1
	
	# While left pointer is less than right pointer:
    while left <= right:
		# Find the middle index of the array
        middle = (left + right) // 2
		
		# If the value at the middle index is the target value:
        if lst[middle] == target:
			# Return the middle index
            last_possible = middle
            left = middle + 1
		# Else if the value at the middle index is less than our target value:
        elif lst[middle] < target:
			# Update pointer(s) to only search right half of the list in next loop iteration
            left = middle + 1
		# Else
        else:
			# Update pointer(s) to only search left half of the list in next loop iteration
            right = middle - 1
            
    if last_possible != -1:
        return last_possible
	# If we search whole list and haven't found target value, return -1
    return -1 

lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
print(find_last(lst, 11))

def find_floor(lst, x):
    largest = 0
    index = 0
    for i, num in enumerate(lst):
        if num <= x:
            if num > largest:
                largest = num
                index = i

    return index

lst = [1, 2, 8, 10, 11, 12, 19]
print(find_floor(lst, 5))