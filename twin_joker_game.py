#GRIFFIN MAKARI
#This is my joker twins game.
#It will test the following things taught in class. Lists, Decision Structures, Iterations, and loops.
#Also teach decomposing a large problem into smaller managable parts(in debugging the code)

#Two player game
#In turns player will play the game.


import random #importing random module(turns, shuffling up the words in the boards)
import os #to clear screen when required to
import time #to pause the screen for players to memorise the cards.

#Initialisations
NUM_ROWS = 6 #constant variable for rows
NUM_COLS = 6 #constant variable for columns
NUM_PLAYERS = 2 #Constant values for number of players
hidden_board = []  # storing the characters
playing_board = [] # alternate between showing characters and place holders during playtims

#this will return randomly between 0 & 1
#used to index the player's score.
turn = random.randint(0, NUM_PLAYERS-1)
#print(turn)


#CODE GOES HERE


#alternating turns goes here
turn = (turn + 1) % NUM_PLAYERS


time.sleep(2)
os.system("clear")


print(turn)

