def word_pattern(pattern, s):
    # 1. split s into list of words
    words = s.split()
    # 2. if len of words != len of pattern return False
    if len(words) != len(pattern):
        return False

    # 3. create a char_to_word and word_to_char dictionaries
    char_to_word = {} # map pattern chars to words
    word_to_char = {} # map words to pattern chars
    
    # 4. for each char, word in (pattern, words)
    for char, word in zip(pattern, words):
        # 5. if char in char_to_word
        if char in char_to_word:
            # if current mapping != return false
            if char_to_word[char] != word:
                return False
        # 6. else add to dict
        else:
            char_to_word[char] = word

        # 7. repeat 4-6 but for word_to_char
            # if word in word_to_char
        if word in word_to_char:
            # if current mapping != return false
            if word_to_char[word] != char:
                return False
         # else add to dict
        else:
            word_to_char[word] = char
    
    # return True
    return True

pattern = "abba"
s = "dog cat cat dog"
print(word_pattern(pattern, s))
s2 = "dog cat cat fish"
print(word_pattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(word_pattern(pattern2, s3))
s4 = "dog dog dog dog"
print(word_pattern(pattern2, s4))