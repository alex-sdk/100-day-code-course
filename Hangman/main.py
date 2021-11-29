import random
from hangman_art import logo, stages
from hangman_word import word_list


print(logo)

chosen_word = random.choice(word_list)

end_game =  False
word_len = len(chosen_word)
display = []
lifes = 6

for letters in range(word_len):
    display.append('_')

print(f"{' '.join(display)}")

while not end_game:
    guess = input("Guess a letter\n")

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_game = True
        print("You win")

    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lifes -= 1
        if lifes == 0:
            end_game = True
            print("You lose.")
    
    print(stages[lifes])
