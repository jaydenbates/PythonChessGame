from pyrsistent import b


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
        if currentPlace[0] == nextPlace[0]:
            if currentPlace[1] < nextPlace[1]: # piece is moving left
                return "left"
            else:
                return "right" # piece is moving right
        elif currentPlace[1] == nextPlace[1]:
            if currentPlace[0] < nextPlace[0]:
                return "up" # piece is moving up
            else:
                return "down" # piece is moving down
        else:
            # need to do math for diagonal then else for if not then completle wrong
            amountDiag = abs(currentPlace[0] - nextPlace[0])
            if amountDiag == abs(currentPlace[1] - nextPlace[1]):
                return "diagonal"
            # not a valid move
            else:
                return "notValid"
            

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        if board[currentPlace[0]][i] == None:
            return True
        elif board[currentPlace[0]][i] == board[nextPlace[0]][nextPlace[1]]:
            return True
        else: 
            print("you cant move past a piece")
            return False

    def replacePiece(self, board, currentPlace, nextPlace, isReplacing):
        if isReplacing:
            board[nextPlace[0]][nextPlace[1]] = None
            board[nextPlace[0]][nextPlace[1]] = self
            board[currentPlace[0]][currentPlace[1]] = None
            self.currentPlace = [nextPlace[0], nextPlace[1]]
        else:
            board[nextPlace[0]][nextPlace[1]] = self
            board[currentPlace[0]][currentPlace[1]] = None
            self.currentPlace = [nextPlace[0], nextPlace[1]]

class Rook(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        way = super.pieceDirection(currentPlace, nextPlace)
        replace = False
        if way != "diagonal" and way != "notValid":
            if way == "up":
                for i in range(currentPlace[0] + 1, nextPlace[0] - 1):
                    if self.checkForPiece(board, currentPlace, nextPlace, i): # if true no piece in the way
                        if i == nextPlace[0] - 1: # no piece in the way
                            replace == True
                    else: 
                        return False

                # no piece in the next place
                if replace == True:
                    if board[nextPlace[0]][nextPlace[1]] != None:
                        # piece there
                        if board[nextPlace[0]][nextPlace[1]].player == self.player:
                            print("cannot move there. You already have a piece there")
                            return False
                        else:
                            self.replacePiece(board,currentPlace,nextPlace,isReplacing=True)
                            return True
                    else:
                        self.replacePiece(board,currentPlace,nextPlace,isReplacing=False)
                        return True
                else:
                    print("error in isMoveValid")
                    return False

            elif way == "down":
                for i in range(nextPlace[0] + 1, currentPlace[0] - 1):
                    if self.checkForPiece(board, currentPlace, nextPlace, i): # if true no piece in the way
                        if i == currentPlace[0] - 1: # no piece in the way
                            replace == True
                    else: 
                        print("there is a piece in the way")
                        return False

                # no piece in the next place
                if replace == True:
                    if board[nextPlace[0]][nextPlace[1]] != None:
                        # piece there
                        if board[nextPlace[0]][nextPlace[1]].player == self.player:
                            print("cannot move there. You already have a piece there")
                            return False
                        else:
                            self.replacePiece(board,currentPlace,nextPlace,isReplacing=True)
                            return True
                    else:
                        self.replacePiece(board,currentPlace,nextPlace,isReplacing=False)
                        return True
                else:
                    print("error in isMoveValid")
                    return False
                    
            elif way == "left":
                for i in range(nextPlace[1] + 1, currentPlace[0] - 1):
                    if self.checkForPiece(board, currentPlace, nextPlace, i): # if true no piece in the way
                        if i == currentPlace[0] - 1: # no piece in the way
                            replace == True
                    else: 
                        print("there is a piece in the way")
                        return False
                    # no piece in the next place
                if replace == True:
                    if board[nextPlace[0]][nextPlace[1]] != None:
                        # piece there
                        if board[nextPlace[0]][nextPlace[1]].player == self.player:
                            print("cannot move there. You already have a piece there")
                            return False
                        else:
                            self.replacePiece(board,currentPlace,nextPlace,isReplacing=True)
                            return True
                    else:
                        self.replacePiece(board,currentPlace,nextPlace,isReplacing=False)
                        return True
                else:
                    print("error in isMoveValid")
                    return False
            else:
                # moving right
                for i in range(currentPlace[1] + 1, nextPlace[1] - 1):
                    if self.checkForPiece(board, currentPlace, nextPlace, i): # if true no piece in the way
                        if i == currentPlace[0] - 1: # no piece in the way
                            replace == True
                    else: 
                        print("there is a piece in the way")
                        return False
                    # no piece in the next place
                if replace == True:
                    if board[nextPlace[0]][nextPlace[1]] != None:
                        # piece there
                        if board[nextPlace[0]][nextPlace[1]].player == self.player:
                            print("cannot move there. You already have a piece there")
                            return False
                        else:
                            self.replacePiece(board,currentPlace,nextPlace,isReplacing=True)
                            return True
                    else:
                        self.replacePiece(board,currentPlace,nextPlace,isReplacing=False)
                        return True
                else:
                    print("error in isMoveValid")
                    return False
        else:
            print("A Rook cannot move to that spot")
            return False     

    def pieceDirection(self, currentPlace, nextPlace):
        super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        super().checkForPiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace, isReplacing):
        super().replacePiece(board, currentPlace, nextPlace, isReplacing)
            


class Knight(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        way = self.pieceDirection(currentPlace,nextPlace)
        # valid move
        if currentPlace[0] == nextPlace[0] + 2 or currentPlace[0] == nextPlace[0] - 2 or currentPlace[1] == nextPlace[1] + 2 or currentPlace[1] == nextPlace[1] - 2:
            if board[nextPlace[0]][nextPlace[1]] != None:
                if board[nextPlace[0]][nextPlace[1]].player != self.player:
                    self.replacePiece(board, currentPlace, nextPlace, isReplacing=True)
                    return True
                else:
                    print("You cannot move to your own piece")
                    return False
            else:
                self.replacePiece(board, currentPlace, nextPlace, isReplacing=False)
                return True
        else:
            print("not a valid move please try again")
            return False

    def pieceDirection(self, currentPlace, nextPlace):
        super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        super().checkForPiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace, isReplacing):
        super().replacePiece(board, currentPlace, nextPlace, isReplacing)

class Bishop(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        pass

    def pieceDirection(self, currentPlace, nextPlace):
        super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        super().checkForPiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace, isReplacing):
        super().replacePiece(board, currentPlace, nextPlace, isReplacing)

class Pawn(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        if self.player == True:
            pass

    def pieceDirection(self, currentPlace, nextPlace):
        super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        super().checkForPiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace, isReplacing):
        super().replacePiece(board, currentPlace, nextPlace, isReplacing)

class King(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        pass

    def pieceDirection(self, currentPlace, nextPlace):
        super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        super().checkForPiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace, isReplacing):
        super().replacePiece(board, currentPlace, nextPlace, isReplacing)

class Queen(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace

    def isMoveValid(self, board, currentPlace, nextPlace):
        pass

    def pieceDirection(self, currentPlace, nextPlace):
        super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, i):
        super().checkForPiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace, isReplacing):
        super().replacePiece(board, currentPlace, nextPlace, isReplacing)