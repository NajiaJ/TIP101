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

# Problem 8


# def get_last(lst):
#     x = lst[len(lst) - 1]
#     print(x)

# get_last([3,1,6,7,5])