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
print('\n')

# PROBLEM SET 2

# Problem 1
def match_made(dictionary):
	for key, value in dictionary.items():
		print( f"{key} and {value} are a perfect match.")

dictionary = {"Peanut Butter":"Jelly", "Spongebob":"Patrick", "Ash":"Pikachu"}
match_made(dictionary)
print('\n')

# Problem 2
def remove_char(s, n):
    new_s = ""
    for index, char in enumerate(s):
        if index is not n:
            new_s += char
    
    return new_s

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
print('\n')

# Problem 3
def vowel_count(s):
    vowel_total = 0

    for char in s:
        if char == 'A' or char == 'a' or char == 'E' or char == 'e' or char == 'I' or char == 'i' or char == 'O' or char == 'o' or char == 'U' or char == 'u':
            vowel_total += 1
    
    return vowel_total

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)
print('\n')

# Problem 4
def reverse_sentence(sentence):
    spilt = sentence.split()
    new_sentence = ""

    for i in range(len(spilt) - 1, -1, -1):
        new_sentence += spilt[i] + " "

    return new_sentence

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))
print('\n')

# Problem 5
def compress_string(my_str):
    letter_dict = {}  # repurposed as a tracker, not a true dictionary
    new_str = ""

    if not my_str:
        return my_str

    prev_letter = my_str[0]
    count = 1

    for letter in my_str[1:]:
        if letter == prev_letter:
            count += 1
        else:
            letter_dict[prev_letter] = count  # save run
            new_str += prev_letter + str(count)
            prev_letter = letter
            count = 1

    # Add the last run
    letter_dict[prev_letter] = count
    new_str += prev_letter + str(count)

    return new_str if len(new_str) < len(my_str) else my_str

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)