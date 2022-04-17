from pieces import *


class HVHgameInstance:
    def __init__(self, whosTurn) -> None:
        # if self.whosTurn == "Human"
        self.whosTurn = ""
        self.winner = ""

    def printBoard(self):
        print(
            f"""
		{board['1']}|{board['2']}|{board['3']}
		-+-+-
		{board['4']}|{board['5']}|{board['6']}
		-+-+-
		{board['7']}|{board['8']}|{board['9']}
		"""
        )

    def checkCasesP1(self) -> str:
        if (
            board["1"] == "x"
            and board["2"] == "x"
            and board["3"] == "x"
            or board["4"] == "x"
            and board["5"] == "x"
            and board["6"] == "x"
            or board["7"] == "x"
            and board["8"] == "x"
            and board["9"] == "x"
            or board["1"] == "x"
            and board["4"] == "x"
            and board["6"] == "x"
            or board["2"] == "x"
            and board["5"] == "x"
            and board["8"] == "x"
            or board["3"] == "x"
            and board["6"] == "x"
            and board["9"] == "x"
            or board["1"] == "x"
            and board["5"] == "x"
            and board["9"] == "x"
            or board["3"] == "x"
            and board["5"] == "x"
            and board["7"] == "x"
        ):
            self.winner == "Player1"
            return self.winner

    def checkCasesP2(self) -> str:
        if (
            board["1"] == "o"
            and board["2"] == "o"
            and board["3"] == "o"
            or board["4"] == "o"
            and board["5"] == "o"
            and board["6"] == "o"
            or board["7"] == "o"
            and board["8"] == "o"
            and board["9"] == "o"
            or board["1"] == "o"
            and board["4"] == "o"
            and board["6"] == "o"
            or board["2"] == "o"
            and board["5"] == "o"
            and board["8"] == "o"
            or board["3"] == "o"
            and board["6"] == "o"
            and board["9"] == "o"
            or board["1"] == "o"
            and board["5"] == "o"
            and board["9"] == "o"
            or board["3"] == "o"
            and board["5"] == "o"
            and board["7"] == "o"
        ):
            self.winner == "Player2"
            return self.winner

    def Player1(self):
        print("The Compass:\n    1 2 3\n    4 5 6\n    7 8 9\n")
        human = input("Enter a number:")
        board[str(human)] = "o"
        self.printBoard()
        print(f"{board}")
        self.whosTurn = "Player1"

    def Player2(self):
        print("The Compass:\n    1 2 3\n    4 5 6\n    7 8 9\n")
        human = input("Enter a number:")
        board[str(human)] = "x"
        self.printBoard()
        print(f"{board}")
        self.whosTurn = "Player2"

    def mainLoop(self):
        # TODO Make board Quantifiable
        while True:
            if self.checkCasesP1():
                if self.winner == "Player1":
                    print("The Winner is The Human")
                break
            if self.checkCasesP2():
                if self.winner == "Player2":
                    print("The Winner is The AI")
                break
            print(f"It is the {self.whosTurn}'s turn ")
            if self.whosTurn == "Human":
                self.humanTurn()
            self.Player2()

    def main(self):
        self.mainLoop()
