from pieces import *

class gameInstance:
	def __init__(self) -> None:
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
		if pieces['a'][1] and pieces['b'][1] and pieces['c'][1]:
			if self.whosTurn == "Human": 
				self.winner = "Human"
				return self.winner
			if self.whosTurn == "AI":
				self.winner = "AI" 	
				return self.winner
		if pieces['a'][2] and pieces['b'][2] and pieces['c'][2]:
			if self.whosTurn == "Human": 
				self.winner = "Human"
				return self.winner
			if self.whosTurn == "AI":
				self.winner = "AI"
				return self.winner 

		if pieces['a'][3] and pieces['b'][3] and pieces['c'][3]:
			if self.whosTurn == "Human": 
				self.winner = "Human"
				return self.winner
			if self.whosTurn == "AI":
				self.winner = "AI"
				return self.winner
		
		# Vertical
		if pieces['a'][1] and pieces['a'][2] and pieces['a'][3]:
			if self.whosTurn == "Human": 
				self.winner = "Human"
				return self.winner
			if self.whosTurn == "AI":
				self.winner = "AI"
				return self.winner

		if pieces['b'][1] and pieces['b'][2] and pieces['b'][3]:
			if self.whosTurn == "Human":
				self.winner = "Human"
				return self.winner
			if self.whosTurn == "AI":
				self.winner = "AI"
				return self.winner

		if pieces['c'][1] and pieces['c'][2] and pieces['c'][3]:
			if self.whosTurn == "Human": 
				self.winner = "Human"
				return self.winner
			if self.whosTurn == "AI":
				self.winner = "AI"
				return self.winner

		if pieces['a'][1] and pieces['b'][2] and pieces['c'][3]:
			if self.whosTurn == "Human": 
				self.winner = "Human"
				return self.winner
			if self.whosTurn == "AI":
				self.winner = "AI"
				return self.winner

		if pieces['c'][1] and pieces['b'][2] and pieces['a'][3]:
			if self.whosTurn == "Human": 
				self.winner = "Human"
				return self.winner
			if self.whosTurn == "AI":
				self.winner = "AI"
				return self.winner
		
		if self.winner == "Human": print("The Winner is The Human")
		if self.winner == "AI": print("The Winner is The AI")
		else:
			pass
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

	def mainLoop(self, whosTurn):
		# TODO Make Pieces Quantifiable
		running = True
		while running:
			if self.checkCases() == "Human":
				running = False
			if self.checkCases() == "Human":
				running = False
			print(f"It is the {self.whosTurn}'s turn ")
			if self.whosTurn == "Human":
				self.humanTurn()
			self.AITurn()

	def main(self):
		self.mainLoop("Human")
	

if __name__=="__main__":
	newInstance = gameInstance()
	newInstance.main()

