import random
from art import logo

def guess_attempt(answer):
    guess = int(input("Makes a guess: "))
    if guess == answer:
        print(f"You got it! The answer was {answer}")
        quit()
    elif guess > answer:
        print("Too high! Guess again")
    elif guess < answer:
        print("Too low! Guess again.")

print(logo)
answer = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty =  input("Choose a difficulty. Type 'easy' or 'hard':  ")

if difficulty == "easy":
    lives = 10
else:
    lives = 5

while lives > 0:
    print(f"You have {lives} attempts remaining!")
    guess_attempt(answer)
    lives -= 1
print("You have run out of guesses, you lose.")