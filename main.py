from pieces import *

class HVHgameInstance:
	def __init__(self, whosTurn) -> None:
		if self.whosTurn == "Human"
		self.whosTurn = ""
		self.winner = ''

	def printBoard(self):
		
		print( f'''
		{pieces['a'][1]}|{pieces['a'][2]}|{pieces['a'][3]}
		-+-+-
		{pieces['b'][1]}|{pieces['b'][2]}|{pieces['b'][3]}
		-+-+-
		{pieces['c'][1]}|{pieces['c'][2]}|{pieces['c'][3]}
		''')
	def checkCases(self) -> str:
		# TODO Make Winning Possible
		# winning cases

		# Diagonal
		if pieces['a'][1] == "x" and pieces['b'][1] == "x" and pieces['c'][1] == "x":
			self.winner = "Human" 	
			return self.winner
		if pieces['a'][1] == "o" and pieces['b'][1] == "o" and pieces['c'][1] == "o":
			self.winner = "AI" 	
			return self.winner

		if pieces['a'][2] == "x" and pieces['b'][2] == "x" and pieces['c'][2] == "x":
			self.winner = "Human"
			return self.winner
		if pieces['a'][2] == "o" and pieces['b'][2] == "o" and pieces['c'][2] == "o":
			self.winner = "AI"
			return self.winner 

		if pieces['a'][3] == "x" and pieces['b'][3] == "x" and pieces['c'][3] == "x":
			self.winner = "Human"
			return self.winner
		if pieces['a'][3] == "o" and pieces['b'][3] == "o" and pieces['c'][3] == "o":
			self.winner = "AI"
			return self.winner
		
		# Vertical
		if pieces['a'][1] == "x" and pieces['a'][2] == "x" and pieces['a'][3] == "x":
			self.winner = "Human"
			return self.winner
		if pieces['a'][1] == "o" and pieces['a'][2] == "o" and pieces['a'][3] == "o":
			self.winner = "AI"
			return self.winner

		if pieces['b'][1] == "x" and pieces['b'][2] == "x" and pieces['b'][3] == "x":
			self.winner = "Human"
			return self.winner
		if pieces['b'][1] == "o" and pieces['b'][2] == "o" and pieces['b'][3] == "o":
			self.winner = "AI"
			return self.winner

		if pieces['c'][1] == "x" and pieces['c'][2] == "x" and pieces['c'][3] == "x":
			self.winner = "Human"
			return self.winner
		if pieces['c'][1] == "o" and pieces['c'][2] == "o" and pieces['c'][3] == "o":
			self.winner = "AI"
			return self.winner

		if pieces['a'][1] == "x" and pieces['b'][2] == "x" and pieces['c'][3] == "x":
			self.winner = "Human"
			return self.winner
		if pieces['a'][1] == "o" and pieces['b'][2] == "o" and pieces['c'][3] == "o":
			self.winner = "AI"
			return self.winner

		if pieces['c'][1] == "x" and pieces['b'][2] == "x" and pieces['a'][3] == "x":
			self.winner = "Human"
			return self.winner
		if pieces['c'][1] == "o" and pieces['b'][2] == "o" and pieces['a'][3] == "o":
			self.winner = "AI"
			return self.winner
	
		if self.winner == "Human": print("The Winner is The Human")
		if self.winner == "AI": print("The Winner is The AI")

	def AITurn(self):
		#  TODO impliment my Algorithm
		self.whosTurn = "Human"
		row, column = input("enter row:"), input("enter column:")
		pieces[str(row)][int(column)] = "o"
		self.printBoard()
		print(f"{pieces}")

	def humanTurn(self):
		self.whosTurn = "AI"
		row, column = input("enter row:"), input("enter column:")
		pieces[str(row)][int(column)] = "x"
		self.printBoard()
		print(f"{pieces}")

	def mainLoop(self):
		
		# TODO Make Pieces Quantifiable
		while True:
			if self.checkCases():
				if self.winner == "Human": print("The Winner is The Human")
				if self.winner == "AI": print("The Winner is The AI")
				break

			print(f"It is the {self.whosTurn}'s turn ")
			if self.whosTurn == "Human":
				self.humanTurn()
			self.AITurn()

	def main(self):
		self.mainLoop()
	
if __name__=="__main__":
	k = input("Which game mode would you like to play:Human vs Human or Human vs AI\n: ")
	if k ==  
	newInstance = HVHgameInstance("Human")
	newInstance.main()

