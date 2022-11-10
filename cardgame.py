""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *
import random
NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2
cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")
def clearDeck():
for x in range(NUMCARDS):
cardLoc[x] = 0
def assignCard(location):
run = True
global cardLoc
while(run):
card = randint(0,51)
if cardLoc[Card] == location:
run = False
def showDeck():
  print("\n")
  print("Card location: ")
  print("# Card ")
  for x in range(NUMCARDS):
    cardName = rankName[(x%13] + suitName[(intx/13)]
    location = playerName[cardLoc[x]]
    print(str(x)+ "  " + cardName + "  " +str(location))
def showHand(location):
  print ("\n")
  print("Showing " + playerName[location] + "'s hand. \n")
  for x in range(NUMCARDS):
if card:pc(x) == location:
# equation ?
cardName = rankName[(x%13)] + " of " + suitName[(suitName[(int(x/13))]
print(cardName)
  
def main():
  clearDeck()
  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)
  showDeck()
  showHand(PLAYER)
  showHand(COMP) 
# if var == "main":
main()