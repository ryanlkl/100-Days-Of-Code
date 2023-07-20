import os
import random
from game_data import data
from art import vs, logo

def higher_or_lower():
    print(logo)
    print("\nWelcome to Higher or Lower!")
    print("You will get 2 options, choose who you believe has the higher social media following count.\n")

    score = 0
    should_play = input("Would you like to start? ('yes' or 'no'): ").lower()

    while should_play == 'yes':
        os.system('cls')  # Clears the screen for a cleaner display.

        choice_a = choice_b if 'choice_b' in locals() else random.choice(data)
        choice_b = random.choice(data)

        print(logo)
        print(f"Your current score is {score}\n")
        print("Compare")
        print(f"A:\n{choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
        print(vs)
        print(f"B:\n{choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")

        guess = input("Who has more followers? 'A' or 'B'?: ").lower()

        if (guess == 'a' and choice_a['follower_count'] > choice_b['follower_count']) or \
           (guess == 'b' and choice_b['follower_count'] > choice_a['follower_count']):
            score += 1
        else:
            break

        os.system('cls')

    print(f"\nWrong! Your final score is {score}\n")
    carry_on = input("Do you want to play again? ('y' or 'n'): ").lower()
    if carry_on == 'y':
        higher_or_lower()

higher_or_lower()
