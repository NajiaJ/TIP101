def first_unique_char(my_str):
    index = 0

    for char in my_str:
        if my_str.count(char) == 1:
            return index
        index += 1
    
    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

def min_distance(words, word1, word2):
    #left = 0
    word1_dist = 0

    for i in len(words):
        if words[i] == word1:
            word1_dist = i
        elif words[i] == word2:
            word2_dist = i

def min_distance(words, word1, word2):
    left = 0
    min_distance = 0
    for i in range(len(words)):
        if words[i] == word1:
            if word2 in words[:i]:
                for j in range(i):
                    if words[j] == word2:
                        min_distance = (i - j)
            else:
                for j in range(i, len(words)):
                    if words[j] == word2:
                       min_distance = (j - i)
    return min_distance

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)

def match_made(dictionary):
	for key, value in dictionary.items():
		print( f"{key} and {value} are a perfect match.")

dictionary = {"Peanut butter" : "Jelly", "Spongebob" : "Patrick", 'Ash': 'Pikachu'}
match_made(dictionary)

def remove_char(s, n):
    s_new = s.replace(s[n],"", 1)
    s_new.strip()

    return s_new

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)

def vowel_count(s):
    vowel = 0
    s_new = s.lower()

    for char in s_new:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowel += 1
    
    return vowel

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

def reverse_sentence(sentence):
    sent_split = sentence.split()

    # new_sent = sent_split[-1]
    
    # new_sent += sent_split[0]
    new_sent = sent_split.reverse()

    return new_sent

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))