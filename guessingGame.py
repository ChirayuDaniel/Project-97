import random

print("Number Guessing Game")

chances = 0

print("Guess a number(between 1 and 9)")

random = random.randint(1,9)

while chances < 5

guess = int(input("Enter your guess :- "))

if guess == number : 
    print("You Won, heres your fake money. YAAAYY!")
    break

elif guess < number: 
    print("Your guess was way off, Choose something else", guess)

else: 
    print("Your guess was way off. Choose something else.", guess)

chances += 1

if not chances < 5 :
    print("You Lose, you don't get any money or recognition for your work. You're welcome. The number is :-", number )