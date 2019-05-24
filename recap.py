# Recap 1
print("Hello World")

# drawing 36 stars in print
print("*" * 36)

# variables & data types
authorName = "Hashan Ranatunge"
codeName = "Vizual Desperado"
isHuman = True
authorAge = 27
rating = 4.7
rank = "noob"

# Getting user input
userName = input("What is your name?\n")
print("Hi " + userName)
usersMusic = input("What is your preferred genre of music?\n")
print(userName + " loves to listen to " + usersMusic + " :)")

print("*" * 36)

birthYear = input("What year were you born?\n")
# Convert the string into an integer to make the calculation
userAge = 2019 - int(birthYear)
# Print the data type of the 'birthYear'
print(type(birthYear))
# Print the data type of the 'userAge'
print(type(userAge))
# Convert 'userAge' back to a string
print(userName + " is " + str(userAge) + " years old.")

print("*" * 36)

# Weight Converter 1.0
userWeight = input("Please enter your weight (in lbs):\n")
inKilos = float(userWeight) / 2.205
print("Your weight in kg: " + str(inKilos))

print("*" * 36)
