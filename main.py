from AIInstace import HVAgameInstance
# from ComputerAlgorithm import 
from HInstance import HVHgameInstance



if __name__ == "__main__":
    gameMode = input(
        "~~Which game mode would you like to play~~\n1 : Human VS Human\n2 : Human VS AI\n:"
    )
    Statistics = input("Would you like extra crap in your screen?\nyes or no\n:")
    if gameMode == 1:
        whoseFirst = input("~~Who's Going First~~\n1 : Player1\n 2 : Player2\n:")
        game = HVHgameInstance(str(whoseFirst))
        game.main()
    else:
        whoseFirst = input("~~Who's Going First~~\n1 : Human\n2 : AI\n:")
        game = HVAgameInstance(str(whoseFirst))
        game.main()
