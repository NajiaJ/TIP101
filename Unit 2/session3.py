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
print('\n')

# Problem 5
def restock_inventory(current_inventory, restock_list):
    for key,value in restock_list.items():
        if key in current_inventory:
            current_inventory[key] += value
        else:
            current_inventory[key] = value
    
    return current_inventory


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory, restock_list))
print('\n')

# Problem 6
def calculate_gpa(report_card):
    #create dictionary report_card
    report_card_values = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

    #create gpa and classes counter
    gpa = 0
    classes = 0

    #loop through report_card
    for clas, grade in report_card.items():
        #add the grade values from the report_card_values to the gpa
        gpa += report_card_values[grade]
        #increase the classes by 1
        classes += 1

    #divide by the total number of classes
    gpa /= classes

    return gpa

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
print('\n')

# Problem 7
def highest_rated(books):
    high_rating = books[0]

    for book in books:
            if book.get('rating') > high_rating.get('rating'):
                high_rating = book
    
    return high_rating
        

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
print(highest_rated(books))
print('\n')

# Problem 8
def index_to_value_map(lst):
    # create a empty dictionary to return
    dictionary = {}

    # create counter for index
    index = 0

    # loop through lst
    for items in lst:
        # add new lst item to dictionary
        dictionary[index] = items
        # increase counter by 1
        index += 1
    
    #return dictionary
    return dictionary

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))