# PROBLEM SET 1

# Problem 1
def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

count_mississippi(6)
print('\n')

# Problem 2
def swap_ends(my_str):
    swap_str = my_str[-1]
    for index in range(1,len(my_str)-1):
        swap_str += my_str[index]
    swap_str += my_str[0]

    return swap_str

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
print('\n')

# Problem 3
def is_pangram(my_str):
    lower = my_str.lower()
    splited = lower.split()
    joined = ''.join(splited)

    alphabet = {}
    for letter in joined:
        if letter in alphabet:
            alphabet[letter] += 1
        else:
            alphabet[letter] = 1
    
    if len(alphabet.keys()) >= 26:
        return True
    else:
        return False

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
print('\n')

# Problem 4
def reverse_string(my_str):
    new_str = ""

    for i in range(len(my_str)-1,-1, -1):
        new_str += my_str[i]
    
    return new_str

my_str = "live"
print(reverse_string(my_str))
print('\n')

# Problem 5
# def first_unique_char(my_str):