def group_anagrams(words):
    # 1. Create an empty dictionary
    anagrams = {}
    # 2. loop through words
    for word in words:
        #3. sort the word to create a key
        key = ''.join(sorted(word))
        # sorted function will return a list of letters
        # joins brings it together as a string
        #4. if the key not in dict, create a new list
        #   "aet" : []
        if key not in anagrams:
            anagrams[key] = []
        # 5. add word to the group
        #   "aet": ["word"]
        anagrams[key].append(word)
    # 6. return grouped lists
    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
print("\n")

words2 = []
print(group_anagrams(words2))