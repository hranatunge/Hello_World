# Recap 2 - Important for interviews (string indexes)
# Strings
course = "Hashan's Python Course For Beginners"
print(course)
print("The first index of the string: " + course[0])
print("The last index of the string: " + course[-1])
print("The one before the last index of the string " + course[-2])

# Display the word 'Python' using the indexes of the string
print("The word 'Python' is after the index 9 and ends with index 15:\n" + course[9:15])

# Display from beginning to end using indexes
print(course[0:])

# After the 9th index
print(course[9:])

# The indexes up to 6
print(course[:6])

# The full string
title = course[:]
print(title)

aUserName = "Minoli"
# Displays 'Mino'
print(aUserName[0:-2])

print("*" * 36)

# A long ass string
poem = '''
Two Of Us
---
We can buy an apartment together.
A small one, we won't need much room.
It'll only be the two of us, maybe a dog.
We'll drink champagne and joke about being classy.

We'll chug beers and noisily laugh,
noisily kiss, noisily make love.
We'll hold hands, fall asleep together.

And in the morning we will head off to work.
Miss each other.
Then we will leave work, arrive home.
And we'll repeat.
'''
print(poem)

print("*" * 36)
