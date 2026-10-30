
"""
Project Name : Hangman Game
Internship   : CodeAlpha - Python Programming
Developer    : Debmalya Chaki

Description:
A simple console-based Hangman game where players
guess a randomly selected word within 6 incorrect attempts.
"""

import random


# Predefined list of 5 words
WORDS = [
    "PYTHON",
    "DEVELOPER",
    "COMPUTER",
    "PROGRAM",
    "KEYBOARD"
]

# Maximum number of incorrect guesses allowed
MAX_ATTEMPTS = 6


def display_word(secret_word, guessed_letters):
    """Display guessed letters and hide unguessed letters."""

    displayed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    return displayed_word.strip()


def play_hangman():
    """Main function to execute one round of Hangman."""

    secret_word = random.choice(WORDS)

    guessed_letters = set()
    incorrect_guesses = 0

    print("\n" + "=" * 45)
    print("             HANGMAN GAME")
    print("=" * 45)

    print("\nWelcome! Try to guess the hidden word.")
    print(f"You have {MAX_ATTEMPTS} incorrect attempts.")

    # Game loop
    while incorrect_guesses < MAX_ATTEMPTS:

        print("\n---------------------------------------------")

        print("Word:", display_word(secret_word, guessed_letters))

        print("Incorrect guesses:", incorrect_guesses)

        print("Remaining attempts:",
              MAX_ATTEMPTS - incorrect_guesses)

        # Get user input
        guess = input("\nEnter a single letter: ").strip().upper()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter only one alphabet.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print("You already guessed this letter. Try another!")
            continue

        # Store guessed letter
        guessed_letters.add(guess)

        # Check the guessed letter
        if guess in secret_word:

            print(f"Correct! '{guess}' is present in the word.")

            # Check winning condition
            if set(secret_word).issubset(guessed_letters):

                print("\n" + "=" * 45)
                print("          CONGRATULATIONS!")
                print("               YOU WON!")
                print("=" * 45)

                print("The correct word was:", secret_word)

                return

        else:

            incorrect_guesses += 1

            print(f"Wrong guess! '{guess}' is not in the word.")

    # Losing condition
    print("\n" + "=" * 45)
    print("              GAME OVER!")
    print("=" * 45)

    print("You have exhausted all 6 incorrect attempts.")

    print("The correct word was:", secret_word)


def main():
    """Control the game and provide replay functionality."""

    print("\nWelcome to the CodeAlpha Hangman Project!")

    while True:

        play_hangman()

        print("\n---------------------------------------------")

        choice = input("Would you like to play again? (yes/no): ")

        if choice.strip().lower() != "yes":

            print("\nThank you for playing Hangman!")

            print("Developed by Debmalya Chaki")

            print("Keep learning and keep coding!")

            break


# Entry point of the program
if __name__ == "__main__":
    main()
