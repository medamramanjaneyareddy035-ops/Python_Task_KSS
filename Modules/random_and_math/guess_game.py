#.  Create a Number Guessing Game where: 
'''● The program generates a random number between 1 and 50 using random. 
● The user has 5 attempts to guess the number. 
'''
import random

# Generate a random number between 1 and 50
number = random.randint(1, 50)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50.")
print("You have 5 attempts.")

# Give the user 5 attempts
for i in range(5):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

else:
    print("Sorry! You have used all 5 attempts.")
    print("The correct number was:", number)
