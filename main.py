# Hangman Game - CodeAlpha Python Internship
# A simple text-based Hangman game using lists, strings, loops, if-else and random.

import random

# Exactly 5 predefined words
words = ["python", "program", "keyboard", "internet", "computer"]

# Maximum number of wrong guesses allowed
MAX_ATTEMPTS = 6


def show_progress(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_game():
    secret_word = random.choice(words)   # pick a random word
    guessed_letters = []                 # all letters the player has tried
    wrong_guesses = 0                    # number of incorrect guesses

    print("=" * 40)
    print("      WELCOME TO HANGMAN GAME!")
    print("=" * 40)
    print(f"Guess the word. You can make {MAX_ATTEMPTS} wrong guesses.")
    print(f"The word has {len(secret_word)} letters.\n")

    while wrong_guesses < MAX_ATTEMPTS:
        # Show current state
        print("Word:", show_progress(secret_word, guessed_letters))
        print("Remaining attempts:", MAX_ATTEMPTS - wrong_guesses)
        if guessed_letters:
            print("Guessed letters:", ", ".join(guessed_letters))

        # Check for win
        if "_" not in show_progress(secret_word, guessed_letters):
            print("\nCongratulations! You won!")
            print("The word was:", secret_word)
            return

        # Get player's guess
        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue

        # Repeated guess does NOT reduce attempts
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

    # Final check after the loop ends
    if "_" not in show_progress(secret_word, guessed_letters):
        print("Word:", show_progress(secret_word, guessed_letters))
        print("\nCongratulations! You won!")
        print("The word was:", secret_word)
    else:
        print("Game Over! You ran out of attempts.")
        print("The word was:", secret_word)


# Main program: allows replaying
play_again = "yes"
while play_again == "yes":
    play_game()
    play_again = input("\nPlay again? (yes/no): ").lower().strip()

print("Thanks for playing Hangman. Goodbye!")
