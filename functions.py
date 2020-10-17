"""
This file will allow us to code with functions
Let's create a program that tells you a compliment whenever you call it
"""
#
# def function_name(argument1, argument2, argumentn):
#     # Function Body, all the code here will be run when we call this function
#     # .
#     # .
#     # .
#
#     # return statement, return any value that the caller can use
#     return any_value

#value = function_name(arg1, arg2, argn)


# example function definition:
def add(x,y):
    # return the sum of x and y
    return


# TODO: create a new function on your own:
# create a function that takes in a strings and adds all the words into a list
def to_list(string):
    """
    Given a string of words seperated by a space,
    return a list of words
    e.g. "Summer Fall Winter Spring" --> ["Summer", "Fall", "Winter", "Spring"]

    :param string: string of space separated words
    :return: list of words
    """
    # 1. each word will have a start and end
    start_index = 0
    end_index = 0
    list_of_words = []
    # 2. loop through every letter by index in this string
    # for i in range(len(string)):
        # if you find a space: this word is ending
            # next word starts after the space
            # add this word to the list based on the string slice

    # Add the last word as well
    return list_of_words


if __name__ == '__main__':
    a = 10
    b = 2
    # print the sum of these two variables
    # sum = add(a,b)
    # print(sum)

    c = 2
    d = 3
    # print the sum as well

    # Call your function to_list with any sentence of your choice

    # we can also do this with a built in string function: string.split()
