import random

# open the file "compliments.txt" in READ (r) mode
# compliments_file = ...

all_compliments = []

# Add every line in this file to a list, excluding \n
# NOTES: str.strip(arg) removes any leading char
# e.g. "HI   ".strip(" ") --> "HI"
# We want to remove the new line characters, "\n"
# for ...

# Create a function that gives the user a compliment based on their number
# of choice


# Step 1: define your function
def get_compliment(index):
    """
    >>> get_compliment(12)
    "You light up the room."
    :param index: the index of the compliments the user chooses
    :return: return the compliment at index index
    """
    # If the index is BIGGER than the length of the list, give an error message
        # exit the function

    # If not, return the compliments at the given index
    return # TODO: specify what we're returning

# Step 2: call your function
# comp2 = get_compliment(12) #example function call:
