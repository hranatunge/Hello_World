# Existential Quotes
print("Generate A Random Existential Quote")
print("*" * 36)

quote_1 = '''
"There is scarcely any passion without struggle."
- Albert Camus
'''
quote_2 = '''
"I rebel; therefore I exist."
- Albert Camus
'''

quote_3 = '''
"I rebel; therefore I exist."
- Albert Camus
'''

quote_4 = '''
"The world is, of course, nothing but our conception of it."
― Anton Chekhov
'''

quote_5 = '''
"The world is, of course, nothing but our conception of it."
― Anton Chekhov
'''

quote_6 = '''
"The world is, of course, nothing but our conception of it."
― Anton Chekhov
'''

quote_7 = '''
"The world is, of course, nothing but our conception of it."
― Anton Chekhov
'''

quote_8 = '''
"The world is, of course, nothing but our conception of it."
― Anton Chekhov
'''

quote_9 = '''
"The world is, of course, nothing but our conception of it."
― Anton Chekhov
'''

quote_0 = '''
"The world is, of course, nothing but our conception of it."
― Anton Chekhov
'''

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you ran out of guesses :(")
print("*" * 36)
