import random


def play_hangman():
    # Key Concept: Lists (Predefined words)
    word_list = ["apple", "bread", "chair", "dance", "eagle"]

    # --- NEW: ASCII Art Figures ---
    # This list represents the hangman at different stages (0 to 6 mistakes)
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        --------
        """
    ]

    # Select a random word
    secret_word = random.choice(word_list)

    # Setup variables
    guesses_allowed = 6
    guessed_letters = []

    print("Welcome to Simple Hangman!")
    print("I have picked a word. Try to guess it letter by letter.")

    while guesses_allowed > 0:

        # --- NEW: Print the Hangman Figure ---
        # Logic: If you have 6 guesses left, you have 0 mistakes (index 0).
        # If you have 0 guesses left, you have 6 mistakes (index 6).
        mistakes_made = 6 - guesses_allowed
        print(hangman_stages[mistakes_made])
        # -------------------------------------

        # Logic to display the word (e.g., "_ _ a _ e")
        display_word = ""
        letters_remaining = 0

        for char in secret_word:
            if char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "
                letters_remaining += 1

        print(f"Word: {display_word}")
        print(f"Guesses left: {guesses_allowed}")

        # Check Win Condition
        if letters_remaining == 0:
            print(f"\nCongratulations! You won! The word was: {secret_word}")
            break

        # Input
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different one.")
            continue

        # Add guess to list
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            guesses_allowed -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    # Check Lose Condition
    if guesses_allowed == 0:
        # Print the final dead hangman figure
        print(hangman_stages[6])
        print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")


if __name__ == "__main__":
    play_hangman()