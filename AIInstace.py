from pieces import *
#TODO # why don't you map o to 1 and empty or x to (or empty to 0 and x to -1) and sum row/column? If it's 3 than win (or -3 for x)

class HVAgameInstance:
	def __init__(self, whosTurn) -> None:
		# if self.whosTurn == "Human"
		self.whosTurn = ""
		self.winner = ''

	def printBoard(self):
		print( f'''
		{board['1']}|{board['2']}|{board['3']}
		-+-+-
		{board['4']}|{board['5']}|{board['6']}
		-+-+-
		{board['7']}|{board['8']}|{board['9']}
		''')

	def checkCasesHuman(self) -> str:
		if( board['1'] == "x" and board['2'] == "x" and board['3'] == "x" or
			board['4'] == "x" and board['5'] == "x" and board['6'] == "x" or
			board['7'] == "x" and board['8'] == "x" and board['9'] == "x" or
			board['1'] == "x" and board['4'] == "x" and board['6'] == "x" or
			board['2'] == "x" and board['5'] == "x" and board['8'] == "x" or
			board['3'] == "x" and board['6'] == "x" and board['9'] == "x" or
			board['1'] == "x" and board['5'] == "x" and board['9'] == "x" or
			board['3'] == "x" and board['5'] == "x" and board['7'] == "x"
			):
			self.winner = "Human"
			return self.winner 

	def checkCasesBot(self) -> str:
		if (board['1'] == "o" and board['2'] == "o" and board['3'] == "o" or
			board['4'] == "o" and board['5'] == "o" and board['6'] == "o" or
			board['7'] == "o" and board['8'] == "o" and board['9'] == "o" or
			board['1'] == "o" and board['4'] == "o" and board['6'] == "o" or
			board['2'] == "o" and board['5'] == "o" and board['8'] == "o" or
			board['3'] == "o" and board['6'] == "o" and board['9'] == "o" or
			board['1'] == "o" and board['5'] == "o" and board['9'] == "o" or
			board['3'] == "o" and board['5'] == "o" and board['7'] == "o"
			):
			self.winner = "AI"
			return self.winner
	
	def minimax(self,board, depth, isMaximising):
		if self.checkCasesBot(): return 1
		if self.checkCasesHuman() : return -1

		if isMaximising == True:
			bestScore = -800
			for key in board.keys():

				if board[key] == " ":
					board[key] = "o"
					score = self.minimax(board,depth +1, False)
					board[key] = ''
					if score > bestScore:
						bestScore = score
				return bestScore

		else:

			bestScore = 800
			for key in board.keys():
				if board[key] == " ":
					board[key] = "o"
					score = self.minimax(board,depth +1, False)
					board[key] = ''
					if score > bestScore:
						bestScore = score
				return bestScore
						
	def AITurn(self):
		self.whosTurn = "Human"
		bestScore = -800
		bestMove = 0
		for key in board.keys():
			if board[key] == " ":
				score = self.minimax(board, 0, False)
				if score > bestScore:
					bestScore = score
					bestMove = key
		board[str(bestMove)] = 'o'
		
		self.printBoard()
		print(f"{board}")

	def humanTurn(self):
		
		print("The Compass:\n    123\n    456\n    789\n")
		human = input("Enter a number:")
		board[str(human)] = "x"
		self.printBoard()
		print(f"{board}")
		self.whosTurn = "AI"

	def mainLoop(self):
		# TODO Make board Quantifiable
		while True:
			if self.checkCasesHuman():
				if self.winner == "Human": print("The Winner is The Human")
				break
			if self.checkCasesBot():
				if self.winner == "AI": print("The Winner is The AI")
				break
			print(f"It is the {self.whosTurn}'s turn ")
			if self.whosTurn == "Human":
				self.humanTurn()
			self.AITurn()
	def main(self):
		self.mainLoop()

