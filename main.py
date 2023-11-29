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
            nextPosXY = [8 - int(input("where would you like to move Y-axis: ")), int(input("where would you like to move X-axis: ")) - 1]
            if currentPosXY[0] < 8 and currentPosXY[1] >= 0 and nextPosXY[0] < 8 and nextPosXY[1] >= 0:
                game.move(currentPosXY, nextPosXY)
                valid = True
            else:
                print("This is not a place on the table")
                # break
        except Exception as e:
            print(f"the move was unsuccessful {e}")
            user_input = str(input(f'would you like to exit: '))
            if user_input == 'y':
                valid = True
                done = True

    # if game.check():
    #     pass
    # else:
    #     pass
    # if game.promotion():
    #     pass
    # make move


