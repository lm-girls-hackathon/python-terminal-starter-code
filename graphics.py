import pygame

word = "hello"
guess = ["_"] * len(word)

WIDTH = 500
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # this assigns the `letter` variable to the key that the user pressed
            letter = event.unicode
            if letter in word:
                # updates the guess to include the known letter
                for i, l in enumerate(word):
                    if l == letter:
                        guess[i] = letter
            else:
                # TODO: what should you do if they guess a letter that isn't in the word?
                pass

    # this makes the screen blue - you can change the rgb values to change the color
    screen.fill(color=(192, 255, 238))

    # TODO: draw a hangman!

    font = pygame.font.SysFont(None, 24)
    img = font.render(" ".join(guess), True, pygame.Color(0, 0, 255))
    # change the coordinates below to adjust the position of the text
    screen.blit(img, (250, 250))

    # TODO: draw the letters that they have already guessed
    # TODO: add check for if they have correctly guessed the word
    pygame.display.flip()

pygame.quit()
