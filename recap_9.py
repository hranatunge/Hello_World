# Recap 10
# Functions


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}.\nWelcome aboard!")


def age_calculator(x, y):
    z = x -y
    print(f"Age: {z}")


def number_squared(x):
    return x * x


def emoji_converter(text):
    words = text.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "☹️",
        "(:": "🙃",
        ";)": "😉",
        "¯\_(ツ)_/¯": "🤷"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


# Leave 2 blank lines after defining a function (a python thing)
print("start")
greet_user("Jack", "Black")
print("End")
print("*" * 36)
# Keyword arguments - Good for numerical arguments and improves the readability of the code
# Pass keyword arguments after the positional arguments in functions
print("Start Age Calculator")
age_calculator(2019, y=1991)
print("End")
print("*" * 36)
# Using the return statements
print("Start Number Squared")
print(f"7 squared: {number_squared(7)}")
print("End")
print("*" * 36)
# Using the emoji converter function
print("Start Emoji Converter")
message = input("> ")
print(emoji_converter(message))
print("End")
print("*" * 36)
