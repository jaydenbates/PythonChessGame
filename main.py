from gamestate import GameState

game = GameState()
done = False
currentPosXY = []
nextPosXY = []
while not done:
    valid = False
    game.board.drawBoard()
    while not valid:
        try:
            currentPosXY = [8 - int(input("what piece would you like to move Y-axis: ")), int(input("what piece would you like to move X-axis: ")) - 1]
            if currentPosXY[0] < 8 and currentPosXY[1] >= 0:
                valid = True
            else:
                print("This is not a place on the table")
                break
            nextPosXY = [8 - int(input("where would you like to move Y-axis: ")), int(input("where would you like to move X-axis: ")) - 1]
            if nextPosXY[0] < 8 and nextPosXY[1] >= 0:
                valid = True
            else:
                print("This is not a place on the table")
                # break
        except:
            print("the move was unsuccessful")
    if valid:
        if game.move(currentPosXY, nextPosXY):
            pass
            # break
        else:
            print("that was not a valid move")
    # if game.check():
    #     pass
    # else:
    #     pass
    # if game.promotion():
    #     pass
    # make move


