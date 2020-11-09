import numpy as np


class Player:
    def __init__(self, name):
        self.name = name

    def score(self):
        print("%s score is %d" % self.name, self.score)


def generate_string(size):  # create initial current string display
    game_word = ["_ "] * size
    letters_left = size
    return game_word, letters_left


def check_letter(letter, game_word, correct_word, letters_left):  # check whether input letter is correct
    correct_np = np.array(list(correct_word))   # convert the correct word string into a numpy array
    if letter in correct_np:
        print("correct guess")
        correct_positions = np.where(correct_np == letter)[0]   # store the correct positions in c_positions
        for i in correct_positions:  # for each position in correct positions array
            game_word[i] = letter  # correct positions = [0 2]
        letters_left -= len(correct_positions)  # decrease the remaining by the value of correctly guessed slots
        print(letters_left)
    else:
        print("wrong guess mate")
    return letters_left


def play_game():
    game_finish = 0
    lives_remaining = 8
    correct_word = "cockawoo"  # WORD GENERATION
    game_word, letters_left = generate_string(len(correct_word))  # returns two variables, board and score needed
    while game_finish == 0:
        print(game_word)
        if letters_left == 0:
            print("game is finished")
            game_finish = 1
        # guess a letter, switch between players
        letter = input()[0]  # input one character at a time
        letters_left = check_letter(letter, game_word, correct_word, letters_left)


print("Welcome challengers\nInput")
while 1:
    play_game()
    print("Play agan?\nY/N")
    play_again = input()[0]
    if play_again == 'Y':
        continue
    else:
        break
print("Game ended")
