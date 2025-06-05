# Problem 2
def todays_mood():
    mood = "🥳"
    print("Today's mood: " + mood)

todays_mood()
print('\n')

# Problem 3
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu("noodles")
print('\n')

# Problem 4
def sum(a, b):
    return a + b

print(sum(20,8) + sum(20,8))
print('\n')

# Problem 5
def product(a,b):
    return a * b

print(product(22,7))
print('\n')

# Problem 6
def classify_age(age):
    if age < 18:
        return("child")
    else:
        return("adult")

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)
print('\n')

# Problem 7
def what_time_is_it(hour):
    if hour == 2:
        return("taco time")
    elif hour == 12:
        return("peanut butter jelly time")
    else:
        return("nap time")

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)
print('\n')

# Problem 8
def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("Nice hand!")
    else:
        print("Hit me!")

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)
print('\n')

# Problem 9
def get_first(lst):
    if lst: #if the lst isn't empty
        print(lst[0])
    else: #all else print this
        print("None")

get_first([3,1,6,7,5])
print('\n')

# Problem 10
def get_last(lst):
    if lst:
        print(lst[len(lst) - 1])
    else:
        print("None")

get_last([3,1,6,7,5])
print('\n')

# Problem 11
def counter(stop):
    for i in range (1, stop + 1):
        print (i)

counter(7)
print('\n')

# Problem 12
def sum_ten():
    total = 0;
    for i in range(1,11):
        total += i;
    print(total)
sum_ten()
print('\n')

# Problem 13
def sum_positive_range(stop):
    total = 0;
    for i in range (1, stop + 1):
        total += i
    print(total)

sum = sum_positive_range(6)
print('\n')

# Problem 14
def sum_range(start, stop):
    total = 0;
    for i in range(start, stop + 1):
        total += i
    print(total)

sum = sum_range(3, 9)
print('\n')

# Problem 15
def print_negatives(lst):
    has_negatives = False
    for num in lst:
        if num < 0:
            print(num)
            has_negatives = True
    if not has_negatives:
        print("None")

print_negatives([3,-2,2,1,-5])
print_negatives([1,2,3,4,5])