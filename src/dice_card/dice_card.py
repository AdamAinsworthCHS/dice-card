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



def show_cards():
	"""
	This method first shows the player's current score and dice
	then it shows every card the player has
	then it shows what cards the player has currently selected to play
	after giving this info, it calls the game_process method.
	"""
	print("")
	print("Score: " + str(Player.score))
	print("Dice: " + str(Player.dice))
	print("Cards in Hand:")
	for i in range (len(hand)):
		print(str(i + 1) + ": " + str(hand[i]))
	print("")
	print("Cards to be Played:")
	for i in range (len(playing)):
		print(str(i + 1) + ": " + str(playing[i]))
	game_process()
	return


def game_process():
	"""
	This method asks the player what command they wish to input
	typing roll rolls 1 die and draws that many cards
	typing a number plays that corresponding card
	typing play plays the current selected cards
	typing q quits the game.
	"""
	hand_length = len(hand)
	cards_play_length = len(playing)
	play_cards = input("Draw Cards ('roll') Play Card ('#') Play Hand ('play') Quit ('q'): ")
	try:
		play_cards = int(play_cards)
	except ValueError:
		if play_cards == "roll":
			if Player.dice >= 1:
				Player.dice -= 1
				for i in range(random.randrange(1, 7)):
					new_card = Deck.draw_card()
					hand.append(new_card)
				show_cards()
				return
			else:
				print("No dice remaining")
				game_process()
				return
		elif play_cards == "play":
			play_hand()
			return
		elif play_cards == "q":
			return
		else:
			print("Unrecognized command")
			show_cards()
			return
	if cards_play_length < 5:
			if play_cards > hand_length or play_cards <= 0:
				print("Card not found")
				game_process()
				return
			else:
				process(play_cards)
				return
	else:
		print("Max hand size is 5")
		game_process()
		return


def play_hand():
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
	show_cards()
	return


def process(play_cards):
	"""
	This method moves the card the player selected
	from the list of current cards into the 
	list of cards currently selected to be played.
	"""
	playing.append(hand[int(play_cards) - 1])
	hand.remove(hand[int(play_cards) - 1])
	show_cards()
	return


def main():
	"""
	This method gives the player 8 cards
	and begins the game.
	"""
	for i in range(8):
		new_card = Deck.draw_card()
		hand.append(new_card)
	show_cards()
	return

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Dice Card App")
		self.setContentsMargins(12, 12, 12, 12)
		self.resize(320, 240)

		layout = QVBoxLayout()

		# title
		title_label = QLabel("Dice Card App: a cooooool little game ;D.")

		# card buttons
		slot_1 = QPushButton("Empty")
		slot_2 = QPushButton("Empty")
		slot_3 = QPushButton("Empty")
		slot_4 = QPushButton("Empty")
		slot_5 = QPushButton("Empty")
		slot_6 = QPushButton("Empty")
		slot_7 = QPushButton("Empty")
		slot_8 = QPushButton("Empty")
		slot_1.clicked.connect(lambda: self.play_card(1))
		slot_2.clicked.connect(lambda: self.play_card(2))
		slot_3.clicked.connect(lambda: self.play_card(3))
		slot_4.clicked.connect(lambda: self.play_card(4))
		slot_5.clicked.connect(lambda: self.play_card(5))
		slot_6.clicked.connect(lambda: self.play_card(6))
		slot_7.clicked.connect(lambda: self.play_card(7))
		slot_8.clicked.connect(lambda: self.play_card(8))




		# add widgets & layouts to main layout
		layout.addWidget(title_label)
		layout.addWidget(slot_1)
		layout.addWidget(slot_2)
		layout.addWidget(slot_3)
		layout.addWidget(slot_4)
		layout.addWidget(slot_5)
		layout.addWidget(slot_6)
		layout.addWidget(slot_7)
		layout.addWidget(slot_8)
		widget = QWidget()
		widget.setLayout(layout)

		# Set the central widget of the Window.
		self.setCentralWidget(widget)
	
	def play_card(self, card_number):
		"""play the current button's card"""
		print(str(card_number))
		return


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()
	print(user)
	print(deck)
	main()

