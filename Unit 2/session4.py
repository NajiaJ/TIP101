# PROBLEM SET 1

# Problem 1
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    
    return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
print('\n')

# Problem 2
def common_keys(dict1, dict2):
	
    common_key = []
    for letter, integer in dict1.items():
        if letter in dict2:
            common_key.append(letter)
    
    return common_key

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
print('\n')

# Problem 3
def get_highest_priority_task(tasks):
    max_name = None
    max_prio = -1

    for name, priorities in tasks.items():
        if priorities > max_prio:
            max_name = name
            max_prio = priorities
        elif priorities == max_prio and name < max_name:
            max_prio = priorities
            max_name = name
    
    if max_name:
        tasks.pop(max_name)
        return max_name

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
print('\n')

# Problem 4
def count_occurrences(nums):
    num_dict = {}

    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    return num_dict

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))
print('\n')

# Problem 5
def find_majority_element(elements):
    counts = {}
    threshold = len(elements) // 2

    for num in elements:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > threshold:
            return num

    return None


elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
print('\n')