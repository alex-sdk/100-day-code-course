from art import logo
import random
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []

playing = True
while playing:
    play_yes_or_no = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_yes_or_no == 'y':
        for draw in range(2):
            playing_card = random.choice(cards)
            player_hand.append(playing_card)
            player_score = sum(player_hand)
            ace = playing_card + player_score
            if playing_card == 11 and ace > 21:
                player_hand.remove(11)
                player_hand.append(1)
            player_score = sum(player_hand)
            if draw == 1:
                computer_hand.append(random.choice(cards))
        computer_score = sum(computer_hand)
        print(f"Yours cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_score}")

        end_turn = True
        while player_score < 21 and end_turn:
            another_hand = input("Type 'y' for another card, type 'n' to pass: ")
            if another_hand == 'n':
                end_turn = False
                break
            playing_card = random.choice(cards)
            player_hand.append(playing_card)
            ace = playing_card + player_score
            if playing_card == 11 and ace > 21:
                player_hand.remove(11)
                player_hand.append(1)
            player_score = sum(player_hand)
            print(f"Yours cards: {player_hand}, current score: {player_score}")
        while computer_score < 17:
            playing_card = random.choice(cards)
            computer_hand.append(playing_card)
            ace = playing_card + computer_score
            if playing_card == 11 and ace > 21:
                computer_hand.remove(11)
                computer_hand.append(1)
            computer_score = sum(computer_hand)

        print(f"Computers final hand: {computer_hand}, final score {computer_score}")

        if player_score > 21:
            print("You went over you bust.")
        elif computer_score > 21:
            print("Computer bust you win!")
        elif player_score == computer_score:
            print("It's a draw.")
        elif player_score > computer_score:
            print("You win!")
        else:
            print("You lose.")
 
        player_hand = []
        computer_hand = []
 
    else:
        playing = False
