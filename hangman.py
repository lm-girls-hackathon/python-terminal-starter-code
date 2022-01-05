WORD = input("enter the word")

guess = ["_" for _ in range(len(WORD))]

# TODO: create a strike counter which counts how many times they guess incorrectly

while "".join(guess) != WORD:
    letter = input("guess a letter")
    if letter in WORD:
        for i in range(len(WORD)):
            if WORD[i] == letter:
                guess[i] = letter

    # TODO: update the strike counter if an incorrect letter was guessed
    # TODO: exit the program if there are a certain number of strikes

    print(" ".join(guess))


# TODO: make a message congratulating the player if they win
# TODO: make a loop that lets users play another game
# TODO: draw a hangman figure using keyboard characters
