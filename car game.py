command= input("Type a command:")
output=""
com = {
    "Start": "car started","Stop": " car stopped","Right": "car turned right","Left": "to turn the car left","Drift": "car drifted"}
while command!="Exit":
    if command == "help":
        print("Start: to Start the car \nStop: to stop the car \nRight: to turn the car right \nLeft: to turn the car left \nDrift:to drift \nExit: To quit the game")
    elif command in output:
        print('Already done! ')
    elif command in com:
        print(com.get(command))
        output += command
    else:
        print("Unknown command.")
    command = input("Type a command:")





