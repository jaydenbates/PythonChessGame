""" TODO: ADD Try Catch to find errors but not crash game. 
        -- pawn move piece needs to be fixed on attach section. if it is not self.player then it could be none
             -- add better error statments 
        -- encapsolate the code so it is not so long. maybe add another class of movement and add all that there.
        -- add feature clastling 
        -- consider changing true false to 1 and 0 for player 1 and 2
        -- implement turns for player 1 and 2

        Diagonals dont work
"""
class Piece():

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
        amountDiag = abs(currentPlace[0] - nextPlace[0])
        if currentPlace[0] == nextPlace[0] and currentPlace[1] != nextPlace[1] and currentPlace[1] > nextPlace[1]:
            return "left" # moving left
        elif currentPlace[0] == nextPlace[0] and currentPlace[1] != nextPlace[1] and currentPlace[1] < nextPlace[1]:
            return "right" # moving right
        elif currentPlace[1] == nextPlace[1] and currentPlace[0] != nextPlace[0] and currentPlace[0] > nextPlace[0]:
            return "up" # moving up
        elif currentPlace[1] == nextPlace[1] and currentPlace[0] != nextPlace[0] and currentPlace[0] < nextPlace[0]:
            return "down" # moving down
        elif amountDiag == abs(nextPlace[1] - currentPlace[1]) and currentPlace[0] < nextPlace[0] and currentPlace[1] < nextPlace[1]:
            return "down right" # down right
        elif amountDiag == abs(nextPlace[1] - currentPlace[1]) and currentPlace[0] < nextPlace[0] and currentPlace[1] > nextPlace[1]:
            return "down left" # down left
        elif amountDiag == abs(nextPlace[1] - currentPlace[1]) and currentPlace[0] > nextPlace[0] and currentPlace[1] < nextPlace[1]:
            return "up right" # up right
        elif amountDiag == abs(nextPlace[1] - currentPlace[1]) and currentPlace[0] > nextPlace[0] and currentPlace[1] > nextPlace[1]:
            return "up left"
        else:
            return "notValid"

            
    def checkForAndReplacePiece(self, board, currentPlace, nextPlace, direction):
        if direction == "up":
            for i in range(nextPlace[0] + 1, currentPlace[0]):
                if board[i][currentPlace[1]] == None:
                    if i == currentPlace[0] - 1: # no piece in the way
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                else: 
                    print("there is a piece in the way (direction == up)")
                    return False
        elif direction == "down":
            for i in range(currentPlace[0] + 1, nextPlace[0]):
                if board[i][currentPlace[1]] == None:
                    if i == nextPlace[0] - 1: # no piece in the way
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                else: 
                    print("there is a piece in the way (direction == down)")
                    return False
        elif direction == "left":
            for i in range(nextPlace[1] + 1, currentPlace[1]):
                if board[currentPlace[0]][i] == None:
                    if i == currentPlace[1] - 1: # no piece in the way
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                else: 
                    print("there is a piece in the way (direction == left)")
                    return False
        elif direction == "right":
            for i in range(currentPlace[1] + 1, nextPlace[1]):
                if board[currentPlace[0]][i] == None:
                    if i == nextPlace[1] - 1: # no piece in the way
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                else: 
                    print("there is a piece in the way (direction == right)")
                    return False
        elif direction == "down right":
            if currentPlace[0] == nextPlace[0] - 1 and currentPlace[1] == nextPlace[1] - 1:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            else:
                for i in range(currentPlace[0] - currentPlace[0] + 1, (nextPlace[0] - currentPlace[0])):
                    # TODO: need to check if there is a piece in the way and then before the last square return true
                    if board[i][i] == None:
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                    else: 
                        print("there is a piece in the way (direction == down right)")
                        return False
        elif direction == "down left":
            if currentPlace[0] == nextPlace[0] - 1 and currentPlace[1] == nextPlace[1] + 1:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            else:
                for i in range(currentPlace[0] - currentPlace[0] + 1, (nextPlace[0] - currentPlace[0])):
                    if board[i][i] == None:
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                    else: 
                        print("there is a piece in the way (direction == down left)")
                        return False
        elif direction == "up right":
            if currentPlace[0] == nextPlace[0] + 1 and currentPlace[1] == nextPlace[1] - 1:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            else:
                for i in range(nextPlace[0] - nextPlace[0] + 1, (currentPlace[0] - nextPlace[0])):
                    if board[i][i] == None:
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                    else: 
                        print("there is a piece in the way (direction == up right)")
                        return False
        elif direction == "up left":
            if currentPlace[0] == nextPlace[0] + 1 and currentPlace[1] == nextPlace[1] + 1:
                self.replacePiece(board, currentPlace, nextPlace)
                return True
            else:
                for i in range(nextPlace[0] - nextPlace[0] + 1, (currentPlace[0] - nextPlace[0])):
                    print(range(nextPlace[0] - nextPlace[0] + 1, (currentPlace[0] - nextPlace[0])))
                    if board[i][i] == None:
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                    elif board[i][i] == True: 
                        print("there is a piece in the way (direction == up left)")
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

        direction = self.pieceDirection(currentPlace, nextPlace)

        if direction == "up" || direction == "down" || direction == "left" || direction == "right":
            if self.checkForAndReplacePiece(board, currentPlace, nextPlace, direction):
                return True
        else:
            print("this is not a valid move for a Rook")
            return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForAndReplacePiece(self, board, currentPlace, nextPlace, way):
        return super().checkForAndReplacePiece(board, currentPlace, nextPlace, way)

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
            print("not a valid move for a knight. Please try again")
            return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForAndReplacePiece(self, board, currentPlace, nextPlace, way):
        return super().checkForAndReplacePiece(board, currentPlace, nextPlace, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)


class Bishop(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.pieceName = "B"

    def isMoveValid(self, board, currentPlace, nextPlace):
        direction = self.pieceDirection(currentPlace, nextPlace)
        if direction == "down right" || direction == "down left" || direction == "up right" || direction == "up left":
            if self.checkForAndReplacePiece(board, currentPlace, nextPlace, direction):
                return True
        else:
            print("not a valid move in diagonal, Bishop")
            return False

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForAndReplacePiece(self, board, currentPlace, nextPlace, way):
        return super().checkForAndReplacePiece(board, currentPlace, nextPlace, way)

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
                    if not self.checkForPiece(board, currentPlace, nextPlace, way="up"):
                        print("This is not a valid pawn move there is a piece in the way (moving two places)")
                        return False
            elif nextPlace[0] == self.currentPlace[0] - 1:
                if not self.checkForPiece(board, currentPlace, nextPlace, way="up"):
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
            elif not self.player:
                if board[nextPlace[0]][nextPlace[1]].player != self.player:
                    if (currentPlace[1] + 1 == nextPlace[1] and currentPlace[0] - 1 == nextPlace[0]) or (currentPlace[1] - 1 == nextPlace[1] and currentPlace[0] - 1 == nextPlace[0]):
                        self.replacePiece(board, currentPlace, nextPlace)
                        return True
                else:
                    print("this is not a valid attacking pawn move for player 1")
                    return False
            else: 
                print("this is not a valid move for a pawn")
                return False
        

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForPiece(self, board, currentPlace, nextPlace, way):
        return super().checkForAndReplacePiece(board, currentPlace, nextPlace, way)

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
        return super().checkForAndReplacePiece(board, currentPlace, nextPlace, i)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)


class Queen(Piece):
    def __init__(self, player, currentPlace):
        self.player = player
        self.currentPlace = currentPlace
        self.pieceName = "Q"

    def isMoveValid(self, board, currentPlace, nextPlace):
        direction = self.pieceDirection(currentPlace, nextPlace)
        replace = False

        if direction == "up" || direction == "down" || direction == "left" || direction == "right" || direction == "down right" || direction == "down left" || direction == "up right" || direction == "up left":
            if self.checkForAndReplacePiece(board, currentPlace, nextPlace, direction):
                return True

    def pieceDirection(self, currentPlace, nextPlace):
        return super().pieceDirection(currentPlace, nextPlace)

    def checkForAndReplacePiece(self, board, currentPlace, nextPlace, position, way):
        return super().checkForAndReplacePiece(board, currentPlace, nextPlace, position, way)

    def replacePiece(self, board, currentPlace, nextPlace):
        super().replacePiece(board, currentPlace, nextPlace)
