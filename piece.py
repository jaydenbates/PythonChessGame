class Piece():
    # impliment a name of the pice for the printing 
    # in this class you can change the color and add self.name
    # clean up code
    # text: f"\u001b[38;2;{r};{g};{b}m", dark brown = f"\u001b[38;2;78;53;36m", cream = f"\u001b[38;2;255;243;154m"

    def __init__(self, player):
        # player1 is False, player2 is True
        self.player = player

    def isMoveValid(self, board, currentPlace, nextPlace):
        return False

    def player(self):
        return self.player

    def __str__(self, isPositionWhite):
        if isPositionWhite:
            if self.player:
                return "\x1b[0;33;47m" + self.pieceName + "\x1b[0m" 
            else:
                return "\x1b[0;35;47m" + self.pieceName + "\x1b[0m" 
        else:
            if self.player:
                return "\x1b[0;33;40m" + self.pieceName + "\x1b[0m" 
            else:
                return "\x1b[0;35;40m" + self.pieceName + "\x1b[0m" 


    def pieceDirection(self, currentPlace, nextPlace):
        if currentPlace[0] == nextPlace[0] and currentPlace[1] != nextPlace[1]:
            if currentPlace[1] > nextPlace[1]: # piece is moving left
                return "left"
            else:
                return "right" # piece is moving right
        elif currentPlace[1] == nextPlace[1] and currentPlace[0] != nextPlace[0]:
            if currentPlace[0] > nextPlace[0]:
                return "up" # piece is moving up
            else:
                return "down" # piece is moving down
        else:
            # need to do math for diagonal then else for if not then completle wrong
            amountDiag = abs(currentPlace[0] - nextPlace[0])
            # TODO: need to add the direction it is going diagonal
            if amountDiag == abs(nextPlace[1] - currentPlace[1]):
                return "diagonal"
            # not a valid move
            else:
                return "notValid"
            

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        if way == "diagonal":
            # why do I have currentplace just need position
            print(position)
            if board[position[0]][position[1]] == None:
                return True
            else: 
                print("you cant move past a piece")
                return False
        else:
            if way == "right" or way == "left":
                if board[currentPlace[0]][position[0]] == None:
                    return True
                else: 
                    print("you cant move past a piece")
                    return False
            else: 
                if board[position[0]][currentPlace[1]] == None:
                    return True
                else: 
                    print("you cant move past a piece")
                    return False
    
    def replacePiece(self, board, currentPlace, nextPlace):
        if board[nextPlace[0]][nextPlace[1]] != None:
            # piece there
            if board[nextPlace[0]][nextPlace[1]].player == self.player:
                print("cannot move there. You already have a piece there")
                return False
            else:
                board[nextPlace[0]][nextPlace[1]] = None
                board[nextPlace[0]][nextPlace[1]] = self
                board[currentPlace[0]][currentPlace[1]] = None
                self.currentPlace = [nextPlace[0], nextPlace[1]]
        else:
            # changing all the values in the same column no idea why
            board[nextPlace[0]][nextPlace[1]] = board[currentPlace[0]][currentPlace[1]]
            board[currentPlace[0]][currentPlace[1]] = None
            self.currentPlace = [nextPlace[0], nextPlace[1]]

class Rook(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.pieceName = "R"

    def isMoveValid(self, board, currentPlace, nextPlace):
        way = self.pieceDirection(currentPlace, nextPlace)
        replace = False
        if way != "diagonal" and way != "notValid":
            if way == "up":
                for i in range(nextPlace[0] + 1, currentPlace[0]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == currentPlace[0] - 1: # no piece in the way
                            replace = True
                    else: 
                        print("there is a piece in the way, up")
                        return False

                # no piece in the next place
                if replace == True:
                    return self.replacePiece(board, currentPlace, nextPlace)
                else:
                    print("error in isMoveValid on going up")
                    return False

            elif way == "down":
                for i in range(currentPlace[0] + 1, nextPlace[0]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == nextPlace[0] - 1: # no piece in the way
                            replace = True
                    else: 
                        print("there is a piece in the way, down")
                        return False

                # no piece in the next place
                if replace == True:
                    self.replacePiece(board, currentPlace, nextPlace)
                    return True
                else:
                    print("error in isMoveValid on going down")
                    return False
                    
            elif way == "left":
                for i in range(nextPlace[1] + 1, currentPlace[1]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == currentPlace[1] - 1: # no piece in the way
                            replace = True
                    else: 
                        print("there is a piece in the way, left")
                        return False
                    # no piece in the next place
                if replace == True:
                    self.replacePiece(board, currentPlace, nextPlace)
                    return True
                else:
                    print("error in isMoveValid on going left")
                    return False
            else:
                # moving right
                for i in range(currentPlace[1] + 1, nextPlace[1]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == nextPlace[1] - 1: # no piece in the way
                            replace = True
                    else: 
                        print("there is a piece in the way, right")
                        return False
                    # no piece in the next place
                if replace == True:
                    self.replacePiece(board, currentPlace, nextPlace)
                    return True
                else:
                    print("error in isMoveValid on going right")
                    return False
        else:
            print("A Rook cannot move to that spot")
            return False     

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForPiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)
            

class Knight(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.pieceName = "K"

    def isMoveValid(self, board, currentPlace, nextPlace):
        # valid move
        if currentPlace[0] == nextPlace[0] + 2 or currentPlace[0] == nextPlace[0] - 2 or currentPlace[1] == nextPlace[1] + 2 or currentPlace[1] == nextPlace[1] - 2:
            self.replacePiece(board, currentPlace, nextPlace)
            return True
        else:
            print("not a valid move please try again")
            return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i, way):
        return super().checkForPiece(board, currentPlace, nextPlace, i,)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)


class Bishop(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.pieceName = "B"

    def isMoveValid(self, board, currentPlace, nextPlace):
        way = self.pieceDirection(currentPlace, nextPlace)
        replace = False
        if way == "diagonal":
            # down right
            if currentPlace[0] < nextPlace[0] and currentPlace[1] < nextPlace[1]:
                if currentPlace[0] == nextPlace[0] - 1 and currentPlace[1] == nextPlace[1] - 1:
                    replace = True
                else:
                    for i in range(currentPlace[0], nextPlace[0] - 1):
                        if self.checkForPiece(board, currentPlace, nextPlace, [currentPlace[0] + i, currentPlace[1] + i], way):
                            replace = True
            # down left
            elif currentPlace[0] < nextPlace[0] and currentPlace[1] > nextPlace[1]:
                # moving one place
                if currentPlace[0] == nextPlace[0] - 1 and currentPlace[1] == nextPlace[1] + 1:
                    replace = True
                else:
                    for i in range(nextPlace[0], currentPlace[0] - 1):
                        if self.checkForPiece(board, currentPlace, nextPlace, [currentPlace[0] + i, currentPlace[1] - i], way):
                            replace = True 
            # up right
            elif currentPlace[0] > nextPlace[0] and currentPlace[1] < nextPlace[1]:
                if currentPlace[0] == nextPlace[0] + 1 and currentPlace[1] == nextPlace[1] - 1:
                    replace = True
                else:
                    for i in range(nextPlace[0], currentPlace[0] - 1):
                        if self.checkForPiece(board, currentPlace, nextPlace, [currentPlace[0] - i, currentPlace[1] + i], way):
                            replace = True 
            # up left
            elif currentPlace[0] > nextPlace[0] and currentPlace[1] > nextPlace[1]:
                if currentPlace[0] == nextPlace[0] + 1 and currentPlace[1] == nextPlace[1] + 1:
                    replace = True
                else:
                    for i in range(nextPlace[0], currentPlace[0] - 1):
                        if self.checkForPiece(board, currentPlace, nextPlace, [currentPlace[0] - i, currentPlace[1] - i], way):
                            replace = True 
            else:
                print("not a valid move in diagonal")
                return False

            if replace:
                if board[nextPlace[0]][nextPlace[1]] != None:
                    if board[nextPlace[0]][nextPlace[1]].player == self.player:
                        print("you cant move to your own piece")
                        return False
                    else:
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                else:
                    self.replacePiece(board, currentPlace, nextPlace)
                    return True
        else:
            print("This is not a valid move before diagonal")
            return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForPiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)


class Pawn(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.firstMove = True
        self.pieceName = "P"

    def isMoveValid(self, board, currentPlace, nextPlace):
        # player 2
        replace = False
        # up and down
        if self.player and currentPlace[1] == nextPlace[1]:
                if self.firstMove and nextPlace[0] == self.currentPlace[0] + 2: # first move and moves two places
                    for i in range(currentPlace[0] + 1, nextPlace[0]): 
                        if not self.checkForPiece(board, currentPlace, nextPlace, [i], way="down"): # checking for pieces in the way
                            print("This is not a valid pawn move there is a piece in the way (moving two places)")
                            return False
                elif nextPlace[0] == self.currentPlace[0] + 1:
                    if not self.checkForPiece(board, currentPlace, nextPlace, [currentPlace[0] + 1], way="down"):
                            print("This is not a valid pawn move there is a piece in the way (moving one place)")
                            return False
                else:
                    print("this is not a valid pawn move, you can only move down two if it is your pawns first move or one if it has used it's first move")
                    return False

                self.firstMove = False
                self.replacePiece(board,currentPlace,nextPlace)
                return True

        # player 1
        elif not self.player and currentPlace[1] == nextPlace[1]:
            if self.firstMove and nextPlace[0] == self.currentPlace[0] - 2: # first move and moves two places
                print("we made it here")
                for i in range(nextPlace[0] + 1, currentPlace[0]):
                    if not self.checkForPiece(board, currentPlace, nextPlace, [i], way="up"):
                        print("This is not a valid pawn move there is a piece in the way (moving two places)")
                        return False
            elif nextPlace[0] == self.currentPlace[0] - 1:
                if not self.checkForPiece(board, currentPlace, nextPlace, [currentPlace[0] - 1], way="up"):
                    print("This is not a valid pawn move there is a piece in the way (moving one place)")
                    return False
            else:
                print("this is not a valid pawn move, you can only move up two if it is your pawns first move or one if it has used it's first move")
                return False

            self.firstMove = False
            self.replacePiece(board,currentPlace,nextPlace)
            return True

        #attacking piece
        else:
            if self.player:
                # down left and down right
                if board[nextPlace[0]][nextPlace[1]].player != self.player:
                    if (currentPlace[1] + 1 == nextPlace[1] and currentPlace[0] + 1 == nextPlace[0]) or (currentPlace[1] - 1 == nextPlace[1] and currentPlace[0] + 1 == nextPlace[0]):
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                else:
                    print("this is not a valid attacking pawn move for player 2")
                    return False
            else:
                if board[nextPlace[0]][nextPlace[1]].player != self.player:
                    if (currentPlace[1] + 1 == nextPlace[1] and currentPlace[0] - 1 == nextPlace[0]) or (currentPlace[1] - 1 == nextPlace[1] and currentPlace[0] - 1 == nextPlace[0]):
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                else:
                    print("this is not a valid attacking pawn move for player 1")
                    return False
        

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForPiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)


class King(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.pieceName = "K"

    def isMoveValid(self, board, currentPlace, nextPlace):
        # up and down
        if currentPlace[0] == nextPlace[0]:
            # down
            if currentPlace[1] + 1 == nextPlace[1]:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            # up
            elif currentPlace[1] - 1 == nextPlace[1]:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            else:
                print("not a valid move")
                return False
        # right and left
        elif currentPlace[1] == nextPlace[1]:
            # right
            if currentPlace[0] + 1 == nextPlace[0]:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            # left
            elif currentPlace[0] - 1 == nextPlace[0]:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            else:
                print("not a valid move")
                return False
        # diagonal
        else:
            # down left
            if currentPlace[0] == nextPlace[0] + 1 and currentPlace[1] == nextPlace[1] + 1:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            # down right
            elif currentPlace[0] == nextPlace[0] + 1 and currentPlace[1] == nextPlace[1] - 1:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            # up left
            elif currentPlace[0] == nextPlace[0] - 1 and currentPlace[1] == nextPlace[1] + 1:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            # up right
            elif currentPlace[0] == nextPlace[0] - 1 and currentPlace[1] == nextPlace[1] - 1:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            else:
                print("this is not a valid move")
                return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        return super().checkForPiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)


class Queen(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.pieceName = "Q"

    def isMoveValid(self, board, currentPlace, nextPlace):
        way = self.pieceDirection(currentPlace, nextPlace)
        replace = False
        if way != "diagonal" and way != "notValid":
            if way == "up":
                for i in range(nextPlace[0] + 1, currentPlace[0]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == currentPlace[0] - 1: # no piece in the way
                            replace == True
                    else: 
                        return False

            elif way == "down":
                for i in range(currentPlace[0] + 1, nextPlace[0]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == nextPlace[0] - 1: # no piece in the way
                            replace == True
                    else: 
                        print("there is a piece in the way")
                        return False
                    
            elif way == "left":
                for i in range(nextPlace[1] + 1, currentPlace[1]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == currentPlace[1] - 1: # no piece in the way
                            replace == True
                    else: 
                        print("there is a piece in the way")
                        return False
            else:
                # moving right
                for i in range(currentPlace[1] + 1, nextPlace[1]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == nextPlace[1] - 1: # no piece in the way
                            replace == True
                    else: 
                        print("there is a piece in the way")
                        return False

        elif way == "diagonal":
            position = currentPlace
            # down right
            if currentPlace[0] < nextPlace[0] and currentPlace[1] < nextPlace[1]:
                if currentPlace[0] == nextPlace[0] + 1:
                    replace = True
                for i in range(currentPlace[0] + 1, nextPlace[0]):
                    position[0] += 1
                    position[1] += 1
                    if self.checkForPiece(board, currentPlace, nextPlace, position, way):
                        replace = True
            # down left
            elif currentPlace[0] < nextPlace[0] and currentPlace[1] > nextPlace[1]:
                # moving one place
                if currentPlace[0] == nextPlace[0] + 1:
                    replace = True
                for i in range(nextPlace[0] + 1, currentPlace[0]):
                    position[0] += 1
                    position[1] -= 1
                    if self.checkForPiece(board, currentPlace, nextPlace, position, way):
                        replace = True 
            # up right
            elif currentPlace[0] > nextPlace[0] and currentPlace[1] < nextPlace[1]:
                if currentPlace[0] == nextPlace - 1:
                    replace = True
                for i in range(currentPlace[0] + 1, nextPlace[0]):
                    position[0] -= 1
                    position[1] += 1
                    if self.checkForPiece(board, currentPlace, nextPlace, position, way):
                        replace = True 
            # up left
            elif currentPlace[0] > nextPlace[0] and currentPlace[1] > nextPlace[1]:
                if currentPlace[0] == nextPlace - 1:
                    replace = True
                for i in range(nextPlace[0] + 1, currentPlace[0]):
                    position[0] -= 1
                    position[1] -= 1
                    if self.checkForPiece(board, currentPlace, nextPlace, position, way):
                        replace = True 
            else:
                print("not a valid move")
                return False
        else:
            print("A queen cannot move to that spot")
            return False   

        if replace:
                if board[nextPlace[0]][nextPlace[1]] != None:
                    if board[nextPlace[0]][nextPlace[1]].player == self.player:
                        print("you cant move to your own piece")
                        return False
                    else:
                        self.replacePiece(board, currentPlace,nextPlace, isReplacing=True)
                        return True
                else:
                    self.replacePiece(board, currentPlace, nextPlace, isReplacing=False)
                    return True

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForPiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)
