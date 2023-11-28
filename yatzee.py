"""
File: pytzee.py
Author: Andrew Bumgardner
Date: 4/1/2022
Section: 21
E-mail: andrewb7@umd.edu
Description: This program allows the user to play a single-player modified
		  version of yahtzee
"""

import random

TOTAL_DICE = 5
DICE_FACES = 6


move_list = [
			'3 of a kind', 
			'three of a kind', 
			'4 of a kind', 
			'four of a kind',
			'full house',
			'chance',
			'pytzee',
			'small straight',
			'large straight',
			'count 1',
			'count 2',
			'count 3',
			'count 4',
			'count 5',
			'count 6',
			]

scorecard = {
			'3 of a kind' : 0, 
			'4 of a kind' : 0, 
			'full house' : 0,
			'small straight' : 0,
			'large straight' : 0,
			'chance' : 0,
			'pytzee' : 0,
			'count 1' : 0,
			'count 2' : 0,
			'count 3' : 0,
			'count 4' : 0,
			'count 5' : 0,
			'count 6' : 0,
}



def roll_dice():
	"""
	:return: a list containing five integers representing dice rolls between 1 and 6.
	"""
	roll_list = []
	for i in range(TOTAL_DICE):
		roll_list.append(random.randint(1, 6))
	return roll_list

def print_scorecard(score):
	# prints the scorecard to the user
	card_titles = []
	for key in scorecard:
		card_titles.append(key)

	print()
	print('\tscorecard')
	for i in range(6):
		print("{}'s".format(i+1), end=' ')
	print()
	for i in range(6):
		print(scorecard['count {}'.format(i+1)], end='   ')
	print()
	for i in range(7):
		print(card_titles[i], end='  ')
	print()
	for i in range(7):
		print(scorecard[card_titles[i]], end='             ')
	print()
	print()




def update_scorecard(roll, move, score):
	# handles score calculations and calls for the print scorecard function
	if move.split()[0] == 'count':
		score += int(move.split()[1]) * int(roll.count(int(move.split()[1])))
		scorecard[move] += int(move.split()[1]) * int(roll.count(int(move.split()[1])))
	elif move == '3 of a kind' or move == '4 of a kind':
		score += sum(roll)
		scorecard[move] += sum(roll)
	elif move == 'full house':
		score += 25
		scorecard[move] += 25
	elif move == 'small straight':
		score += 30
		scorecard[move] += 30
	elif move == 'large straight':
		score += 40
		scorecard[move] += 40
	elif move == 'chance':
		score += sum(roll)
		scorecard[move] += sum(roll)
	elif move == 'pytzee':
		if scorecard['pytzee'] == 0:
			score += 50
			scorecard[move] += 50
		else:
			score += 100
			scorecard[move] += 100
	print_scorecard(score)

def get_input(roll):
	# gets the user input of what move they would like to make with the given roll
	types = classify_roll(roll)

	flag = True
	while flag:
		move = input('How would you like to count this dice roll? ')
		if move == 'three of a kind':
			move = '3 of a kind'
		if move == 'four of a kind':
			move = '4 of a kind'
		if move.lower() == 'skip':
			flag = False
			update_scorecard(roll, 'invalid', score)
		elif move.lower() not in move_list:
			print('You must enter a valid move')
		elif move.lower() not in types:
			print('Move not accepted')
		elif scorecard[move] != 0:
			if move.lower() != 'pytzee':
				print('There is already a score in that slot')
			else:
				print('Move accepted')
				update_scorecard(roll, move.lower(), score)
		else:
			print('Move accepted')
			
			flag = False
			update_scorecard(roll, move.lower(), score)
			


def classify_roll(roll):
	# Creates a list of the number of each type of dice rolled
	count = [0,0,0,0,0,0]

	for dice in roll:
		count[dice-1] += 1

	# Returns the list of what the roll can be attributed to on the scorecard
	classifications = []
	temp = []

	for i in range(2):
		if count[i] != 0 and count[i+1] != 0 and count[i+2] != 0 and count[i+3] != 0 and count[i+4] != 0:
			temp.append('large straight')
	for i in range(3):
		if count[i] != 0 and count[i+1] != 0 and count[i+2] != 0 and count[i+3] != 0:
			temp.append('small straight')
	for i in range(6):
		if count[i] != 0:
			temp.append('count {}'.format(i+1))
		if count[i] == 3:
			temp.append('3 of a kind')
		if count[i] == 4:
			temp.append('4 of a kind')
		if count[i] == 5:
			temp.append('pytzee')
	if 2 in count and 3 in count:
		temp.append('full house')
	if scorecard['chance'] == 0:
		temp.append('chance')


	for i in temp:
		if i not in classifications:
			classifications.append(i)
	print(classifications)
	return classifications

def check_bonus():
	# checks for the count bonus and returns a boolean for if it should be added
	temp = 0
	for i in range(6):
		temp += scorecard['count {}'.format(i+1)]

	if temp > 62:
		return True
	else:
		return False

def play_game(num_rounds):
	# handles the setup for each game round
	for turn in range(num_rounds):
		print('***** Beginning round {} *****'.format(turn + 1))
		print('\tYour score is {}'.format(sum(scorecard.values())))
		current_roll = roll_dice()
		for number in current_roll:
			print('\t {}'.format(number), end='\t')
		print()
		get_input(current_roll)

	print()
	if check_bonus():
		print('Your final score was {}'.format(sum(scorecard.values()) + 35))
	else:
		print('Your final score was {}'.format(sum(scorecard.values())))


if __name__ == '__main__':
	score = 0
	num_rounds = int(input('What is the number of rounds that you want to play? '))
	seed = int(input('Enter the seed or 0 to use a random seed: '))
	if seed:
		random.seed(seed)
	play_game(num_rounds)
