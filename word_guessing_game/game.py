import random  

name = input("What is your name? ")

print("Good Luck, " + name + "!")

word_list = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks',"pineapple","apple","strawberry","box","hello","bird"]

word = random.choice(word_list)

print("Guess the characters")

guesses = " "

try:
    turns = int(input("How many turns you want? "))
    
except:
    print("You have 10 turns")
    turns =10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ") 
            failed += 1
    if failed == 0:
        print("\nYou Win","YAY")
        print("The word is", word)
        break  

    print()
    guess = input("Guess a character: ")
    guesses += guess
    '''if len(guess) != 1 or not guess.isalpha():  
        print("Please enter a single letter.")
        continue ''' 

    guess = guess.lower()

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, "more guesses")

        if turns == 0:
            print("You lose!!!!")
            print("correct word is ",word)
    print("Your guessed characters:", guesses)
#hello
