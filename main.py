print("Welcome to Python Chess Game")
notDone = True
while notDone:
    play = str(input("Are you ready to play? y/n")).lower()
    if play == "y":
        pass
    else:
        done = str(input("are you wanting to exit the game? y/n")).lower()
        if done == "y":
            notDone = False