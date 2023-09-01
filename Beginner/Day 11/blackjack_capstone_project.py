import random
from blackjack_art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_card():
    return random.choice(cards)

def calculate_score(card_list):
    score = sum(card_list)
    if len(card_list) == 2 and score == 21:
        return 0
    elif score > 21 and 11 in card_list:
        score -= 10
        card_list[card_list.index(11)] = 1
    return score

def blackjack():
    print("Welcome to Blackjack!")
    name = input("What is your name?: ")
    keep_playing = True

    while keep_playing:
        user_cards.clear()
        computer_cards.clear()
        user_score = 0
        computer_score = 0
        computer_turn = False

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}\nComputer's first card: {computer_cards[0]}")

        while not computer_turn:
            deal = input("Would you like me to deal you a card? ('Y' or 'N'): ")
            if deal == "Y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"\nYour cards: {user_cards}")

                if user_score == 0:
                    print(f"{name} got a Blackjack!")
                    computer_turn = True
                elif user_score > 21:
                    print(f"{name} goes bust.")
                    computer_turn = True
            else:
                computer_turn = True

        while computer_score < 17 and computer_turn:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"\nYour final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}\n")

        if user_score > 21 and computer_score > 21:
            print("Both went bust! Draw!")
        elif user_score == computer_score:
            print("It's a draw!")
        elif user_score == 0 or computer_score > 21 or (user_score > computer_score and user_score <= 21):
            print(f"{name} wins!")
        else:
            print("Computer wins!")

        play_again = input("\nWould you like to play again? ('Y' or 'N'): ")
        if play_again != 'Y':
            keep_playing = False

blackjack()
