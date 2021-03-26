import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25]

number = random.choice(list)

user_guess = input("Make a guess here: ")

if number == user_guess:
    print("You are right!")
else:
    print("You are wrong.")