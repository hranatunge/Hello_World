# A simple text based car game
command = ""
started = False
user_help = '''
start - To start the car
stop - To stop the car
quit - To quit the game
'''

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("The car started...")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("The car stopped...")
    elif command == "help":
        print(user_help)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand this!")
