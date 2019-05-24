# Recap 5
# For Loops

# Prints out all the indexes in the string / array
for item in "Python":
    print(item)

for bud in [4, 2, 0]:
    print(bud)
print("*" * 36)

# Prints out all the numbers in the range of numbers up to 10
for numbers in range(10):
    print(numbers)
print("*" * 36)

# Prints out all the numbers in the range 5 to 10 (increments in 2s)
for digits in range(5, 10, 2):
    print(digits)
print("*" * 36)

# Getting the total of an array
# Some variables
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"The total is: {total}")
print("*" * 36)

# An example of a nested loop
loopOutput = '''
0, 0
0, 1
0, 2
1, 0
1, 1
1, 2
2, 0
2, 1
2, 2
3, 0
3, 1
3, 2
'''
for x in range(4):
    for y in range(3):
        print(f"{x}, {y}")
print("*" * 36)

# Small challenge
numbers = [5, 2, 5, 2, 2]
letter = "x"

for digit in numbers:
    output = ""
    for count in range(digit):
        output += letter
    print(output)
