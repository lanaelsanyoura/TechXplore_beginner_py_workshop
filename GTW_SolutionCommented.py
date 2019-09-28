import random

# The goal of the game is to solve the word puzzle

# We have a list of words that we need to read in the list

# Give the user a random word that they need to guess

# The rules of the game are:
# -- Guess the word

# Question 1: Where would you want to go on Vacation?
# --> Tropical Island : words related to beaches
    # --> What activity would you want to do first?
    # --> Hiking: 5
    # --> Swimming: 3

# --> City Scape : words related to cities
    # --> What would you rather do?
    # --> Night Out: 3
    # --> Movie Night: 4
# First let's build a regular guessing game
# assume no duplicate letters

# Let's set the data we need:
# the target word
# list of valid letters  (alphabet)
# number of chances
# number of letters in target word
# game state: playing or game over?

# Question: answers
theme_question = "Where would you like to go on vacation?\n A. Tropical Island\n B. City Scape"

theme_to_activity = {"A": "What would you do first?\n H. Hiking\n S. Swimming",
                   "B": "What would you rather do?\n N. Night out\n M. Movie Night In"}

activity_to_lives = {"H": 5, "S": 3, "N": 3, "M":4}

theme_to_words = {"A": ["beach","sand", "swim", "sun", "waves", "tide",
                        "shore", "light", "salt"],
                  "B": ["tower", "road", "sign", "light",
                        "show", "drink", "cup"]}

answers_to_questions = [
             {"A": {"What would you do first?": ["A. Hiking",
                                                 "B. Swimming"]},
             "B": {"What would you rather do":["A. Night out",
                                               "B. Movie Night In"]}},
             {"A": 3,
              "B": 5}
             ]

PINK = "\033[95m"
BLACK = '\033[30m'
GREEN = '\033[32m'
RED = '\033[31m'

def choose_target_word():
    """
    @:param environment: default is island
    @:param word_length: when it's None, any length is good

    Return the target word based on the environment and word length the user specifies
    """
    #
    # # We need to ask the user the questions we cared about
    # theme = input(theme_question + "\nyour answer: ")
    #
    # # Choose the word based on these themes
    # word_list = theme_to_words[theme]
    # word = random.choice(word_list)
    #
    # # Ask them what activity they'd like to do
    # activity = input(theme_to_activity[theme] + "\nyour answer: ")
    #
    # # update the lives
    # lives = activity_to_lives[activity]
    word,lives = "python", 3 # TODO: remove when you want to run
    return word, lives


# 1. Initialize game state to playing and parameters and blank target word
game_state = True
valid_letters = ["a", "b", "c", "d", "e",
                 "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o",
                 "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y",
                 "z"]
used_letters = []
# 2. Choose the target word and lives
target_word, lives = choose_target_word()

# 3. Create a * list for the user to update: python --> ["*","*","*","*","*"]
built_word = []
# for l in range(len(target_word)):
#     built_word.append(" * ")
# 2. Keep asking for new letters until the word is correct
# while(...)
while (game_state):
    # Print the status of the game
    print("Letters left: ", valid_letters)
    print("Letters used: ", used_letters)
    #print("lives: ", lives)
    print("".join(built_word))

    # # Ask the user for a letter
    # letter = input("Next letter? \n").lower() # make sure the letter is lower case
    #
    # # Remove the letter from the valid alphabet:
    # if letter in valid_letters:
    #     valid_letters.remove(letter)
    #     used_letters.append(letter)
    #
    # # check if the letter is in the target word
    # if letter in target_word:
    #     # Let the user know they're right
    #     print(GREEN + "correct!" + BLACK)
    #
    #     # Add the letter to the word we're building
    #     index = target_word.index(letter)
    #     # Add colour to the correct letters: "\033[1;32;"
    #     built_word[index] = letter
    # else:
    #     # Subtract one life
    #     lives = lives - 1
    #     # Tell them they're incorrect
    #     print(RED + "wrong!" + BLACK)
    # if lives == 0:
    #     print(RED + "Game Over," + BLACK  + "the correct word is: ", target_word)
    #     game_state = False
    # elif "".join(built_word) == target_word:
    #     print(PINK + "You Won!" + BLACK)
    #     print("The correct word is: ", target_word)
    #     game_state = False

    # TODO: remove following code when you want to uncomment
    game_state = False