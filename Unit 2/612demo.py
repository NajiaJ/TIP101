def count_by_category(items):
    #1. create empty dict
    counts = {}
        #other ways to create empty dictionaries
            # counts = dict{} -> dict is a constructor

    #2. loop through each tuple:
    for category, __ in items: # we can use __ to throw away that value
        #2a. if item is in dict: increment value by 1
        if category in counts:
            counts[category] += 1
        #2b. else, add to dict with val of 1
        else:
            counts[category] = 1
    #3. return dict
    return counts

items = [("fruits", "apples"), ("vegetables", "carrot"), ("fruits", "banana")]
print(count_by_category(items))