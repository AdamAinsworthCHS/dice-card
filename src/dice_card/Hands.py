"""
Hands Class
by Adam Ainsworth
"""
from Player import Player

class Hands:
	def __init__(self, score_given, dice_given, name):
		self.score_given = score_given
		self.dice_given = dice_given
		self.name = name

	
	def process_hand(self):
		"""
		This method gives the corresponding amount
		of dice and points for the given hand.
		"""
		Player.score += self.score_given
		Player.dice += self.dice_given
	
	
	def calculate_flush(playing):
		"""
		This method picks the first suit played and
		checks it against every other suit. If 
		all the suits match, it returns that
		the hand played is a flush.
		"""
		if len(playing) != 5:
			return False
		first_suit = playing[0].suit
		flush = True
		for i in range (len(playing)):
			if playing[i].suit != first_suit:
				flush = False
				break
		return flush

	
	def calculate_straight(playing):
		"""
		This method first sorts the current played
		hand by rank, and then checks if the gaps
		between each rank are 1. If this is
		true, then it is a straight.
		"""
		straight = True
		if len(playing) != 5:
			return False
		card_values = []
		for i in range(len(playing)):
			card_values.append(playing[i].point_value)
		card_values.sort()
		for i in range (len(playing)):
			if i != 4:
				if (card_values[i]) == (card_values[i + 1] - 1):
					pass
				else:
					straight = False
					break
		return straight

	
	def calculate_kinds(playing):
		"""
		This method picks a card in hand and
		checks it to see how many other cards
		in the hand share its rank. It repeats
		this for every card in the hand. If
		there are a certain amount of matches,
		it returns the corresponding variable.
		"""
		first_rank = 0
		count = 0
		for i in range (len(playing)):
			first_rank = playing[i].point_value
			for a in range (len(playing)):
				if playing[a].point_value == first_rank:
					if playing.index(playing[a]) == playing.index(playing[i]):
						pass
					else:
						count += 1
			count += 1
			if count == 3:
				return 3
			elif count == 4:
				return 4
			else:
				count = 0
		if count == 0:
			return count

	
	def calculate_full_house(playing):
		"""
		This method searches the current player's
		hand for pairs. If it finds two, it will
		then see if one of those pairs is actually
		a group of 3. If it is, then
		it reports that the hand is a full house.
		"""
		first_rank = 0
		pair_rank_1 = 0
		pair_rank_2 = 0
		total_1 = 0
		total_2 = 0
		pairs = 0
		for i in range (len(playing)):
			first_rank = playing[i].point_value
			for a in range (len(playing)):
				if playing[a].point_value == first_rank:
					if playing.index(playing[a]) == playing.index(playing[i]):
						pass
					else:
						if playing[a].point_value == pair_rank_1 or playing[a].point_value == pair_rank_2:
							pass
						else:
							pairs += 1
							if pair_rank_1 == 0:
								pair_rank_1 = playing[a].point_value
							elif pair_rank_2 == 0:
								if playing[a].point_value != pair_rank_1:
									pair_rank_2 = playing[a].point_value
		if pairs >= 2:
			for i in range (len(playing)):
				if playing[i].point_value == pair_rank_1:
					total_1 += 1
			for i in range (len(playing)):
				if playing[i].point_value == pair_rank_2:
					total_2 += 1
			if (total_1 + total_2) == 5:
				return True
		else:
			return False


	def calculate_pairs(playing):
		"""
		This method goes through the player's hand and
		picks the rank of the first card in that hand.
		Then it checks that rank to see if it pairs
		with another card. It repeats this for
		the entire hand and returns how many pairs
		it found.
		"""
		first_rank = 0
		pairs = 0
		pair_rank = 0
		for i in range (len(playing)):
			first_rank = playing[i].point_value
			for a in range (len(playing)):
				if playing[a].point_value == first_rank:
					if playing.index(playing[a]) == playing.index(playing[i]):
						pass
					else:
						if playing[a].point_value == pair_rank:
							pass
						else:
							pairs += 1
							pair_rank = playing[a].point_value
		if pairs == 0:
			return 0
		elif pairs == 1:
			return 1
		elif pairs >= 2:
			return 2
	
	
	def to_string(self):
		"""
		This method returns info about the hand.
		"""
		return ("Hand: " + self.name + " +" + str(self.dice_given) + " dice +" + str(self.score_given) + " points")


if __name__ == '__main__':
	print("This is the hands class.")