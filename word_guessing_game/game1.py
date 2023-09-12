import random            # Import the random module to generate a random word

name = input("What is your name? ")
print("Good Luck, " + name + "!")

word_list = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition',
           'water', 'board',"pineapple","apple","strawberry","box","hello","bird","elephant","flower","vegetable","fruit"]

word = random.choice(word_list)

print("Guess the characters")

guesses = " "          # Initialize the 'guesses' variable as an empty string to store guessed characters

try:
    turns = int(input("How many turns you want? "))
    
except:
    print("You have 10 turns")
    turns =10

while turns > 0:                        # Start a while loop that continues as long as the user has turns left
    failed = 0                         # Initialize a variable to count how many characters were not guessed in each turn

    for char in word:                    # Iterate through each character in the random word
        if char in guesses:              # If the character has been guessed and is in 'guesses'...
            print(char, end=" ")          # Print the character (with a space) to show it
        else:
            print("_", end=" ")           # If the character has not been guessed, print an underscore
            failed += 1                    #Increment the 'failed' count

    if failed == 0:                    # If 'failed' is still 0 after the loop, it means all characters have been guessed
        print("\nYou Win","YAY")
        print("The word is", word)
        break                               # Exit the loop when the user wins

    print()
    guess = input("Guess a character: ")          # Ask the user to guess a character and store it in 'guess'
    guesses += guess                              # Add the guessed character to the 'guesses' string
    
    '''if len(guess) != 1 or not guess.isalpha():  
        print("Please enter a single letter.")
        continue ''' 

    guess = guess.lower()                         # Convert the guessed character to lowercase for consistency


    if guess not in word:
        turns -= 1                                # Decrement the number of turns
        print("Wrong")                              # Print a message indicating the guess was incorrect
        print("You have", turns, "more guesses")     # Print the number of remaining turns


        if turns == 0:                            # If there are no more turns left...
            print("You lose!!!!")
            print("correct word is ",word)         # Print the correct word
    print("Your guessed characters:", guesses)     # Print the guessed characters after each guess

