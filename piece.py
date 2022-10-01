class Piece():
    def __init__(self, player):
        # player1 is False, player2 is True
        self.player = player

    def isMoveValid(self, board, currentPlace, nextPlace):
        return False

    def player(self):
        return self.player

    def __str__(self):
        pass

    def pieceDirection(self, currentPlace, nextPlace):
        if currentPlace[0] == nextPlace[0] and currentPlace[1] != nextPlace[1]:
            if currentPlace[1] < nextPlace[1]: # piece is moving left
                return "left"
            else:
                return "right" # piece is moving right
        elif currentPlace[1] == nextPlace[1] and currentPlace[0] != nextPlace[0]:
            if currentPlace[0] < nextPlace[0]:
                return "up" # piece is moving up
            else:
                return "down" # piece is moving down
        else:
            # need to do math for diagonal then else for if not then completle wrong
            amountDiag = abs(currentPlace[0] - currentPlace[1])
            # TODO: need to add the direction it is going diagonal
            if amountDiag == abs(nextPlace[0] - nextPlace[1]):
                return "diagonal"
            # not a valid move
            else:
                return "notValid"
            

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        if way == "diagonal":
            if board[currentPlace[position[0]]][position[1]] == None:
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
                return True
        else:
            board[nextPlace[0]][nextPlace[1]] = self
            board[currentPlace[0]][currentPlace[1]] = None
            self.currentPlace = [nextPlace[0], nextPlace[1]]
            return True

class Rook(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        way = super.pieceDirection(currentPlace, nextPlace)
        replace = False
        if way != "diagonal" and way != "notValid":
            if way == "up":
                for i in range(nextPlace[0] + 1, currentPlace[0]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == currentPlace[0] - 1: # no piece in the way
                            replace == True
                    else: 
                        return False

                # no piece in the next place
                if replace == True:
                    return self.replacePiece(board, currentPlace, nextPlace)
                else:
                    print("error in isMoveValid")
                    return False

            elif way == "down":
                for i in range(currentPlace[0] + 1, nextPlace[0]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == nextPlace[0] - 1: # no piece in the way
                            replace == True
                    else: 
                        print("there is a piece in the way")
                        return False

                # no piece in the next place
                if replace == True:
                    return self.replacePiece(board, currentPlace, nextPlace)
                else:
                    print("error in isMoveValid")
                    return False
                    
            elif way == "left":
                for i in range(nextPlace[1] + 1, currentPlace[1]):
                    if self.checkForPiece(board, currentPlace, nextPlace, [i], way): # if true no piece in the way
                        if i == currentPlace[1] - 1: # no piece in the way
                            replace == True
                    else: 
                        print("there is a piece in the way")
                        return False
                    # no piece in the next place
                if replace == True:
                    return self.replacePiece(board, currentPlace, nextPlace)
                else:
                    print("error in isMoveValid")
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
                    # no piece in the next place
                if replace == True:
                    return self.replacePiece(board, currentPlace, nextPlace)
                else:
                    print("error in isMoveValid")
                    return False
        else:
            print("A Rook cannot move to that spot")
            return False     

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForPiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        return super().replacePiece(board, currentPlace, nextPlace)
            

class Knight(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        # valid move
        if currentPlace[0] == nextPlace[0] + 2 or currentPlace[0] == nextPlace[0] - 2 or currentPlace[1] == nextPlace[1] + 2 or currentPlace[1] == nextPlace[1] - 2:
            return self.replacePiece(board, currentPlace, nextPlace)
        else:
            print("not a valid move please try again")
            return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i, way):
        return super().checkForPiece(board, currentPlace, nextPlace, i,)

    def replacePiece(self, board, currentPlace, nextPlace):
        return super().replacePiece(board, currentPlace, nextPlace)


class Bishop(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        way = self.pieceDirection(currentPlace, nextPlace)
        replace = False
        if way == "diagonal":
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
        else:
            print("This is not a valid move")
            return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForPiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        return super().replacePiece(board, currentPlace, nextPlace)


class Pawn(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.firstMove = True

    def isMoveValid(self, board, currentPlace, nextPlace):
        # player 2
        replace = False
        # up and down
        if self.player:
            if currentPlace[1] == nextPlace[1]:
                if self.firstMove and nextPlace[0] == self.currentPlace[0] + 2:
                    for i in range(currentPlace[0], nextPlace[0]):
                        if self.checkForPiece(board, currentPlace, nextPlace, [i], way="down"):
                            replace = True
                else:
                    if self.checkForPiece(board, currentPlace, nextPlace, [currentPlace[0] + 1], way="down"):
                            replace = True
                if replace:
                    self.replacePiece(board,currentPlace,nextPlace)
                    return True
                else:
                    print("this is not a valid move")
                    return False
            else:
                print("this is not a valid move")
                return False
        elif not self.player:
            if currentPlace[1] == nextPlace[1]:
                if self.firstMove and nextPlace[0] == self.currentPlace[0] - 2:
                    for i in range(currentPlace[0], nextPlace[0]):
                        if self.checkForPiece(board, currentPlace, nextPlace, [i], way="up"):
                            replace = True
                else:
                    if self.checkForPiece(board, currentPlace, nextPlace, [currentPlace[0] - 1], way="up"):
                            replace = True
                if replace:
                    self.replacePiece(board,currentPlace,nextPlace)
                    return True
                else:
                    print("this is not a valid move")
                    return False
            else:
                print("this is not a valid move")
                return False
        #attacking piece
        else:
            if self.player:
                # down left and down right
                if board[nextPlace[0]][nextPlace[1]] != self.player and (currentPlace[1] == nextPlace[1] + 1 and currentPlace[0] == nextPlace[0] + 1) or (currentPlace[1] == nextPlace[1] - 1 and currentPlace[0] == nextPlace[0] + 1):
                    self.replacePiece(board, currentPlace, nextPlace)
                    return True
                else:
                    print("this is not a valid move")
                    return False
            else:
                if board[nextPlace[0]][nextPlace[1]] != self.player and (currentPlace[1] == nextPlace[1] + 1 and currentPlace[0] == nextPlace[0] - 1) or (currentPlace[1] == nextPlace[1] - 1 and currentPlace[0] == nextPlace[0] - 1):
                    self.replacePiece(board, currentPlace, nextPlace)
                    return True
                else:
                    print("this is not a valid move")
                    return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForPiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        return super().replacePiece(board, currentPlace, nextPlace)


class King(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        pass

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        return super().checkForPiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace):
        return super().replacePiece(board, currentPlace, nextPlace)


class Queen(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        pass

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForPiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)
