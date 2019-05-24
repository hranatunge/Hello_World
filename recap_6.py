# Recap 6
# While Loops

print("Python For Beginners: While Loops")

x = 1
while x <= 10:
    print("*" * x)
    x += 1
print("DONE")
print("*" * 36)

# A simple guessing game
print("Guess a number")
print("*" * 36)
secret_no = 420
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess:\n"))
    guess_count += 1
    if guess == secret_no:
        print("You've guessed correct!")
        break
else:
    print(f"Sorry you've run out of guesses!\nThe secret number is {secret_no}")
