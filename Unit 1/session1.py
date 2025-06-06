# Session 1 - PROBLEM SET 1
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
print('\n')

# PROBLEM SET 2

# Problem 1
def greet_user(name):
    print("Hello " + name)

greet_user("Michael")
print('\n')

# Problem 2
def difference(a, b):
    return b - a

diff = difference(3,8)
print(diff)
print('\n')

# Problem 3
def concatenate_list(nums):
    concat = nums + nums
    print(concat)

concatenate_list([1,2,3,4])
print('\n')

# Problem 4
def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours >= 8 and hours <= 10:
        print("You got a good night's rest!")
    else:
        print("You're a sleep prodigy")

sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)
print('\n')

# Problem 5
def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        bill = bill * 0.10
        return bill
    elif service_quality == "average":
        bill = bill * 0.15
        return bill
    elif service_quality == "excellent":
        bill = bill * 0.20
        return bill
    else:
        return "None"

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
print('\n')

# Problem 6
def rock_paper_scissors(player1, player2):
    if player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 wins!")
    elif player1 == player2:
        print("It's a tie!")
    else:
        print("No winner!")

rock_paper_scissors('rock', 'rock')
rock_paper_scissors('scissors', 'rock')
rock_paper_scissors('scissors', 'paper')
rock_paper_scissors('rock', 'paper')
rock_paper_scissors('paper', 'rock')
print('\n')

# Problem 7
def halve_lst(lst):
    result = []
    for number in lst:
        halved = number/2
        result.append(halved)
    return result

print(halve_lst([2,4,6,8]))
print('\n')

# Problem 8
def above_threshold(lst, threshold):
    new_lst = []
    for num in lst:
        if num > threshold:
            new_lst.append(num)

    return new_lst

lst = [8,2,13,11,4,10,14]
new_lst = above_threshold(lst, 10)
print(new_lst) 
print('\n')

# Problem 9
def countdown(m,n):
    for num in range(m, n-1, -1): #step here being -1 so we can go back
        print(num)

countdown(5,1)
print('\n')

# Problem 10
def power(base, exponent):
    return base ** exponent

pow1 = power(2,5)
print(pow1)
pow2 = power(3,3)
print(pow2)
print('\n')

# Problem 11
def list_length(lst):
    length = 0;
    for num in lst:
        length += 1
    
    return length

lst = [2,4,6,8,10]
length = list_length(lst)
print(length)
print('\n')

# Problem 12
def factorial(n):
    fact = 1; #have to make the factorial have 1 since it ends with one
    for num in range(n, 0, -1):
        fact = fact * num
    return fact

print(factorial(3))
print('\n')

# Problem 13
def squares(nums):
    square = []
    for num in nums:
        square.append(num * num)
    return square

print(squares([1,2,3,4]))
print('\n')

# Problem 14
def multiply_list(lst, multiplier):
    multipled = []
    for num in lst:
        multipled.append(num * multiplier)
    return multipled

lst = [1,2,3]
new_lst = multiply_list(lst, 3)
print(new_lst)
print('\n')

# Problem 15
def count_evens(lst):
    count = 0;
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)