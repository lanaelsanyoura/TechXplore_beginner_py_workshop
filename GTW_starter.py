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

theme_to_activity = {"A": "What activity would you do first?\n H. Hiking\n S. Swimming",
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

    Return the target word and lives based on the specifications
    """

    #1. Ask the user what them they are interested in
    #theme = input(...)

    # Get the word list based on these themes
    #word_list = ...

    # Choose a random word from the list
    # HINT: random.choice(list) returns a random element
    #word = ...

    # Ask them what activity they'd like to do
    #activity = ...

    # Update the lives accordin to their answer
    #lives = ...

    # return the target word and lives
    return "python", 3 #TODO: only for building purposes

# 1. Initialize game state to playing and parameters and blank target word
game_state = True
valid_letters = ["a", "b", "c", "d", "e",
                 "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o",
                 "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y",
                 "z"]
used_letters = []

# 2. Choose and set the target word and lives
target_word, lives = "", 0 #TODO

# 3. Create a blank word list for the user to update based on word length
built_word = []

#TODO: set built_word

# 2. Keep asking for new letters until the word is correct
# while(...)
while (game_state == True):
    # Print the status of the game
    print("Letters left: ", valid_letters)
    print("Letters used: ", used_letters)
    print("lives: ", lives)

    print("".join(built_word))
    # Ask the user for a letter
    letter = "" #TODO

    # Remove the letter from the valid alphabet ONLY if it's there:
    # Add the letter to the used
    if letter in valid_letters:
        #TODO
        pass

    # check if the letter is in the target word
    #TODO
    # if ...
        # Let the user know they're right
        # print(GREEN + "correct!" + BLACK) # TODO: uncomment this

        # Add the letter to the word we're building at the correct index
        # HINT: you can get the index of a list element by: string.index(element)

    # But if they lost, subtract one life
    #el..
        # Subtract one life
        #TODO:
        # Tell them they're incorrect
        # print(RED + "wrong!" + BLACK) #TODO: uncomment this
    # If they've used all their lives, game over
    # OR if they got all the letters correctly, they win!

    #if ...
        #print(RED + "Game Over," + BLACK  + "the correct word is: ", target_word)

    #elif "".join(built_word) == target_word:
        #print(PINK + "You Won!" + BLACK)
        #print("The correct word is: ", target_word)
        #
    game_state = False # TODO: this is just so we don't have an infinite loop