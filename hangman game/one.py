import random
fruits = [
    "apple","mango","banana"
]

word = random.choice(fruits)

if __name__== "__main__":
    print("Guess the word! Hint: The words belongs to fruits category")

    guessed_letters =" "
    chances = len(word)+2
    game_state =0

    while chances>0 and game_state ==0:
        print("\nchances left",chances)
        chances-=1

        guess = input("Enter a letter to guess: ").lower()

        if not guess.isalpha() or len(guess)!=1:
            print("Please enter single letter ")
            continue
        
        guessed_letters +=guess
        if guess in word:
            for char in word:
                if char in guessed_letters:
                    print(char,end = "")

                else:
                    print("_",end =" ")

            if set(word)==set(guessed_letters):
                print("\n the word is ",word)
                game_state = 1

        else:
            print("Incorrect guess.Try again")

    if game_state ==0:
        print("\n you ran out of chances")
        print("The word was :",word)

