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
def first_unique_char(my_str):
    char_count = {}

    for char in my_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for letter, value in enumerate(my_str):
        if char_count[value] == 1:
            return letter

    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
print('\n')

# Problem 6
def min_distance(words, word1, word2):
    index1 = -1
    index2 = -1
    min_dist = float('inf')

    for i in range(len(words)):
        if words[i] == word1:
            index1 = i
        elif words[i] == word2:
            index2 = i
        
        if index1 != -1 and index2 != -1:
            dist = abs(index1 - index2)
            if dist < min_dist:
                min_dist = dist

    if min_dist == float('inf'):
        return -1
    else:
        return min_dist

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
