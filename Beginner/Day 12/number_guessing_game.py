import random

from number_art import logo

def number_guess():
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    number = random.randint(1, 100)
    attempts = 0
    not_found = True

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 10 if difficulty == "easy" else 5

    while attempts > 0 and not_found:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high.\n")
        elif guess < number:
            print("Too low.\n")
        else:
            print("You got it!")
            not_found = False

        attempts -= 1

    play_again = input("Would you like to play again? ('yes' or 'no')\n")
    if play_again.lower() == "yes":
        number_guess()

number_guess()


number_guess()
