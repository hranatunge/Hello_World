# Recap 3
# Formatted Strings
# Need to import Math for this one
import math

# Variables
firstName = "John"
lastName = "Smith"
rapperName = "mf doom"
course = "Python for beginners"
message = firstName + " [" + lastName + "] is a programmer."
print(message)
print("*" * 36)

# Formatted Strings make it easier to visualize the concept
msg = f"{firstName} [{lastName}] is a programmer."
print(msg)
print("*" * 36)

# String Methods
# The length of the lastName
print(len(lastName))
# Convert into all caps
# ALL CAPS when you spell the man's name :)
allCaps = rapperName.upper()
print(allCaps)
print("*" * 36)

# The Find and replace method
rapper = (rapperName.find("doom"))
# Prints out the index where the word 'doom' begins
print(rapper)
# The replace method
newTitle = course.replace("beginners", "noobs")
print(newTitle)
print("*" * 36)

# The 'in' operator returns a boolean value
a = "Python" in course
print(a)
print("*" * 36)

# Python math operators
x = 10
# x squared
y = x ** 3
print(y)
print("*" * 36)

x += 3
print(x)
print("*" * 36)

x -= 3
print(x)
print("*" * 36)

x = (2 + 3) * 10 - 3
print(x)
print("*" * 36)

# Using the Python Math function
i = 3.134
j = -243
# Rounding a float number
print(round(i))
# Getting the absolute number - without positive negative
print(abs(j))
# Return the floor of i as a float
print(math.floor(i))
