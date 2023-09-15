import random

# List of fruit names for word choices
fruits = [
    "apple", "banana", "mango", "pineapple", "strawberry",
    "watermelon", "papaya", "grapes", "orange", "lemon",
    "coconut", "muskmelon", "peach", "apricot"
]

# Randomly select a word from the list
word = random.choice(fruits)

# Check if this script is the main program
if __name__ == '__main__':
    print("Guess the word! Hint: The word is a name of a fruit")

    # Initialize variables
    guessed_letters = ""  # To store guessed letters
    chances = len(word) + 2  # Number of chances the player has
    game_state = 0  # 0 represents an ongoing game, 1 represents a win

    # Main game loop
    while chances > 0 and game_state == 0:
        print("\nChances left:", chances)
        chances -= 1

        # Get a letter guess from the player and convert it to lowercase
        guess = input("Enter a letter to guess: ").lower()

        # Check if the input is a single letter
        if not guess.isalpha() or len(guess) != 1:
            print('Please enter a single letter.')
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters += guess

        # Check if the guessed letter is in the word and update the display
        if guess in word:
            for char in word:
                if char in guessed_letters:
                    print(char, end=" ")  # Print the letter if guessed correctly
                else:
                    print("_", end=" ")  # Print an underscore for unrevealed letters

            # Check if the player has guessed all the letters in the word
            if set(word) == set(guessed_letters):
                print("\nThe word is:", word)
                game_state = 1
                print("Congratulations! You won!")
        else:
            print("Incorrect guess. Try again.")

    # Game over message if the player runs out of chances
    if game_state == 0:
        print('\nYou ran out of chances.')
        print('The word was:', word)
