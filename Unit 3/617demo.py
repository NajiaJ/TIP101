name = "hello world"
print("original word: ", name)

#Printing first/last characters
print("First character: ", name[0])
print("Last character: ", name[-1])

# Print first 5 characters
print("Print first 5 characters: ", name[:5])
# Print from index 6 onwards
print("Print from index 6 onwards: ", name[6:])

# Print length of string
print(len(name))

# Uppercase string
print(name.upper())
# Lowercase
print(name.lower())

print(name.replace("world", "python"))
print(name) # even though we replaced the name, the string is not immutable
print('\n')

# Problem Set Ver 3 Q5: Longest Substring
def length_of_longest_substring(s):
    # 1. initalize set to track characters
    seen = set()
    # 2. initialize left and max_length to 0
    left = 0
    max_length = 0

    # 3. for each character at position right
    for right in range(len(s)):
        # 3a. while char is in set
        while s[right] in seen:
            # 3b. remove s[left] from set
            seen.remove(s[left])
            # 3c. move left forward
            left += 1
        # 4. add s[right] to set
        seen.add(s[right])
        # 5. update max_length
        if len(seen) > 1:
            max_length = max(max_length, right - left + 1)

    return max_length

s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)