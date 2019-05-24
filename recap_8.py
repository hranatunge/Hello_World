# Recap 8
# Tuples
numbers = (45, 46, 47)
print(f"Agent {numbers[2]}")

# The unpacking feature in Python
# Can be used with lists as well
coordinates = (6.8522, 79.9249)
x, y = coordinates
print(f"x: {x}° N y: {y}° E")

# Dictionaries in Python
# Each key should be listed once
targets = {
    "name": "Hashan Ranatunge",
    "alias": "VanGoghs Mango",
    "age": 28,
    "is_verified": True
}

print(f"Target name: {targets['name']}")
print(f"Alias: {targets['alias']}")
print(f"D.O.B.: {targets.get('birthdate', 'Jan 1 1970')}")
targets['alias'] = "Vizual Desperado"
print(f"Target alias: {targets['alias']}")

# A small program using dictionaries
# A dictionary to store all the digits
phone_numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight"
}

phone = input("Phone:\n")
output = ""
for cha in phone:
    # '!' is a replacement
    output += phone_numbers.get(cha, "!") + " "
print(output)

# Emoji converter program
message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "🙂",
    ":(": "☹️",
    "(:": "🙃",
    ";)": "😉",
    "¯\_(ツ)_/¯": "🤷"
}
msg = ""

for word in words:
    msg += emojis.get(word, word) + " "
print(msg)
