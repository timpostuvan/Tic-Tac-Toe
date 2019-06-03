from tkinter import *
import tkinter.messagebox as messagebox

class Game:
	char = {-1 : '-', 0 : 'O', 1 : 'X'}

	def __init__(self):
		self.table = [[-1] * 3 for i in range(3)]
		self.player = 0
		self.turn = 0
		self.end = 0


	def __str__(self):
		s = ""
		for i in range(3):
			s = s + "|".join(self.char[self.table[i][j]] for j in range(3))
			s = s + "\n" 

		return s

	def possibleMove(self, x_position, y_position):
		if(self.table[x_position][y_position] == -1):
			return True

		return False


	def makeMove(self, x_position, y_position):
		self.turn += 1
		self.table[x_position][y_position] = self.player
		self.player = 1 - self.player

		print(self)


	def checkTable(self):
		for i in range(3):						#check rows
			cur = self.table[i][0]
			for j in range(3):
				if(cur != self.table[i][j]):
					cur = -1

			if(cur != -1):
				return cur


		for j in range(3):						# check columns
			cur = self.table[0][j]
			for i in range(3):
				if(cur != self.table[i][j]):
					cur = -1

			if(cur != -1):
				return cur


		cur = self.table[0][0]					# check first diagonal 
		for i in range(3):
			if(cur != self.table[i][i]):
				cur = -1

		if(cur != -1):
			return cur


		cur = self.table[2][0]					# check second diagonal
		for i in range(3):
			if(cur != self.table[2 - i][i]):
				cur = -1

		if(cur != -1):
			return cur

		return -1



class GUI:

	def __init__(self):
		self.window = Tk()
		self.window.title("Tic Tac Toe")
		self.window.geometry('450x600')
		self.window.resizable(False, False)
		self.game = Game()

		self.label = Label(self.window, font=("Helvetica", 40))
		self.label.grid(row=0, columnspan=3, sticky=E+W)
		self.label['text'] = "Player: O"

		for i in range(4):
			self.window.rowconfigure(i, weight=1)

		for i in range(3):
			self.window.columnconfigure(i, weight=1)

		self.buttons = list()
		for i in range(3):
			self.buttons.append([])
			for j in range(3):
				self.buttons[i].append(Button(self.window, command=lambda a = i, b = j: self.clickButton(a, b)))
				self.buttons[i][j].grid(row=i + 1, column=j, sticky=N+S+E+W)
				self.buttons[i][j].config(width=150, font=("Helvetica", 60))

		self.window.mainloop()


	def setLabel(self, x_position, y_position):
		if(self.game.player == 0):
			self.buttons[x_position][y_position]['text'] = 'O'
		
		else:
			self.buttons[x_position][y_position]['text'] = 'X'



	def playAgain(self):
		choice = messagebox.askquestion("Tic Tac Toe", "Do you want to play again?")
		self.window.destroy()
		
		if(choice == "yes"):
			self.__init__()


	def checkWinner(self):
		winner = self.game.checkTable()
		if(winner == 0):
			messagebox.showinfo("Tic-Tac-Toe", "Player O won")
			print("player O won")
			self.playAgain()
			return 1

		if(winner == 1):
			messagebox.showinfo("Tic-Tac-Toe", "Player X won")
			print("player X won")
			self.playAgain()
			return 1

		if(winner == -1 and self.game.turn == 9):
			messagebox.showinfo("Tic-Tac-Toe", "It is a tie")
			print("It is a tie")
			self.playAgain()
			return 1


	def clickButton(self, x_position, y_position):
		print(x_position, y_position)

		possible = self.game.possibleMove(x_position, y_position);	
		if(not possible):
			messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked! Click again")
			return

		self.setLabel(x_position, y_position)
		self.game.makeMove(x_position, y_position)

		if(self.checkWinner() == 1):
			return

		if(self.game.player == 0):
			self.label['text'] = "Player: O"
		else:
			self.label['text'] = "Player: X"


if(__name__ == "__main__"):
	TicTacToe = GUI()