'''
It is a blackjack game made using simple python functions
'''

import os
import random

deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]*4

def deal(deck):
	hand = []

	for i in range(2):
		random.shuffle(deck)
		card=deck.pop()	

		if card==11:
			card ="J"
		if card==12:
			card="Q"
		if card==13:
			card="K"
		if card==1:
			card="A"
		hand.append(card)

	return hand

def play_again():
	again=input("Do you want to play again? (Y/N): ").lower()

	if again=='y':
		dealer_hand=[]
		player_hand=[]
		game()
	else:
		print("Bye")
		exit()


def total(hand):
	total=0
	for card in hand:
		if card=="J" or card=="Q" or card=="K":
			total+=10
		elif card=="A":
			if total>=11:
				total+=1
			else:
				total+=11
		else:
			total+=card

	return total

def hit(hand):
	card=deck.pop()
	if card==11:
		card="J"
	if card==12:
		card="Q"
	if card==13:
		card="K"
	if card==1:
		card="A"
	
	hand.append(card)

	return hand

def clear():
	if os.name=='nt':
		os.system('CLS')

	if os.name=='posix':
		os.system('clear')

def print_results(dealer_hand,player_hand):
	clear()
	print("The dealer has a " + str(dealer_hand) + "for a total of "+ str(total(dealer_hand)))
	print("You have a "+ str(player_hand)+"for a total of "+ str(total(player_hand)))


def blackjack(dealer_hand,player_hand):
	if total(player_hand)==21:
		print_results(dealer_hand,player_hand)
		print("Congratulations you have got a blackjack")
		play_again()

	elif total(dealer_hand)==21:
		print_results(dealer_hand,player_hand)
		print("Sorry you lose. The dealer has a blackjack")
		play_again()

def score(dealer_hand,player_hand):
	if total(dealer_hand)==21:
		print_results(dealer_hand,player_hand)
		print("Sorry you lose. The dealer has a blackjack")

	elif total(player_hand)==21:
		print_results(dealer_hand,player_hand)
		print("Congratulations you won. You have got a blackjack")

	elif total(player_hand)>21:
		print_results(dealer_hand,player_hand)
		print("Sorry you are busted")

	elif total(dealer_hand)>21:
		print_results(dealer_hand,player_hand)
		print("Congratulations you won. The dealer is busted")

	elif total(dealer_hand)>total(player_hand):
		print_results(dealer_hand,player_hand)
		print("Sorry you lose.")

	elif total(dealer_hand)<total(player_hand):
		print_results(dealer_hand,player_hand)
		print("Congratulations you have won.")




def game():
	choice=0
	clear()
	print("Welcome to BLACKJACK!")
	dealer_hand=deal(deck)
	player_hand=deal(deck)
	while choice!="q":
		print("The dealer is showing "+str(dealer_hand[0]))
		print("You have a "+str(player_hand)+"and a total of "+str(total(player_hand)))
		blackjack(dealer_hand,player_hand)
		choice = input("Do you want to\n1. hit\n2. stand\n3. quit\n").lower()
		clear()

		if choice =="h":
			hit(player_hand)
			while total(dealer_hand)<17:
				hit(dealer_hand)
			score(dealer_hand,player_hand)
			play_again()

		elif choice=="s":
			while total(dealer_hand)<17:
				hit(dealer_hand)
			score(dealer_hand,player_hand)
			play_again()

		elif choice=="q":
			print("Bye!")
			exit()

if __name__ == "__main__":
	game()
