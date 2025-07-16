# python3 breakout.py

def is_power_of_two(n):
    if n == 1:
        return True

    if n % 2 != 0:
        return False
    else:
        return is_power_of_two(n//2)

#print(is_power_of_two(4))

def countdown(n):
	if n > 0:
		print(n)
		countdown(n - 1)
		
#countdown(5)

def countdown_iterative(n):
    for _ in range(n):
        print(n)
        n -= 1

# countdown_iterative(5)

def find_floor(lst, x):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == x:
            result = middle
        elif lst[middle] < x:
            result = middle
            left = middle + 1
        else:
            right = middle - 1
    
    return result

lst = [1, 2, 8, 10, 11, 12, 19]
# print(find_floor(lst, 5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))

def list_product(lst):
    if not lst:
        return 1
    
    return lst[0] * list_product(lst[1:])

lst = [1, 2, 3, 4, 5]
# print(list_product(lst))

def is_power_of_four(n):
    if n == 1:
        return True
    
    if n % 4 != 0:
        return False
    else:
        return is_power_of_four(n//4)

# print(is_power_of_four(64))

def binary_search_iterative(arr, target):
    left = 0
    right = len(lst) - 1
    result = -1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1

lst = [1, 3, 5, 7, 9, 11, 13, 15]
#print(binary_search_iterative(lst, 11))

def find_ceiling(lst, x):
    left = 0
    right = len(lst) - 1
    result = -1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] < x:
            left = middle + 1
        elif lst[middle] > x:
            result = middle
            right = middle - 1
        else:
            result = middle
    
    return middle

lst = [1, 2, 8, 10, 11, 12, 19]
# print(find_ceiling(lst, 5))

def ternary_search(lst, target):
  # Divide the array into three parts using two mid points (mid1 and mid2).
    left = 0
    right = len(lst) - 1
  
    while left <= right:
        third = (left + right) // 3
        mid1 = left + third
        mid2 = right - third

        if target == lst[mid1]:
              return mid1
        if target == lst[mid2]:
            return mid2
	      # If the target is less than the value at mid1
        if target < lst[mid1]:
		      # search between the lower bound and mid1 - 1.
            right = mid1 - 1
	      # If the target is between mid1 and mid2
        elif mid1 < target < mid2:
		      # search between mid1 + 1 and mid2 - 1.
            left = mid1 + 1
            right = mid2 - 1
	      # If the target is greater than the value at mid2
        else:
		      # search between mid2 + 1 and the upper bound.
              left = mid2 + 1
  # Return -1, indicating the target is not in the array.
    return -1

lst = [1, 3, 5, 7, 9, 11, 13, 15]
print(ternary_search(lst, 11))