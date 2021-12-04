from game_data import data
from art import logo
from art import vs
import random

def compare(A, B): #Compare follower counts and return the one with higher follower count
    print(
        f"Compare A: {data[A]['name']} a {data[A]['description']}, from {data[A]['country']}.")
    print(vs)
    print(
        f"Compare B: {data[B]['name']} a {data[B]['description']}, from {data[B]['country']}.")
    if data[A]['follower_count'] > data[B]['follower_count']:
        return 'a'
    else:
        return 'b'


datalength = len(data) - 1
score = 0
comparison_A = 0
comparison_B = 0
correct_answer = None

print(logo)

playing = True
while playing:
    while comparison_A == comparison_B or correct_answer == 'a' or correct_answer == 'b': 
        # Generate a random int to index into data list as arguments for compare().
        # Should have used random.choice() instead
        if correct_answer == 'a':
            comparison_B = random.randint(0, datalength)
            correct_answer = None
        elif correct_answer == 'b':
            comparison_A = random.randint(0, datalength)
            correct_answer = None
        else:
            comparison_A = random.randint(0, datalength)
            comparison_B = random.randint(0, datalength)
    
    correct_answer = compare(comparison_A, comparison_B) # return correct answer from compare function
    answer = input("Who has more followers? Type 'A' or 'B'\n").lower()

    if answer == correct_answer: # check user answer 
        score += 1
        print(f"Correct! Your score is now {score}")
    else:
        print(f"Sorry that is wrong. Your final score is {score}")
        playing = False
