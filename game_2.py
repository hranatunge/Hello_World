# Weight converter 1.0


def weight_converter(x, cha):
    if cha == "K":
        converted = float(x) * 2.205
        print(f"Your weight is: {str(converted)} lbs")
    elif cha == "L":
        converted = float(x) / 2.205
        print(f"Your weight is: {str(converted)} kg")
    else:
        print("Please enter 'l' for lbs or 'k' for kg")


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


user_weight = input("Please enter your weight:\n> ")
unit = input("lbs (l) or kg (k)?\n> ")
upper_unit = unit.upper()
weight_converter(user_weight, upper_unit)
print("*" * 36)
comment = input("Enter your text here\n> ")
print(emoji_converter(comment))
print("*" * 36)
