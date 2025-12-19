"""
Dice Card Game
by Adam Ainsworth
"""
import random
from Card import Card
from Player import Player
from Hands import Hands
from Deck import Deck
import sys
from PySide6.QtWidgets import (
	QApplication,
	QLabel,
	QLineEdit,
	QMainWindow,
	QPushButton,
	QVBoxLayout,
	QWidget,
)

straight_flush = Hands(100, 5, "Straight Flush!")
four_of_a_kind = Hands(80, 4, "Four of a Kind.")
full_house = Hands(50, 3, "Full House.")
flush = Hands(40, 2, "Flush.")
straight = Hands(30, 2, "Straight.")
three_of_a_kind = Hands(25, 1, "Three of a Kind.")
two_pair = Hands(15, 1, "Two Pair.")
pair = Hands(10, 0, "Pair.")
high_card = Hands(0, 0, "High Card.")

deck = Deck(52)

user = Player("PlayerName")

#Main variables and lists
hand = []
playing = []

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Dice Card App")
		self.setContentsMargins(12, 12, 12, 12)
		self.resize(320, 240)

		self.main_layout = QVBoxLayout()

		# title
		title_label = QLabel("Dice Card App: a cooooool little game ;D.")

		# card buttons
		
		#dictionary thing
		self.slots_index = []

		# play hand button
		begin_game_button = QPushButton("Begin")
		begin_game_button.clicked.connect(lambda: self.begin_game())
		play_hand_button = QPushButton("Play Hand")
		play_hand_button.clicked.connect(lambda: self.play_hand())
		roll_die_button = QPushButton("Roll Die")
		roll_die_button.clicked.connect(lambda: self.roll_die())

		# add widgets & layouts to main layout
		self.main_layout.addWidget(title_label)
		self.main_layout.addWidget(begin_game_button)
		self.main_layout.addWidget(play_hand_button)
		self.main_layout.addWidget(roll_die_button)
		widget = QWidget()
		widget.setLayout(self.main_layout)

		# Set the central widget of the Window.
		self.setCentralWidget(widget)
	
	def play_card(self):
		"""
		This method moves the card the player selected
		from the list of current cards into the 
		list of cards currently selected to be played.
		"""
		card_number = int(self.sender().objectName)
		print(card_number)
		playing.append(hand[int(card_number) - 1])
		hand.remove(hand[int(card_number) - 1])
		self.update_cards()
		return
	
	def begin_game(self):
		"""
		This method updates each button to correctly represent
		the card in the hand it corresponds to.
		"""
		for i in range(len(hand)):
			card_slot = QPushButton()
			card_slot.setObjectName(str(i))
			card_slot.clicked.connect(lambda: self.play_card())
			self.slots_index.append(card_slot)
			self.main_layout.addWidget(card_slot)
		for i in range(len(self.slots_index)):
			print(self.slots_index[i])
		self.update_cards()


	def update_cards(self):
		"""
		This method updates each button to correctly represent
		the card in the hand it corresponds to.
		"""
		for i in range(len(hand)):
			try:
				self.slots_index[i].setText(hand[i].name)
			except IndexError:
				self.main_layout.removeWidget(self.slots_index[i])

	def roll_die(self):
		if Player.dice >= 1:
			Player.dice -= 1
			for i in range(random.randrange(1, 7)):
				new_card = Deck.draw_card()
				hand.append(new_card)
			self.update_cards()
			return
		else:
			print("No dice remaining")
			return
	
	def play_hand(self):
		"""
		This method takes the current selected cards and
		calculates them to see what kind of poker hand
		they are. Then it gives the player the requisite
		points and dice for that poker hand.
		Finally, it gives them points for each
		card played.
		"""
		print("Calculating hand...")
		if Hands.calculate_flush(playing) == True:
			if Hands.calculate_straight(playing) == True:
				straight_flush.process_hand()
				print(straight_flush)
			else:
				flush.process_hand()
				print(flush)
		elif Hands.calculate_kinds(playing) == 4:
			four_of_a_kind.process_hand()
			print(four_of_a_kind)
		elif Hands.calculate_full_house(playing) == True:
			full_house.process_hand()
			print(full_house)
		elif Hands.calculate_straight(playing) == True:
			straight.process_hand()
			print(straight)
		elif Hands.calculate_kinds(playing) == 3:
			three_of_a_kind.process_hand()
			print(three_of_a_kind)
		elif Hands.calculate_pairs(playing) == 2:
			two_pair.process_hand()
			print(two_pair)
		elif Hands.calculate_pairs(playing) == 1:
			pair.process_hand()
			print(pair)
		else:
			high_card.process_hand()
			print(high_card)
		for i in range (len(playing)):
			Player.score = Player.score + playing[i].point_value
		playing.clear()
		return


def main():
	"""
	This method gives the player 8 cards
	and begins the game.
	"""
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	for i in range(8):
		new_card = Deck.draw_card()
		hand.append(new_card)
	app.exec()
	return


if __name__ == "__main__":
	main()
	print(user)
	print(deck)
	

