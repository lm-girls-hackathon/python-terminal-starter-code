#add school name, group number, and individual names

#this method plays the game 
def play_game():
    word = input("enter the word")
    guess = ["_" for _ in range(len(word))]  # create list of characters which represents the word
    # TODO: create a strike counter which counts how many times they guess incorrectly

    while "".join(guess) != word:
        letter = input("guess a letter")  # the user will enter a letter to guess
        # TODO: verify that the user entered a valid input (a single letter)

        if letter in word:
            update_guess(guess, word, letter)
        else:
            # TODO: update the strike counter if an incorrect letter was guessed
            ...

        # TODO: exit the program if there are a certain number of strikes
        print(" ".join(guess))  # prints the guess as a space-separated string
        # TODO: print a list of letters which are not in the word

    # TODO: make a message congratulating the player if they win
    # TODO: make a loop that lets users play another game
    # TODO: draw a hangman figure using keyboard characters

    
def update_guess(guess, word, letter):
    # TODO: update guess based on where the letter is in the word
    ...


play_game()
