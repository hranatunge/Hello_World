# Recap 4
# Variable Operators
name = "Hashan"
print(len(name))
if len(name) < 3:
    print("Name must be at least 3 characters!")
elif len(name) > 50:
    print("Name must be less than 50 characters!")
else:
    print("Looks good")
print("*" * 36)

# Simple conditional program using if else statements
isHot = True
isCold = False
temperature = 30

if isHot:
    print("It's a hot day today.\nDrink plenty of water!")
elif isCold:
    print("It's cold outside.\nBundle up!")
else:
    print("It's a lovely day!")

# Comparison Operators
if temperature == 30:
    print("Goddamn it's hot in this motherfucker!!!")
else:
    print("It's an okay day.")

# House Down Payment Calculator 1.0
desc = '''
Price of a house is $ 1 Million
    They need to put down 10%
Otherwise
    they need to put down 20%
Print the down payment
'''
print("*" * 36)
print(desc)
print("*" * 36)
print("House down payment calculator")
print("*" * 36)

# variables
housePrice = 1000000
goodCredit = True
criminalRecord = False
highIncome = True

if goodCredit:
    downPayment = 0.1 * housePrice
else:
    downPayment = 0.2 * housePrice
print(f"Down payment: $ {downPayment}")

# Logical operators
if goodCredit and highIncome:
    print("You are eligible for a loan.")
elif goodCredit or highIncome:
    print("You are still eligible for a loan.")
else:
    print("Not eligible for a loan")

# Not operator
if goodCredit and not criminalRecord:
    print("Eligible AF")
else:
    print("Not eligible")
