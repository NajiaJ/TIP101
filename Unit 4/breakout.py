# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True

# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))