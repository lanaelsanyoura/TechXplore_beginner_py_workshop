import random
all_compliments = []

compliments_file = open("compliments.txt", "r")
for line in compliments_file:
    all_compliments.append(line.strip("\n"))


# Step 1: define your function
def get_compliment(index):
    print("The user index is ", index)
    if index > len(all_compliments):
        print("Please choose an index smaller than ", len(all_compliments))
        return
    return all_compliments[index]

# Step 2: call your function
comp2 = get_compliment(2)
print(comp2)
