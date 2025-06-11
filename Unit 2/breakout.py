# Problem 1
def is_subsequence(lst, sequence):
    i = 0
    for num in lst:
        if i < len(sequence) and num == sequence[i]:
            i += 1
    return i == len(sequence)

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
print('/n')

# Problem 2
def create_dictionary(keys, values):
    dictionary = {}

    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    
    return dictionary

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))
print('/n')

# Problem 3
def print_pair(dictionary, target):
    if target in dictionary:
        print("Key: ", target)
        print("Value: ", dictionary[target])
    else:
        print("That pair doesn't exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
print('/n')

# Problem 4
