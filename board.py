class Board():
    def __init__(self):
        self.board = []
        self.Player1 = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        self.Player2 = ["R", "N", "B", "K", "Q", "B", "N", "R"]
        for i in range(8):
            self.board.append([])
            for j in range(8):
                if i == 0:
                    self.board[i].append("\033[0;34m" + self.Player1[j])
                elif i == 1:
                    self.board[i].append("\033[0;34m" + "P")
                elif i == 6:
                    self.board[i].append("\033[0;37m" + "P")
                elif i == 7:
                    self.board[i].append("\033[0;37m" + self.Player2[j])
                else:
                    self.board[i].append(" ")


    def drawBoard(self):
        boardLength = 8
        print("  *", end="")
        for i in range(len(self.board)):
            print("****", end="")
        print()
        for i in range(len(self.board)):
            print(f"{boardLength - i:<2}|", end="")
            for j in range(len(self.board[i])):
                if self.board[i][j] != " ":
                    print(f"{self.board[i][j]:^11}|", end="")
                else:
                    print(f"{self.board[i][j]:^3}|", end="")
            print()
        print("  *", end="")
        for i in range(len(self.board)):
            print("****", end="")
        print()
        print("   ", end="")
        for i in range(len(self.board)):
            print(f"{i + 1:^4}", end="")