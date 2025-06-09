# Unit 2 PROBLEM SET 1

# Problem 1
def is_subsequence(lst, sequence):
    found_num = False
    for num in sequence:
        for found in lst:
            if num == found:
                found_num = True
                return True
    else:
        return False


lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
print('\n')

# Problem 2
def create_dictionary(keys, values):
    d = {} #initialize dictionary
    for key in range(len(keys)): #can use zip(keys,values)
        if key < len(values): 
            d[keys[key]] = values[key]
    return d

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))
print('\n')

# Problem 3
def print_pair(dictionary, target):
    if target in dictionary:
        print("Key:", target)
        print("Value:", dictionary[target])  # or dictionary.get(target)
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
print('\n')

# Problem 4
def keys_v_values(dictionary):
    #set up sum key and val variables
    sum_key = 0
    sum_val = 0
    #go through the dictionary
    for key,value in dictionary.items():
        #add up all keys
        sum_key += key
        #add up all values
        sum_val += value
        #if sum of keys > values
        if sum_key > sum_val:
            #print keys
            return 'keys'
        #elif 
        elif sum_val > sum_key:
            #print values
            return 'values'
        #elif ==
        elif sum_key == sum_val:
            #print balanaced
            return 'balanced'

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)