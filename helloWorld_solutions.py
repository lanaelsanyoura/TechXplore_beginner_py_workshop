# Print Hello
print("Hello World")

# Store the name of the user in a variable
name = "Lana"
print(name)

# Store different types of variables and print them
age = 22
print(age)

height = 1.59
print(height)

# Print "Hello <name>"
print("Hello " + name)

# Create a new variable, greeting, with the whole greeting message
# print(greeting) --> "How are you, <name>"
greeting = "How are you, " + name
print(greeting)

# How old would we be in 20 years?
age_in_20 = age + 20
print(age_in_20)

# Take user input and let's see if they can vote
# name = input("What is your name? ")
# print("Hello " + name)
#
# age = int(input("How old are you? "))
#
# if age > 18:
#     print("You can vote!")
# elif age < 17:
#     print("Sorry you're too young to vote")
# else:
#     print("One more year till you can vote!")

# If Statements with Booleans
if True:
    print("If statement passes")
if False:
    print("This will never print")

## Booleans as a result of a comparison
#print(age > 18)
#print(age < 18)
## And we can store them in variables
canVote = age >= 18
print(canVote)

if canVote:
    print("Assessing variable canVote")

# Sometimes we want a list of numbers or names
# Let's create a workshop class list
celebs = ["Drake", "Ariana Grande", "Bruno Mars"]
print(celebs[0])

celebs.append("Miley Cyrus")
print(celebs)

print(len(celebs))

# But sometimes we need to access information based on the data itself
# DICTIONARIES
# dict = { key1: value1, key2: value2 ... , keyN: valueN }
fruit_to_sugar = {"apple": 11, "banana": 18, "strawberry": 7}

# Accessing the elements from the dictionary based on keys:
# v = dict[key]
sugar_in_apple = fruit_to_sugar["apple"]
print("this is the sugar in apples: ", sugar_in_apple)

# Adding a new value in the dict is:
# dict[key] = value
fruit_to_sugar["orange"] = 21

print(fruit_to_sugar)

# Keys need to be unique, so adding the same key will just update the value
fruit_to_sugar["apple"] = 0
print(fruit_to_sugar)

# How can we go ove each element in the list? A For Loop
# print every element in the list
for celeb in celebs:
    print(celeb)

# looping by index
for i in range(5):
    print(i)

# loop over all celebrities using range(len(celebs))
for i in range(len(celebs)):
    print(celebs[i])

# We can also manipulate elements
# Only print the elements that are less than 5
for num in [0,1,2,3,4,5,6,7]:
    if num < 5:
        print(num)


# While loops
print("While Loops")
i = 0
while i < 10:
    print(i)
    i += 1
