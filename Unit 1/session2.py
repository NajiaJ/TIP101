# Session 2 PROBLEM SET 1
# Problem 1
def print_list(lst):
    for pokemon in lst:
        print(pokemon)

lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)
print("\n")

# Problem 2
def doubled(lst):
    #for each number in the lst
    for num in lst:
        #multiply by 2 and print
        print(num * 2)
    
lst = [1,2,3]
doubled(lst)
print("\n")

# Problem 3
def doubled(lst):
    #create new empty list
    double_lst = []
    #for each number in the lst
    for num in lst:
        #multiply by 2 and add to lst
        double_lst.append(num * 2)
    return double_lst
lst = [1,2,3]
print(doubled(lst))
print("\n")

# Problem 4
def flip_sign(lst):
    changed_lst = []
    for num in lst:
        changed_lst.append(num * -1)
    return changed_lst

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
print("\n")

# Problem 5
def max_difference(lst):
    small = lst[0]
    large = lst[0]

    for num in lst:
        if num < small:
            small = num
        elif num > large:
            large = num
    
    result = large - small
    return result

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
print("\n")

# Problem 6
def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count+= 1

    return count

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)
print("\n")

# Problem 7
def get_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)
print("\n")

# Problem 8
def multiples_of_five():
    print(1)
    for i in range(1,101):
        if i % 5 == 0:
            print(i)

multiples_of_five()
print("\n")

# Problem 10
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(13)
print("\n")

# Problem 11
def print_indices(lst):
    for index in range(len(lst)):
        print(index)

lst = [5,1,3,8,2]
print_indices(lst)
print("\n")

# Problem 12
def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1

lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)